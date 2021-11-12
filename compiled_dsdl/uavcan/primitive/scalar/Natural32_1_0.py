# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/primitive/scalar/Natural32.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:22.670758 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.scalar.Natural32
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Natural32_1_0(_dsdl_.CompositeObject):
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
                 value: _ty_.Optional[_ty_.Union[int, _np_.uint32]] = None) -> None:
        """
        uavcan.primitive.scalar.Natural32.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint32 value
        """
        self._value: int

        self.value = value if value is not None else 0

    @property
    def value(self) -> int:
        """
        saturated uint32 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _ty_.Union[int, _np_.uint32]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 4294967295:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 4294967295]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Natural32_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u32(max(min(self.value, 4294967295), 0))
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.primitive.scalar.Natural32.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Natural32_1_0._DeserializerTypeVar_) -> Natural32_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_u32()
        self = Natural32_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.primitive.scalar.Natural32.1.0'
        assert isinstance(self, Natural32_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.primitive.scalar.Natural32.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8W}=N@0{?YWOKTKC5MD{vgv19S!K)h&5)YX%2K)gEf~;ACQE$?8Pgk}Zdb)>xth++M925gB3Mv1uHM_}fjATw#)T6&g&DZ5W'
        'KbJbwFF$N1GDuUf0A6#Wzi?roV3n&I7jy*7caNe^RZJe<Pa42;d~%8>xRblg@|x<~iH|C7i^l6(M?HcfRNQc13^)yOv;Pe9DjR_h'
        '+F4Ycyz=oPKF9v8e&;)$VqRxFMz2MR5bzV;1Z&=ex%*0kkqbC$O!CNCY%$(6K8J{T^Meg~XhFWV5r*LZ<+jd*j?91^Muq(zEw6Zp'
        'tacJmZRH1tmy6o5;w9A%+7c1!e8YE`w^)eWO77*=ML&{I-P|2<lL)~wldi(t!6bOzyuzP}$xPZ4R6Vs32#tisL&YOVJj?gku^xkD'
        'jq{OdiG#esf=j*vDi~l5r?+w}m8+plq(FJ>JP_G(=G16!SKDKg#!~El_T;fIn<R{`n1^99?JEl{!^KcJ*RGt|Th8q*_KK&)tc!GI'
        'iU)$=!Nykok*)yG)V6v=goO#1A76U2P=*@g^&In^7dpO~=0}uXc$1fyYcTh2S`sF;aKwd>96;^J`ADbswgJzh^9zS>vr1{YAGMe7'
        'A95+R9sbv(p10LOGDLTBy-FKqM*hN`e(!e>bmYx!5%yP;AiA}-?eS2+$8E6E9uNuKPOmW-H{4GDgFzBOBvJeYQMxI;m;(R+'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
