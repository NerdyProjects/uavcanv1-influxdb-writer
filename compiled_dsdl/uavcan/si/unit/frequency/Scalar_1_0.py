# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/si/unit/frequency/Scalar.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.206420 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.frequency.Scalar
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
                 hertz: _ty_.Optional[_ty_.Union[int, float, _np_.float32]] = None) -> None:
        """
        uavcan.si.unit.frequency.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param hertz: saturated float32 hertz
        """
        self._hertz: float

        self.hertz = hertz if hertz is not None else 0.0

    @property
    def hertz(self) -> float:
        """
        saturated float32 hertz
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._hertz

    @hertz.setter
    def hertz(self, x: _ty_.Union[int, float, _np_.float32]) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._hertz = x
        else:
            raise ValueError(f'hertz: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Scalar_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.hertz):
            if self.hertz > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.hertz < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.hertz)
        else:
            _ser_.add_aligned_f32(self.hertz)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.frequency.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Scalar_1_0._DeserializerTypeVar_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "hertz"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            hertz=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.frequency.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'hertz=%s' % self.hertz,
        ])
        return f'uavcan.si.unit.frequency.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{?YWOHUL*5MBeT2tGn2Ug0EgU}hh)I2^oa!es@C7;mQ2J>9$ANzcQ6th*#6a?nW9i6)f4%s*reyRe91PSsOYU)NXP'
        '*IyTZ|5<2Ueqp_uaLaW>tT2jdbwZgI5y{HDDy?z?!sBCSeCE6nA10N63)nt`Q`ibkQqUap>z<A>T0~YwzECb281dPQBAZ0V8P(K4'
        'SRx}~tSSqTjqu>(EWUvLy?*06oIzM2)H$P=cf!IaxNE5EA_&cWB{ZK8vrIU3l(>4ryV@(Ga^=(rD<1CalDdEStPrLg(V`eS3H=R('
        '%&2uFFS!7@7M>qnwbyOY8_XTlDWuW(2Ja!P5$kBdso^()ejrXxhqxHe>x&15W)A6FT+99}MvSo8O<J9_(@l1FyJ@eJroFwi-G13h'
        '+G#gQlU{pwuhUDC7SwlnCYzxtg>fek76~si2o3y8!?PQkBy2L3=oI9pT(!uMi^_<MI>F&QJRt)$7MxV2aYS)A46DSJ-edw3T9At3'
        '{K3Ss%th>Rm+_!9LJf;}s`#kAql$s{W6pNI81#yXE6=pbh!I1t>s#ik*jZC-Rb1O7zP3p`wMo>DTG6xykcOld2QZ>=wTdH^2{@Nq'
        'avSL~jmvv+rSW{%Sm<t_Av}7m+}q3ZF&<}XhXqnr5H{`tv6GyY$OI=j5P69Xs&#r-2}50J=AOAvGO5sqG7V3UDCepe{#PVl)!9R@'
        'k>uod77<2NdjUUTtH1HfGJGu66bSlDo*~^_6}25PpyN7tP+Jn$TX!!LF|KHF`JN6vv&^&TFP8Bb%iaS300'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)