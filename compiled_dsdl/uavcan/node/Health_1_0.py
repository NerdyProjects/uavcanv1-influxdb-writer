# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/node/Health.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:22.899159 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.node.Health
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Health_1_0(_dsdl_.CompositeObject):
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
    NOMINAL:  int = 0
    ADVISORY: int = 1
    CAUTION:  int = 2
    WARNING:  int = 3

    def __init__(self,
                 value: _ty_.Optional[_ty_.Union[int, _np_.uint8]] = None) -> None:
        """
        uavcan.node.Health.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint2 value
        """
        self._value: int

        self.value = value if value is not None else 0

    @property
    def value(self) -> int:
        """
        saturated uint2 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _ty_.Union[int, _np_.uint8]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 3:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 3]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Health_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(max(min(self.value, 3), 0), 2)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
            'Bad serialization of uavcan.node.Health.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Health_1_0._DeserializerTypeVar_) -> Health_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_unsigned(2)
        self = Health_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
            'Bad deserialization of uavcan.node.Health.1.0'
        assert isinstance(self, Health_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.node.Health.1.0({_o_0_})'

    _EXTENT_BYTES_ = 1

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8W}=N@0{@j&ZEssO6i&;!W*H2PPLn`_c@m&jqxUu~FVgsw6&0ei>1ez0A|cE7+BY`%+E;!_8YCq40i;P+0%_(q@HaWmOPh8S'
        'v`CSh*gofZo^#IQU$6ajquH2z>U-6gS}GH4nGr;apGhWJf^%I~+6u=){l>8~K6l=*lX1nui?H!5{1Vpd6|6`J`)_$N%!x{rrY!l2'
        '5$SlSn|R2K6<P(}s8^rP)-OVDsn_^DJPY+rOq??!^N!i@1BAN*$l0k-uj~mX={bNFro<8KBC4ydS4Nb=i6NX=d!nouC`P-=u>ms|'
        '+1$jLa9A=m0QkLS2%Zz`a0#RWzf<3RJP#DFCA+Y95VwF)<F{}W>O0svq9`$RG0=0L@s)aINTde@*D%$2s2c(Py;V1NwTgG#83?|{'
        '@6J|l_m=rP{5^he8ez46c+l;4_5;6PZ=G<4CiPKFIV3D9yviNuE7Sm0Mpw+pF<Mu;6pF}=B-GdO48gl|mDp)zn2klbpi%RP#6U#O'
        'G4TiWjlz&gcnkY`vo-A3OIsmQw;4cu|Nj^?J6}BQ9v>ck7b*PRLAimHIgzL$2HMCmgGP~#_V6u`A!@*oHppEd%T%sCl+Q4V2m*d^'
        'q98&-bHYjD5Y@~gr5)(NhH#@5?^~bQv30COh0!GfeF|;Ls1{M<m`yl~40P_M6D2#7(<VTlCo>)RPQBEA1;VSlohK*V!+zvDJozsc'
        '<i`aT&_l7L3mAohLzE2+p>RGnWYh(8vLY_0=qa1_Hj=TH<lo_MzY6?sI!FC(|H}yf`-||cFNzuV0tQe513A}hj^C>|f5_=MlL<-z'
        'q*Y`wKmHQLoim86UR$sToQ<b;6QLr0n{V(B_~-mHzQ-T&ula$80j3O!o)gDtcwXPag*astSK2r%Xz16svDMz>3^pXg6^S;*Qm#vu'
        'dN7R?P%_Xko!Z&3y(v^7{VB~hN6@Qqpz@g%IW}zIWz2GJKX!I0jUJdzJuqn}Tgmiq@E**Gg`5WTiw-puISbGE{cpumqtVH%i(|DQ'
        'F`tA0y`prJY9^>#Ookz*n2Tyr>7^4DC>_Ug2qOjUzYZQSgx*-#Rm_dF`3cQZ+l`M}u^zKD;6lz@WV!Z|!XOlq0h-C=On3A&HH5Hk'
        'b8&p8Nu$|ZOt6u(_Oz6GWFNK=;?7m}VVaIcqePNXl53-wlnJ9g%?pz{cIwjh$LaP?(%#wLzI3A?BpK*o3f}2U5NBUxhL~|$GAc;g'
        'p+jM{8RK1Ha;S?*JG*%MlS!b>c2dy-Fil(Y)9ApN1RMKsZiDAm4OMZMe~0?@N5bt-ejl?lpRQlSx(YSADu^AInTAe*vLCQg!&4N~'
        'AA)YgX><PMT*o;V@SyQQ{pMprDJc5VAui)?-%DUNzP!sH{1MiB%YWJo-rH&#A@rI)1D;SHSjGi8jf>Uzlz~1Ge=FKQQIjXR58epV'
        'miz-SO|DlI2mk;'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
