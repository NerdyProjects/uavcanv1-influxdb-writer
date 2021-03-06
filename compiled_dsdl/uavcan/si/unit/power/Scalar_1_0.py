# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/si/unit/power/Scalar.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.251986 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.power.Scalar
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
                 watt: _ty_.Optional[_ty_.Union[int, float, _np_.float32]] = None) -> None:
        """
        uavcan.si.unit.power.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param watt: saturated float32 watt
        """
        self._watt: float

        self.watt = watt if watt is not None else 0.0

    @property
    def watt(self) -> float:
        """
        saturated float32 watt
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._watt

    @watt.setter
    def watt(self, x: _ty_.Union[int, float, _np_.float32]) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._watt = x
        else:
            raise ValueError(f'watt: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Scalar_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.watt):
            if self.watt > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.watt < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.watt)
        else:
            _ser_.add_aligned_f32(self.watt)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.power.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Scalar_1_0._DeserializerTypeVar_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "watt"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            watt=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.power.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'watt=%s' % self.watt,
        ])
        return f'uavcan.si.unit.power.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{?YWOHUL*5MBcaf{zf07Y}k0I54x1SsV^tG~u#>M2t7n>6z}`>7-|R(vM}=ghUP+NjlMl@=y7ztlnK*#4x9-spt3A'
        '*IyQY{a$EHKL5NPGs9#=4A+86@tJ0lM<iEet&Ff7{G(H=U2dJ`AI3F@E7-k&bJ+1qq@pFppE)|rX%!g}xk}imR%cvCr#Y2WgI^&-'
        'u8mL?6b--pab{mZ?_RI*4KBd15o)a#nX}x$C%9{&ze(Vi4h5HNzQ`(J)KX%@c6XK6T9m?yA!a-{l#1Gav8<6ySR#2fum$wCuw_n-'
        'C8c5<icSCY<hneRMQ<>66ha82@fF^K-z3J;ic!sOHu{czN;*JN91DZ{n&uYa8>HoMW@8V(-AS75wB1Se_d98~ou=J`wAFgqOj>Ct'
        'Nt14C|DfGXk|u;%E-RM&;u-P*evvShgKywZ>Njo>NwV?uI_FSq7wZNAGG1$*Q_C4#`p2X%Mx2paX-foyW4}&}aysW2ket*M*Y{Oi'
        'sFKGHsf_zdb1|sm>9L2cJyG?g8?kKfOruP6T)Rw)oM=99GEA8t#mtIgBjTWtc%qPas*tD^HKS=95JEu>4%fW0;ebPtbGR&aid}@7'
        'N#yOt^?BzsW1_w7gMav1*tZk^6y4dO{Q^-n_^rE|m~ojYM1h+e@lv69!inD1TvMy`TrT%XUI>(6k@_bmlrd2a{!1!eh3K)92y%Qo'
        'iXDbjIu1Wzr?>UfWcW_%X(Q;ZxD4Tzq6$hxgN}l+9Mp)^hU!(qM>VY`PwCiYCUaTz2h_AbN7VxW00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
