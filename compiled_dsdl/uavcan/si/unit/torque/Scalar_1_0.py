# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/si/unit/torque/Scalar.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.232985 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.torque.Scalar
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
                 newton_meter: _ty_.Optional[_ty_.Union[int, float, _np_.float32]] = None) -> None:
        """
        uavcan.si.unit.torque.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param newton_meter: saturated float32 newton_meter
        """
        self._newton_meter: float

        self.newton_meter = newton_meter if newton_meter is not None else 0.0

    @property
    def newton_meter(self) -> float:
        """
        saturated float32 newton_meter
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._newton_meter

    @newton_meter.setter
    def newton_meter(self, x: _ty_.Union[int, float, _np_.float32]) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._newton_meter = x
        else:
            raise ValueError(f'newton_meter: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Scalar_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.newton_meter):
            if self.newton_meter > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.newton_meter < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.newton_meter)
        else:
            _ser_.add_aligned_f32(self.newton_meter)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.torque.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Scalar_1_0._DeserializerTypeVar_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "newton_meter"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            newton_meter=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.torque.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'newton_meter=%s' % self.newton_meter,
        ])
        return f'uavcan.si.unit.torque.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{?YWO-~d-5M2WZ0&0lFlZl)J4$SPwEDi@Rns8Y`BF3BP^i0?8bTTtN^vAMmLLvu^B%NqN`Oo}8*076<80J)+S6}bd'
        'n=kXfe$O?oKL5NL3nTJ?8PJmF@-t6z2w19$N*QSZ{ljCcU22_%5912(61UIs47dCOD|tcqGslN1F9Rb3S4taLrB56L$0^UbM!&>{'
        'pp8@|W(~jiaT;G@?_RI*4bRc9FmA1uiL+qv6W+Da-z4-4`x0_7+hmyuZaK5{dUusqS{BmEA!R(+&lR`-l38Jiv@C~mU^DD(P|K7X'
        '%L*j`vvvRU=(@Zv3*HcRP(wtc@fF{rUuVYhQgAJ9Hu_F|3O*oJoTvx)HBT+kHzdpcG^QSYvlBJjak~@k?snpCJC3`1ajW&R8MWe0'
        '6i40G?q0haMNO<{xg=Zgt0kOTRk8vskjV2)s1$vJK<=O15R@h3$(hbD+sxJs5fxBrNVx@p7yc3J%Ml1xDQ%e)c<9%dQBJ2oKn|?p'
        'M8m5vQw4;MBn|sYgB+CM<m$uLjx77R8;NA+RFhwHSh*yZDbp};c|B!z95XEnjSOq6gcGZT6RQNRpczaOkT_)A&~y!@tuHy0Dd0u6'
        'm2DH(Bqsr1T;F-7HznHJZ}h9LrG0z#KBnjN;(m^)3jM}iP0YAR6w#nf4xmuvqWV_vD$tykp84iJOEXDc%wqrehzlXh!GB5Fs~SCY'
        'IguRSMybP)=ML}(ZuK^PnuLCsYSIXMOD-Y0g)D1JQou)buvpuYw5_X`8H_4kUj0*tE-{Hqf<H&o+|1tt000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
