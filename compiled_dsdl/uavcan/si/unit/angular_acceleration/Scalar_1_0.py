# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/si/unit/angular_acceleration/Scalar.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.202833 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.angular_acceleration.Scalar
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Scalar_1_0(_dsdl_.CompositeObject):
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
                 radian_per_second_per_second: _ty_.Optional[_ty_.Union[int, float, _np_.float32]] = None) -> None:
        """
        uavcan.si.unit.angular_acceleration.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param radian_per_second_per_second: saturated float32 radian_per_second_per_second
        """
        self._radian_per_second_per_second: float

        self.radian_per_second_per_second = radian_per_second_per_second if radian_per_second_per_second is not None else 0.0

    @property
    def radian_per_second_per_second(self) -> float:
        """
        saturated float32 radian_per_second_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._radian_per_second_per_second

    @radian_per_second_per_second.setter
    def radian_per_second_per_second(self, x: _ty_.Union[int, float, _np_.float32]) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._radian_per_second_per_second = x
        else:
            raise ValueError(f'radian_per_second_per_second: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Scalar_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.radian_per_second_per_second):
            if self.radian_per_second_per_second > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.radian_per_second_per_second < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.radian_per_second_per_second)
        else:
            _ser_.add_aligned_f32(self.radian_per_second_per_second)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.angular_acceleration.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Scalar_1_0._DeserializerTypeVar_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "radian_per_second_per_second"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            radian_per_second_per_second=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.angular_acceleration.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'radian_per_second_per_second=%s' % self.radian_per_second_per_second,
        ])
        return f'uavcan.si.unit.angular_acceleration.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{?YWO-~d-5M3h(f*&CgPbP8_FkxmtaX5I<gv$yNG2Tq4r@MEjlbP;Gf2_MEBy!M5(upRN|JQ1EaS>%s)m>Gu->Z7_'
        'W#Lz2p>gqrr}czeUM9o}BWWo=)4UW3VY;fdl}<pof9#BB&KvQ5QVTeT?Nc~`t*}TGtuX)G(-EU8u`=;Wx`e8sFR3AvF;NObozyBh'
        'W)$xrER&Hi7H^<vgryI&_#FDT`i*aJ3SpH{=Zws~6Ba(gP5k~8L0H_EqU3X4D}+-=iHl@!YOjr~q?048xVv9!>i(9tN^<E)Db&yv'
        '(BD8vMy(^2<^qcK@c8JmJ+>vUF?SGCD5LQe-a%L=)=|Z&;a7paBThw!I3v&F!vjNE9FE1Y?9XDv2%DX5vz@g&-QC?z)@x^3Z!c@L'
        'UNpO{tkcc9z1HqtyVvbDA-?7FVlg~1luN2eEer}}TJb9(gayJigV4ZY8XjF4Fv%y=C7wXBS*%$U&P8nmqfT%*3lGRZjs=2g<A~&N'
        '7}ki@-Y|iQQjnUWtZ<SRx)Q0!5vK!fgdD1L>WNWnN2)>T$2{NpWYA3}t$kifMvRCi!B^(Xva_bt$}}1&{hyK2sgaUa(oCl1fQkxg'
        'k&6+^#XXNC6L3~+72BvhFLAujE?qF+1{S*OX9)LRN%!XBe2mALAHr>-YX}=Rf!IlvYZQe{4n(EVW0C3GI#SkV?y5V46%w6VWZ~fv'
        '<y@-aKSjmMm_76*ikw`}BEpE4Uce97>TmqCIsQ)d6bSmuK1aEgRMD^)&~XfwqG@r8v3rGxaZT05A9v_;oBKTZ4MEo{whIIR00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
