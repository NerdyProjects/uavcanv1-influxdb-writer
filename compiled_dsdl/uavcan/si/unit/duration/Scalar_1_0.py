# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/si/unit/duration/Scalar.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.215758 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.duration.Scalar
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
                 second: _ty_.Optional[_ty_.Union[int, float, _np_.float32]] = None) -> None:
        """
        uavcan.si.unit.duration.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param second: saturated float32 second
        """
        self._second: float

        self.second = second if second is not None else 0.0

    @property
    def second(self) -> float:
        """
        saturated float32 second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._second

    @second.setter
    def second(self, x: _ty_.Union[int, float, _np_.float32]) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._second = x
        else:
            raise ValueError(f'second: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Scalar_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.second):
            if self.second > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.second < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.second)
        else:
            _ser_.add_aligned_f32(self.second)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.duration.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Scalar_1_0._DeserializerTypeVar_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "second"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            second=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.duration.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'second=%s' % self.second,
        ])
        return f'uavcan.si.unit.duration.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{?YW%We}f6b<T=mWL`Tme3V#7oEvt5~d3_AaxU3DvH=4%N{!!OEcrakB}f$q6-j}EP>R^kMTuZHz_Ga_3GO9dCool'
        'viR%wLgVuIr}cyzUPQzQEomV?Q&xzGWU8!{kye1ee`2-EtkdG%q!w@iyJv6;JAR2&v_$_CM@Jd0A|oSLNgHvesg<gVPBL0h4Sto3'
        'gf{pBdBd-~pV=4CzteAggER2!gj%a5b5<Dm0JqKbHwgUFffNOw&$321wUpQ};BD!(mZh|Egb{ZS3PtU|aMlTvmK35I+8p{@STdu='
        'l2UO2`KEt-e3c&3qF3lU3@(Jx_zG{qZxUl^#i{1k3w_5rB^@F!j)%qrO|w9bL0S%GHrDXlout`L+nuD>>!jUwns)coR_l2)X{DVc'
        'O}ee#e!H6_O$fal%a{DJ5t*tu_(j512EKvM)IYjLC1I24icTTl&NmD~<f7IhqgHS@_YcTGjs+*R(w0aLM}C7C<#Z;{Q3z5~1mHi$'
        'xhh5Mkj!|Xw2;Fpo^E{9+LP6waAVH)K55j7j%&vXnGr39t_WS`YcaE=*vL4@B)*bKJe5h*iki_h1Q10|4ffZfvSEuOnF%=0ck*3C'
        '%L*j#+0~BcTw|cUc?W;*rL?av?<aVjZQCypRfFHUt%#YFOd$}Q<WQ6f6%;0YQwtnf>A7Z>NtR30VV?Sj$CPtf4gU+uUj*-wD-h)5'
        'rWY%WXyF9>fSvx<Ps8xD)YC%HUv&)Oma+<RM1zilu@WSS?1t<$BE~hXF8|Y!V}>~v{Q>F*woKgv000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)