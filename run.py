#!/usr/bin/env python3

import sys
import threading
import time
from datetime import datetime
import configparser
import influxdb
import os
import queue
import signal
import traceback
from collections import defaultdict

import pathlib
import asyncio
import logging
import importlib
import pyuavcan

from pyuavcan.presentation import Presentation, Subscriber
from pyuavcan.transport.can import CANTransport
from pyuavcan.transport.can.media.socketcan import SocketCANMedia
from pyuavcan.dsdl._builtin_form import to_builtin

running = True

# Prepare DSDL for uavcan v1
compiled_dsdl_dir = pathlib.Path(__file__).resolve().parent / "compiled_dsdl"
sys.path.insert(0, str(compiled_dsdl_dir))

try:
  import housebus
  import pyuavcan.application
except (ImportError, AttributeError):  # Redistributable applications typically don't need this section.
    logging.warning("Transcompiling DSDL, this may take a while")
    src_dir = pathlib.Path(__file__).resolve().parent
    pyuavcan.dsdl.compile_all(
        [
            src_dir / "custom_data_types/housebus",
            src_dir / "public_regulated_data_types/uavcan/",
        ],
        output_directory=compiled_dsdl_dir,
    )
    importlib.invalidate_caches()  # Python runtime requires this.
    import housebus
    import pyuavcan.application

# Import other namespaces we're planning to use. Nested namespaces are not auto-imported, so in order to reach,
# say, "uavcan.node.Heartbeat", you have to "import uavcan.node".
import uavcan.node  # noqa
import housebus.heating.heatmeter_1_0
import housebus.heating.heating_status_1_0
import housebus.electricity.meter_1_0


class App:
    SUBSCRIBE_TO = [
      { 'port': 1000, 'data_type': housebus.heating.heatmeter_1_0, 'name': 'heatmeter'},
      { 'port': 1010, 'data_type': housebus.electricity.meter_1_0, 'name': 'meter_heatpump'},
      { 'port': 1001, 'data_type': housebus.heating.heating_status_1_0, 'name': 'heating_status'},
    ]

    def __init__(self, transport, record_method, influxdb_queue) -> None:
        node_info = uavcan.node.GetInfo_1_0.Response(
            software_version=uavcan.node.Version_1_0(major=1, minor=0),
            name="uavcanv1.logger",
        )
        self.influxdb_queue = influxdb_queue
        self.record_method = record_method

        # The Node class is basically the central part of the library -- it is the bridge between the application and
        # the UAVCAN network. Also, it implements certain standard application-layer functions, such as publishing
        # heartbeats and port introspection messages, responding to GetInfo, serving the register API, etc.
        # The register file stores the configuration parameters of our node (you can inspect it using SQLite Browser).
        self._node = pyuavcan.application.make_node(info = node_info, transport = transport)

        # Published heartbeat fields can be configured as follows.
        self._node.heartbeat_publisher.mode = uavcan.node.Mode_1_0.OPERATIONAL  # type: ignore
        self._node.heartbeat_publisher.vendor_specific_status_code = os.getpid() % 100


        self._node.start()  # Don't forget to start the node!

    async def run(self) -> None:
        """
        The main method that runs the business logic. It is also possible to use the library in an IoC-style
        by using receive_in_background() for all subscriptions if desired.
        """

        def make_handler(port):
          async def handler(msg, transfer):
            #print(port)
            #print(str(msg._MODEL_))

            self.record_method(to_builtin(msg), transfer.source_node_id, str(msg._MODEL_), port, self.influxdb_queue)
          
          return handler

        self.subscriptions = []
        for s in self.SUBSCRIBE_TO:
          subscriber = self._node.presentation.make_subscriber(s['data_type'], s['port'])
          subscriber.receive_in_background(make_handler(s['port']))

          self.subscriptions.append(
            subscriber
          )

        logging.info("Application started")
        print("Running. Press Ctrl+C to stop.", file=sys.stderr)       

    def close(self) -> None:
        """
        This will close all the underlying resources down to the transport interface and all publishers/servers/etc.
        All pending tasks such as serve_in_background()/receive_in_background() will notice this and exit automatically.
        """
        self._node.close()


running = True

  

def shutdown(signal, frame):
  global running
  running = False


signal.signal(signal.SIGTERM, shutdown)

def influxdb_writer(q, influxdb_client):
  while running:
    buffer = list()
    try:
      buffer.append(q.get(timeout=2))
    except queue.Empty:
      continue

    while not q.empty():
      buffer.append(q.get_nowait())
      q.task_done()

    try:
      influxdb_client.write_points(
        buffer,
        time_precision="ms",
        batch_size=200,
      )
    except:
      # ignore any writing error, just print it and continue
      print(traceback.format_exc())

    q.task_done()
    time.sleep(1)




def read_config(filename):
  config = configparser.ConfigParser()
  config.read(os.path.join(os.path.dirname(__file__), 'defaults.ini'))
  config.read(filename)
  return config


def record_event_data(msg, source_node_id, type_name, port, influxdb_queue=None):
  if influxdb_queue is None:
    raise Exception('please pass in an influxdb_queue option')

  fields = msg

  if len(fields) > 0:
      write_to_influxdb(source_node_id, type_name, port, fields, influxdb_queue)


def write_to_influxdb(source_node_id, type_name, port, fields, influxdb_queue, **kwargs):
  data = {
    "measurement":
        type_name,
    "tags": {
        "node_id": source_node_id,
        "port": port
    },
    "time": int(round(time.time()*1000)),
    "fields":
        fields,
  }
  extra_tags = kwargs.get('extra_tags')
  if extra_tags:
    data['tags'].update(extra_tags)

  influxdb_queue.put(data)
  
def main(config_filename, *args):
  config = read_config(config_filename)
  influxdb_queue = queue.Queue()
  can_if = config.get('canbus', 'ifname')
  node_id = config.getint('node', 'id')
  transport = CANTransport(SocketCANMedia(can_if, 8), node_id)
  app = App(transport, record_event_data, influxdb_queue)
  
  logging.root.setLevel(logging.INFO)

  influxdb_client = influxdb.InfluxDBClient(
      config.get('influxdb', 'host'),
      config.getint('influxdb', 'port'),
      config.get('influxdb', 'username'),
      config.get('influxdb', 'password'),
      config.get('influxdb', 'database'),
      config.getboolean('influxdb', 'ssl'),
      verify_ssl=True,
      timeout=5,
      retries=5,
  )
  
  # client might not be allowed to create database, but it could happen here
  #influxdb_client.create_database(config.get('influxdb', 'database'))

  influxdb_thread = threading.Thread(
      target=influxdb_writer,
      kwargs={
          'q': influxdb_queue,
          'influxdb_client': influxdb_client
     })
  influxdb_thread.start()

  print('started')
  try:
      asyncio.get_event_loop().run_until_complete(app.run())
      asyncio.get_event_loop().run_forever()
  except KeyboardInterrupt:
      pass
  finally:
      app.close()


if __name__ == "__main__":
    main(*sys.argv[1:])