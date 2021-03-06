# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/si/sample/electric_charge/Scalar.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.149681 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.electric_charge.Scalar
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_
import uavcan.time


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
                 timestamp: _ty_.Optional[uavcan.time.SynchronizedTimestamp_1_0] = None,
                 coulomb:   _ty_.Optional[_ty_.Union[int, float, _np_.float32]] = None) -> None:
        """
        uavcan.si.sample.electric_charge.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param coulomb:   saturated float32 coulomb
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._coulomb:   float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.coulomb = coulomb if coulomb is not None else 0.0

    @property
    def timestamp(self) -> uavcan.time.SynchronizedTimestamp_1_0:
        """
        uavcan.time.SynchronizedTimestamp.1.0 timestamp
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, x: uavcan.time.SynchronizedTimestamp_1_0) -> None:
        if isinstance(x, uavcan.time.SynchronizedTimestamp_1_0):
            self._timestamp = x
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 got {type(x).__name__}')

    @property
    def coulomb(self) -> float:
        """
        saturated float32 coulomb
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._coulomb

    @coulomb.setter
    def coulomb(self, x: _ty_.Union[int, float, _np_.float32]) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._coulomb = x
        else:
            raise ValueError(f'coulomb: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Scalar_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.coulomb):
            if self.coulomb > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.coulomb < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.coulomb)
        else:
            _ser_.add_aligned_f32(self.coulomb)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.electric_charge.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Scalar_1_0._DeserializerTypeVar_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "coulomb"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            coulomb=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.electric_charge.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'coulomb=%s' % self.coulomb,
        ])
        return f'uavcan.si.sample.electric_charge.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{^X7S#KQ25hf*3ymXq9EX!BRaYQoF&hpr$R!*Emp{>|xYbEHgi3G`{XQp?%p*c3)Jxi{D0P#Zt5f~r?cmnt*_$T-='
        'Nb+DHK%V^*4F3W@rfQ~VcPUG67C?P9-PKjqb@u+{#6P;HXUc!sn}boHgV1p`SCWPD3G+hkxPB515-klcveOTYN_~?m{%|zl#b?F('
        'r^TO(wQSCfSp@s5DI5AMcC>Ufiw1C-huk+x`mQgS>T~CT&qAh(Y{4CJrDYNqVkVpa*wUXBbe7Kit@yOamR)AxpqCo1i{FEe7g#su'
        'DzdrTl83>>swFpIhPeh!700SYF_&GnMj9D`J)_tcDv9M29z28vZNTnA%!|d^5^)N&i*xq)%8Tq6C>cp3hhWFbqgcy+%!3bO!~0wv'
        '_0_WLN#lk*?i*3i4p`|kZQLjcz{=OMOZRF)c+A;_y*s#tuK8<mzsN4QU}GFG6-)~{Og*^TawL6~XznL*P-G|EAn}X6Z;#E)JQSS7'
        'Y2<N5k{+4j(!>a6h+sob225)n5G`Y$6P-kyFa;_UQzH_=XKaX!fxqN5&Jqf>>mW2yvJcy9(&5hak_#P7Jf`_Nk(va&C&4FVz*U0{'
        '2BGwsftWi4#rUaGC}(^GHKm#_L7<4oiQ<1sAvSQlr;=zQU5~?83L_C1#?^JAIWL*~1mx-gTvWz=SXDy_cPmYirS>Jb1sFGEVam};'
        'laQDX(M|AQFHH6;`^Nk2od&ps?8^Y`<URu%-&tBBq(Qd+(B3)fSzu>gk{YtL)oGIvXG&iu`$GBxx1c&=Gjhl+vePPMPMrn2Q^*}f'
        '_LDRWKoMvlB#mS4bFG<@;ixhJ5`jpg$JT<|;22no5ov=~Ba&1jSE(MhgA_y%2HHR{Kak+B*gzf=Ur8;sQ(a~^gj|q*WA|2<ti_2T'
        'x8GYQkO?vPQh`37DM*TRfd0Bcyb%;BY8<dpn6NU&5GZH~PHFhVI#eV=^ZUT81q(xrFs55S<c*TOQqkiRM@1YKsvI@rI6zXY8cYlH'
        'fx_Jw0z<%w+9{wA&SVR_NsMJ;#&suF#2c2nN;~2$@iv{odJ?Nu>C8Xs((c_)x`kNJuKkv)<XP2azCqm38;|2;KX!`jq+1$PWUtpv'
        'fgcPY;joz<X$cGW%lu?vZI5VYi*RKhS2gV4wlwT#vl|6kroGhT*~(NObiGm4Xz><n;)>W7jT9P6z(FaL6Ay~R?2Ox!2Rv{wP_7J$'
        'Zg$?)NveDf8zFZG4BACzngS}f2?0>eUZObkt7g>~hno!<_rmlb@EZFH+P-QIQV+`2RlJ{usAbYuwLR2C?=+v=Or1?<!>PESHM)Xn'
        'Fae9*wdGhGg3JHgt;!oE6O@d(0o9%;sC{%PW+{{~gYq={iF({9^IuPCEF)B^guF1~NIijoBuuM{FAIL62R?-C3#cgYVG=<*3#?+y'
        'PA>sT(2MGxTUOi<coNmn1MbV7oXTn#2amafo!1K?s@LkQm^5m*w0ZWs$WHxQnvcrw2Yj5e*>N`+6d8Gu5Iu^#1mXf-y~Cr#w!phk'
        'd(0$iGH_19?1f@4#J%k7Jr-am{2r5dguC4|gyB4Tc2~6jUaZkhu00srgGxd{7g7)I8Oa!j7!d3LiFq7kkR>RT&f>Y5oF21y9PwCA'
        'PuTA{#MzvlwCnSBeZk_QU0*^xnbT#<e+qFSr>7B5<n)Z?Ka04W({pzJJmOqVU$Sym5MRpa1;leXy@+@wr<V{<<@9C5rJP>2=U=gU'
        'uUI{=S~;&-eXk?Fn$tHBujKSi#8+}k5HIKSD&osIeGBnYPJe`WF{f`MUdZW>5m$10&Dyn!cs{3V*1mPbvpM~VwezQlr*nGU+S{=A'
        'b*$Y@#KoL$So=2-=X1Jc@3C$D(X#g`<9a-&JN8~TtbaT9emASQ(|0WX%;L{2zH9Lp7Jq5+R~A38xMxvVJh1rG;^!8>u=u6LuPlCT'
        '@f(ZZRd{D%))JR%Vyz}RHSs}B?A3&*iG!MWS`(kw#1}R3Wlell6JOWFH#PB{B~p0HLH~!TfsNd*dDzBbzAT!_>vBDt!7(*{Q^K=v'
        '@iq)jbL6E6bBe&6+7hczL2$(S@MKBxk@#-5y4~8?>TGSdc6PQq?X6CyeY3N<d1Irs+1YM&TJ6o9n_KNxtC}O#c!L*3m_!~Z7ypL2'
        'B5t9Ee~I(rf8sx>*gX{Qb;bMHlOK32XxXfO2sEGhA<(RT2uu$L@tZ?5PJAdns@l$7aev&MJ{eQ@r#jX}81p#y;^(%$Y_aNmFl_J_'
        '#B-%R5H6hs5B(9|1PuN>(EHCWEc|Y&^$}=&TqDySFzrp4T<n71TgHex{|DEio`YEp000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
