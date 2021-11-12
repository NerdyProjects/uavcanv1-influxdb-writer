# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/primitive/scalar/Integer16.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:22.662919 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.scalar.Integer16
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Integer16_1_0(_dsdl_.CompositeObject):
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
                 value: _ty_.Optional[_ty_.Union[int, _np_.int16]] = None) -> None:
        """
        uavcan.primitive.scalar.Integer16.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated int16 value
        """
        self._value: int

        self.value = value if value is not None else 0

    @property
    def value(self) -> int:
        """
        saturated int16 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _ty_.Union[int, _np_.int16]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if -32768 <= x <= 32767:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [-32768, 32767]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Integer16_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_i16(max(min(self.value, 32767), -32768))
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of uavcan.primitive.scalar.Integer16.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Integer16_1_0._DeserializerTypeVar_) -> Integer16_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_i16()
        self = Integer16_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of uavcan.primitive.scalar.Integer16.1.0'
        assert isinstance(self, Integer16_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.primitive.scalar.Integer16.1.0({_o_0_})'

    _EXTENT_BYTES_ = 2

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8W}=N@0{?YWU279T6pgg8rS+r1;;XF>QXjf&Uit$R1c{Bsh;K5??A&AqW_OnPh>1|J4~oSBg<k)!cat=!mF&|U&iy#&p1WT+'
        '|NPu&&A#-co=PuG#ymL9jsC)gfs7TltgY7pFx?*n7mE-be3;gNSNQw_&+#a=S;b4j4<jEJyvk~)OC9tWGGB1RUG}C5Fap;-!L-fB'
        ';JmgKs#e<ixQMT?cc<6-ju)7A84tl}5d(PqgzIQ6lQ6YkYcO&}XNO51I13HOb>&Nnm^uSJsz5F{{;O=42_2Y$Y7`Xq_NaBiePE@P'
        'fNDQIKD%zylx437J8dA6)B1+*G3_%ScqO@$HyizkLbX$S%uS^En@rjQQwyWu>Cp}KOibsCJx6t*I-b}_s2vnMfW*u6fDQEoB&)3p'
        'OiS#i4)Zp;0thg`YEH9K$dxT2kEA~zS_dRHpZhfK9_wmo;zWw$&yE~+c^!q(1#>WprkS$Zq+b-}%gyC;bMvLSSvPx;&9jh%DDH`Z'
        'gDNz;AL|0}QXQ(NBv=@a>Dje2tIbeixc$a-@1+iJXYT<$7v7`|W@}6b>zep!DJ*FrCZ|wZ@;%U@y{p0TVBN~$yR1-}u19s#!!s_W'
        'u15bQsgnlnM?-R_w^8aaH}V%A_4a;yK__0%8)0ud3X)susyQAC_@oK8nggN*H`O}~CN-~Se?dPAFQUl)0&m)P%$5TH00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)