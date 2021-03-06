# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/metatransport/ethernet/Frame.0.1.uavcan
#
# Generated at:  2021-11-11 23:08:22.689306 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.metatransport.ethernet.Frame
# Version:       0.1
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_
import uavcan.metatransport.ethernet


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Frame_0_1(_dsdl_.CompositeObject):
    """
    Generated property settings use relaxed type signatures, accepting a large variety of
    possible representations of the value, which are automatically converted to a well-defined
    internal representation. When accessing a property, this strict well-defined internal
    representation is always returned. The implicit strictification enables more precise static
    type analysis.

    The value returned by the __repr__() method may be invariant to some of the field values,
    and its format is not guaranteed to be stable. Therefore, the returned string representation
    can be used only for displaying purposes; any kind of automation build on top of that will
    be fragile and prone to mismaintenance.
    """
    def __init__(self,
                 destination: _ty_.Optional[_ty_.Union[_np_.ndarray, _ty_.List[int], bytes, bytearray]] = None,
                 source:      _ty_.Optional[_ty_.Union[_np_.ndarray, _ty_.List[int], bytes, bytearray]] = None,
                 ethertype:   _ty_.Optional[uavcan.metatransport.ethernet.EtherType_0_1] = None,
                 payload:     _ty_.Optional[_ty_.Union[_np_.ndarray, _ty_.List[int], bytes, bytearray, str]] = None) -> None:
        """
        uavcan.metatransport.ethernet.Frame.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param destination: saturated uint8[6] destination
        :param source:      saturated uint8[6] source
        :param ethertype:   uavcan.metatransport.ethernet.EtherType.0.1 ethertype
        :param payload:     saturated uint8[<=9216] payload
        """
        self._destination: _np_.ndarray
        self._source:      _np_.ndarray
        self._ethertype:   uavcan.metatransport.ethernet.EtherType_0_1
        self._payload:     _np_.ndarray

        if destination is None:
            self.destination = _np_.zeros(6, _np_.uint8)
        else:
            if isinstance(destination, (bytes, bytearray)) and len(destination) == 6:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._destination = _np_.frombuffer(destination, _np_.uint8)
            elif isinstance(destination, _np_.ndarray) and destination.dtype == _np_.uint8 and destination.ndim == 1 and destination.size == 6:
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._destination = destination
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                destination = _np_.array(destination, _np_.uint8).flatten()
                if not destination.size == 6:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'destination: invalid array length: not {destination.size} == 6')
                self._destination = destination
            assert isinstance(self._destination, _np_.ndarray)
            assert self._destination.dtype == _np_.uint8
            assert self._destination.ndim == 1
            assert len(self._destination) == 6

        if source is None:
            self.source = _np_.zeros(6, _np_.uint8)
        else:
            if isinstance(source, (bytes, bytearray)) and len(source) == 6:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._source = _np_.frombuffer(source, _np_.uint8)
            elif isinstance(source, _np_.ndarray) and source.dtype == _np_.uint8 and source.ndim == 1 and source.size == 6:
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._source = source
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                source = _np_.array(source, _np_.uint8).flatten()
                if not source.size == 6:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'source: invalid array length: not {source.size} == 6')
                self._source = source
            assert isinstance(self._source, _np_.ndarray)
            assert self._source.dtype == _np_.uint8
            assert self._source.ndim == 1
            assert len(self._source) == 6

        if ethertype is None:
            self.ethertype = uavcan.metatransport.ethernet.EtherType_0_1()
        elif isinstance(ethertype, uavcan.metatransport.ethernet.EtherType_0_1):
            self.ethertype = ethertype
        else:
            raise ValueError(f'ethertype: expected uavcan.metatransport.ethernet.EtherType_0_1 '
                             f'got {type(ethertype).__name__}')

        if payload is None:
            self.payload = _np_.array([], _np_.uint8)
        else:
            payload = payload.encode() if isinstance(payload, str) else payload  # Implicit string encoding
            if isinstance(payload, (bytes, bytearray)) and len(payload) <= 9216:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._payload = _np_.frombuffer(payload, _np_.uint8)
            elif isinstance(payload, _np_.ndarray) and payload.dtype == _np_.uint8 and payload.ndim == 1 and payload.size <= 9216:
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._payload = payload
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                payload = _np_.array(payload, _np_.uint8).flatten()
                if not payload.size <= 9216:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'payload: invalid array length: not {payload.size} <= 9216')
                self._payload = payload
            assert isinstance(self._payload, _np_.ndarray)
            assert self._payload.dtype == _np_.uint8
            assert self._payload.ndim == 1
            assert len(self._payload) <= 9216

    @property
    def destination(self) -> _np_.ndarray:
        """
        saturated uint8[6] destination
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._destination

    @destination.setter
    def destination(self, x: _ty_.Union[_np_.ndarray, _ty_.List[int], bytes, bytearray]) -> None:
        if isinstance(x, (bytes, bytearray)) and len(x) == 6:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._destination = _np_.frombuffer(x, _np_.uint8)
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size == 6:
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._destination = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size == 6:  # Length cannot be checked before casting and flattening
                raise ValueError(f'destination: invalid array length: not {x.size} == 6')
            self._destination = x
        assert isinstance(self._destination, _np_.ndarray)
        assert self._destination.dtype == _np_.uint8
        assert self._destination.ndim == 1
        assert len(self._destination) == 6

    @property
    def source(self) -> _np_.ndarray:
        """
        saturated uint8[6] source
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._source

    @source.setter
    def source(self, x: _ty_.Union[_np_.ndarray, _ty_.List[int], bytes, bytearray]) -> None:
        if isinstance(x, (bytes, bytearray)) and len(x) == 6:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._source = _np_.frombuffer(x, _np_.uint8)
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size == 6:
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._source = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size == 6:  # Length cannot be checked before casting and flattening
                raise ValueError(f'source: invalid array length: not {x.size} == 6')
            self._source = x
        assert isinstance(self._source, _np_.ndarray)
        assert self._source.dtype == _np_.uint8
        assert self._source.ndim == 1
        assert len(self._source) == 6

    @property
    def ethertype(self) -> uavcan.metatransport.ethernet.EtherType_0_1:
        """
        uavcan.metatransport.ethernet.EtherType.0.1 ethertype
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._ethertype

    @ethertype.setter
    def ethertype(self, x: uavcan.metatransport.ethernet.EtherType_0_1) -> None:
        if isinstance(x, uavcan.metatransport.ethernet.EtherType_0_1):
            self._ethertype = x
        else:
            raise ValueError(f'ethertype: expected uavcan.metatransport.ethernet.EtherType_0_1 got {type(x).__name__}')

    @property
    def payload(self) -> _np_.ndarray:
        """
        saturated uint8[<=9216] payload
        DSDL does not support strings natively yet. To interpret this array as a string,
        use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
        .payload.tobytes().decode()
        When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._payload

    @payload.setter
    def payload(self, x: _ty_.Union[_np_.ndarray, _ty_.List[int], bytes, bytearray, str]) -> None:
        x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
        if isinstance(x, (bytes, bytearray)) and len(x) <= 9216:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._payload = _np_.frombuffer(x, _np_.uint8)
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 9216:
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._payload = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size <= 9216:  # Length cannot be checked before casting and flattening
                raise ValueError(f'payload: invalid array length: not {x.size} <= 9216')
            self._payload = x
        assert isinstance(self._payload, _np_.ndarray)
        assert self._payload.dtype == _np_.uint8
        assert self._payload.ndim == 1
        assert len(self._payload) <= 9216

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Frame_0_1._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.destination) == 6, 'self.destination: saturated uint8[6]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.destination)
        assert len(self.source) == 6, 'self.source: saturated uint8[6]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.source)
        _ser_.pad_to_alignment(8)
        self.ethertype._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.payload) <= 9216, 'self.payload: saturated uint8[<=9216]'
        _ser_.add_aligned_u16(len(self.payload))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.payload)
        _ser_.pad_to_alignment(8)
        assert 128 <= (_ser_.current_bit_length - _base_offset_) <= 73856, \
            'Bad serialization of uavcan.metatransport.ethernet.Frame.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Frame_0_1._DeserializerTypeVar_) -> Frame_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "destination"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, 6)
        assert len(_f0_) == 6, 'saturated uint8[6]'
        # Temporary _f1_ holds the value of "source"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, 6)
        assert len(_f1_) == 6, 'saturated uint8[6]'
        # Temporary _f2_ holds the value of "ethertype"
        _des_.pad_to_alignment(8)
        _f2_ = uavcan.metatransport.ethernet.EtherType_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f3_ holds the value of "payload"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u16()
        assert _len0_ >= 0
        if _len0_ > 9216:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 9216')
        _f3_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
        assert len(_f3_) <= 9216, 'saturated uint8[<=9216]'
        self = Frame_0_1(
            destination=_f0_,
            source=_f1_,
            ethertype=_f2_,
            payload=_f3_)
        _des_.pad_to_alignment(8)
        assert 128 <= (_des_.consumed_bit_length - _base_offset_) <= 73856, \
            'Bad deserialization of uavcan.metatransport.ethernet.Frame.0.1'
        assert isinstance(self, Frame_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'destination=%s' % _np_.array2string(self.destination, separator=',', edgeitems=10, threshold=1024, max_line_width=10240000),
            'source=%s' % _np_.array2string(self.source, separator=',', edgeitems=10, threshold=1024, max_line_width=10240000),
            'ethertype=%s' % self.ethertype,
            'payload=%s' % _np_.array2string(self.payload, separator=',', edgeitems=10, threshold=1024, max_line_width=10240000),
        ])
        return f'uavcan.metatransport.ethernet.Frame.0.1({_o_0_})'

    _EXTENT_BYTES_ = 9232

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8W}=N@0{^{MTW=dh6n5HNoTe@5g;w0u5tLpKT{}&J3Q|Sg;<Tv~6OuF%0yG_a$3D}ncULpBZd`<Dk&1{kQVZQaAn{ZQc;XQW'
        'i9f+l;>_+kj*~cumqv;_o;h>oJ2T(+9X}j?{`*8O`7>w2j;mbHp^8hvJn?|lJnqnX&<X=3G>^@Z6)mH>jwE00ggky0UwjmQ6JIbR'
        ')MqVRe<xz?I`f?t*Gx<1t1yt-;TpK~xpwAc5|yWIE|m!U7;<K8EgL_JE4j+h_wl3HOi-q^6tzfm6@P{K2O!&uip|KJ;GWw<bcni4'
        'Gpa32^TvSfQnF5LPR@x9?k;e@si9=2`fEEvxyM`F*IBXwSVAdULW?#=oVepF(e$}H?`z)VvOnJhtqD!N<hZz!N2GP8G;IYgkKuK5'
        'YN?yZZgXzn+M->u*Yh}DMz~aI=DSR~+Y|i|)yz0%3Rzv~PFxu^!?fn9*qrOa?FA!pz4Lo)4qq2Ky@VC~n!z;(X%NPS3`(Lpty<uT'
        'Iu^aiTLE5%#<%=5<dW$?_KF^*brASI;F#mfJmgyJ9e04PBX*d^xL2x?=P}vY8HBmo%!_#ZB)(9|KUFoXe3-U`A6JTYz&7k)%wA~Z'
        'F`KnAWJ7aLEBW*@!aL_1A=1<Gt{T;B4j3^LE>~LkNeMBgas#X@7vtJw3J*@esciHbyqS&8RPsRJEWC?P0Ot_=d3Y~bf=f`$Vy0m>'
        '8(m4N`zQ^#+A9G*t`y-K{+IRw4CNlmQ58h8j$FA3xB8$R$VMaP{Qfd5+d)D~7=!Vy>fkUcZCkoteUrWVM$AZh`Pu15P5wsUTS9J8'
        'X1~4jOLT1}*$Y?ATU}D&TS%_#WAw==znr`T^SYUF&v-+!x}8O4=jXC9uAAY@#hELy6-aVT_x=mY!P4?l1_Wf59q!vSvorrAO;XVZ'
        'dn6i}o|(NoyOoKX6WctE);g(S+Kd1$1h5X@!q>0~k0Ue)m*a)hndWZ1X^zr{^(SiIkP0`hnqxGj04{i(h79Fz9uy#G@j`^ARA>Z}'
        'qyH3A7PO}>3BTb*8*c5=eTg<M3t?14%~Hvms1Q7*=ankkROq8lp-Y{@7ImDWGv%bQsC^1dArNU@5)rfo@^ceznm<-Dt0G$)Nj>9>'
        'B1{pNHv}3bsddPFxm+g8yeSl(YoC>rA`Jl|?hs5u=1bL*b7&QWA|A#N{0w{#*NAE{&m#&I!ZisR+fLBHG(lL&lyJGkqjW%OoJchF'
        'HpURVEOMu`cB52v;=QGdR<y)iSNP3cezil&lPG2EZebdY=AP(!5_LUkb={S-+Ainu<ZhGJvP;n?&FM9UO$Hmxp!PJ-h!%5a&GD{R'
        'H*9lE`_~R8zg-!!98EV3DF0QIxMicir@7m<W4#?8-}dTV7t)vN^fL3Ce7_DbO4kz)NBo0~G6&ag=g3fQAFt#pyZPIb`v+#PFcz|o'
        '7cgv4H_g;a6k66R%bGS)Ix!(~FTz$w8ullQA{V0266r%y5!Wv|*djPQu{F-YG57-J;aB(){(;{j_;C|{s=_nVemVL~eqn9bCOo$~'
        '{4NpKmEvV*I#nXZrlk;$Pa7(Gj`iO|^FBcYEoF7&iCTz@1ziu_s1?4Ca<WR2Xx3riTZ&_dzfLSLE60WTYGw8Fr7|tA-YPFw%d3S?'
        '7FKDwI#pb}K1f`@Y>j$zf2Co6TQ<F{$SHVH8R~Dt2|wVoluCDT_HJ+XMW*c?(?6%dA<l-|gVW4ArvFTXA0kN~W+d%TzH7yj)%h1e'
        '>x6Hz3jhE'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
