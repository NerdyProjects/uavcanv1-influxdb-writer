# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/time/SynchronizedTimestamp.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.012152 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.time.SynchronizedTimestamp
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class SynchronizedTimestamp_1_0(_dsdl_.CompositeObject):
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
    UNKNOWN: int = 0

    def __init__(self,
                 microsecond: _ty_.Optional[_ty_.Union[int, _np_.uint64]] = None) -> None:
        """
        uavcan.time.SynchronizedTimestamp.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param microsecond: truncated uint56 microsecond
        """
        self._microsecond: int

        self.microsecond = microsecond if microsecond is not None else 0

    @property
    def microsecond(self) -> int:
        """
        truncated uint56 microsecond
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._microsecond

    @microsecond.setter
    def microsecond(self, x: _ty_.Union[int, _np_.uint64]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 72057594037927935:
            self._microsecond = x
        else:
            raise ValueError(f'microsecond: value {x} is not in [0, 72057594037927935]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: SynchronizedTimestamp_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(self.microsecond, 56)
        _ser_.pad_to_alignment(8)
        assert 56 <= (_ser_.current_bit_length - _base_offset_) <= 56, \
            'Bad serialization of uavcan.time.SynchronizedTimestamp.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: SynchronizedTimestamp_1_0._DeserializerTypeVar_) -> SynchronizedTimestamp_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "microsecond"
        _f0_ = _des_.fetch_aligned_unsigned(56)
        self = SynchronizedTimestamp_1_0(
            microsecond=_f0_)
        _des_.pad_to_alignment(8)
        assert 56 <= (_des_.consumed_bit_length - _base_offset_) <= 56, \
            'Bad deserialization of uavcan.time.SynchronizedTimestamp.1.0'
        assert isinstance(self, SynchronizedTimestamp_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'microsecond=%s' % self.microsecond,
        ])
        return f'uavcan.time.SynchronizedTimestamp.1.0({_o_0_})'

    _EXTENT_BYTES_ = 7

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{?YYTZ<e;7@cS?>#RmX!h)it@?hM>Oi!}7aq%s#EXuf(klm;V+EjOcGgYL!s;$e+PCzgZ3V{ZNl)uV<;;-;j&uurF'
        'c^JC;`|7)%bL!WNe{F4a+Fx_Co)xwzlhl%typ+#)R#KAYx~jF6jzaU!u`@n*-q6XcrtmWCJP*Hw?dDRdcm?|{&nG!oiIWv2$1{}+'
        'qm_I{#R)!G$E!Lt8|j3Mm0AVSX|8;`czziM7Y3c*!}HK=rrbFrGw;ZT9})dEb*;QYbLmi0S*+{nrUiFAb+O3T9j}e7q>~ePTz{gh'
        '94jimR*uGG&NsK2X40i4sj(Abu#ez5w=S)8K|$PTwjM15#be0<Y)8=)JNhj=4$X}eovVVI;%uN7J`<Ok%}VA*TgtU6LUS=KbRNF{'
        '=Z#M1L=aQH%E&N1VrRT8bAmf2_=H%^t)+rlsd8dgSH!qM3d7BeRd`j7Nd^Db(<R*)bnzWQwUJ|(w`D@foz^R^jb+@@4wIG@G?JJJ'
        'tI70uU6(TF4y#I743m3fVw}~Hn8{n}V*M;5X6R>+jpO*p=xQC^u0YWSV-*S`bB9@?)+yJBYil$r)fivRM54F06xn9)q6-u^;iaco'
        'rPEB&B#sGxqf$@j^{woC_j?!#o5})pQqEE1=iM%2J+}MP-u?5Fg*(r*cWifee~-<G8+(UMh0H}X)!3YyCF}va|7jcZ%vsd!fgQu9'
        '+Lr|qAp>JxDay%OZe%%|mjECz>Flanj19+7ZQRHnvO1x?jb3efm<x{(j3XNY)2YO~lmm`gZlskqnKyG#0t+(l9XuGaZKWMM{Bnl@'
        '2@10`$d_{iQ208|>ob<kz^$0E=Ce}scE?y0IGnVFpDb6!s#yLQ&Q|cUj2n({8<*5;-RCJrv>sGN_%O$)TkQd$_}E2Q#2J`qRagwe'
        '5N#4bgsaWQfmV?wZpAxsU2H9$-W%+T_r(W;PUMrgIj7E*C&R(;;djFzZZ)@mAfsPR-Qo><i_>_j^i(CGxtz8Ih33PhD9~vQz(ox@'
        'CkY#mTYU0zS&!&7Z=vNpezmY4E}mg;F5C^VGMo8~n(JreE6rweWsF@gaZP+8KJpNhf{+w+q9VL#uBIb-N<|tMmC7Ovn`^1n-sA*B'
        'Noma?7me!+Ft?8dnEpr`f?oCKYCE~tlWJ7@(<19l4RqS{YoCFxsiCniW0tiX+Qp%MoKF9LB|5p6+)d_Qkj7MSixMK)(*+&F3yl2l'
        ';hf$vGK-NTHo$gm!2LMVh*D6PgPv}x&C_0se|silyP-BEaN)!`J|TcE{haYF;n#WaBIH<rQJA5wAZNuQaYSdP5eZtf)ZCVF6ZmM;'
        'vo+;%B+sB4*TGXtqVi@Xwt9PsinUOqY4_@TXx{!px^LR|V_HGBc{A0x;MnVe*jbfn>;+RjqDn6$@FBRzoi^(W=W?10kUfa6ns*=Z'
        'A}Zm3oWxPI4t-fd>|eEt-XCFmu>YscaNE}N2w||{GxS+W6)!P7@YDEkC0=AeNvyvc*#HhjSPy*`@tph%N95)+AqW5f'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
