# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/primitive/scalar/Real16.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:22.675564 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.scalar.Real16
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Real16_1_0(_dsdl_.CompositeObject):
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
                 value: _ty_.Optional[_ty_.Union[int, float, _np_.float16]] = None) -> None:
        """
        uavcan.primitive.scalar.Real16.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated float16 value
        """
        self._value: float

        self.value = value if value is not None else 0.0

    @property
    def value(self) -> float:
        """
        saturated float16 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _ty_.Union[int, float, _np_.float16]) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -65504.0 <= x <= 65504.0
        if in_range or not _np_.isfinite(x):
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [-65504, 65504]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Real16_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.value):
            if self.value > 65504.0:
                _ser_.add_aligned_f16(65504.0)
            elif self.value < -65504.0:
                _ser_.add_aligned_f16(-65504.0)
            else:
                _ser_.add_aligned_f16(self.value)
        else:
            _ser_.add_aligned_f16(self.value)
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of uavcan.primitive.scalar.Real16.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Real16_1_0._DeserializerTypeVar_) -> Real16_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_f16()
        self = Real16_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of uavcan.primitive.scalar.Real16.1.0'
        assert isinstance(self, Real16_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.primitive.scalar.Real16.1.0({_o_0_})'

    _EXTENT_BYTES_ = 2

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8W}=N@0{?YWO-~d-5M2W+2!22$9(7NOQD(pZQ4bz8a#=wF#)~1H?&;p0PI|h>{#bWSNaUcAq!Udj|DM0aYGz?k!(661RrR{w'
        'd(~g2fBl|noqq9NJ>rh5j5uK>Rq``sN@S!kRc)N~0^*H*Z$sgO74Js1fD?Fl1c$I3+eFg}^LGOs6jW!mm6h~zATn1_MQyexs9M{E'
        'I7<e?I%zbNtvK_39G^h<O1Je5jv&qx>b;dLc;VmxE}QAR2x5Cn3dJY0%n?pKB|Z&!S^N2X5U*`1L;c@$<_VLYD53klgzf@D7SwrC'
        '87`n)ig$L;+EZKh3Uk{jg)~}UVGrUGah_^UEx!o#9dRn!*U|@`F78=cc%<)8maTD&7_q&%v9Y=i2`R9$9oqw{0yaz&ZVHIm>mk;v'
        'QOAnf3MaHroH|l_(MLU>cRs8<SzUknxbrCe4iJOJ+ZR+NY}B}Q2<3xv(IH!&kP7MrhvRsY^yE-*QXA`u<ggPLi8H|#0uxG*nj)9@'
        'F)vLe@_@SLJ!6IJ>%1|4u(l#~PlX|8E1xW`jm_)8lq`r9{h-n<6NlWmDL;24Z#E`xHYQukR<ouAkVQ!y-fxj}GISsd0mtQXY$b7+'
        'LLu*;`90AcEB(J`h}U0A|K{|(kH@j|af+B4V&^gtH>#LHCOFErs0?mX^6YIbEcM1t_U9@oN{KsJK8v?@Dd$r6|0^nAr0h;mNOtsZ'
        '77-fLf538g;iqHxaOwsKy0d{H-Ad}Tni$Yw3TD!JqP(elj)-AR_37K%3Cyv;vOn{smV@a7000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)