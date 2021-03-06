# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/si/sample/angular_velocity/Scalar.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.161871 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.angular_velocity.Scalar
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
                 timestamp:         _ty_.Optional[uavcan.time.SynchronizedTimestamp_1_0] = None,
                 radian_per_second: _ty_.Optional[_ty_.Union[int, float, _np_.float32]] = None) -> None:
        """
        uavcan.si.sample.angular_velocity.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp:         uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param radian_per_second: saturated float32 radian_per_second
        """
        self._timestamp:         uavcan.time.SynchronizedTimestamp_1_0
        self._radian_per_second: float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.radian_per_second = radian_per_second if radian_per_second is not None else 0.0

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
    def radian_per_second(self) -> float:
        """
        saturated float32 radian_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._radian_per_second

    @radian_per_second.setter
    def radian_per_second(self, x: _ty_.Union[int, float, _np_.float32]) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._radian_per_second = x
        else:
            raise ValueError(f'radian_per_second: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Scalar_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.radian_per_second):
            if self.radian_per_second > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.radian_per_second < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.radian_per_second)
        else:
            _ser_.add_aligned_f32(self.radian_per_second)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.angular_velocity.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Scalar_1_0._DeserializerTypeVar_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "radian_per_second"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            radian_per_second=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.angular_velocity.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'radian_per_second=%s' % self.radian_per_second,
        ])
        return f'uavcan.si.sample.angular_velocity.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{^X7TW=h<6_#wvy7{Kab{ywMr>P~i-dWvNUZ+i3SE-wT@!GKLMo7_4IWycP;klLMth5ONG!G3dV1N#gDUhF#pOD9*'
        '?L&Y9ea=q^`U~>db7nXz$+6#RK>p5<hvyugEBDW*{`S$?iRxeedO8Yp5IU~rO0rOX%)F30uAf9{qNU+wes;&G%r}|h4@W64zbIEe'
        'D?crl^C>rG5$rE#Z0NJt(bCZ@O5rq%2U*CJJLF;FOEYqId<NfTJ_Aci%OozvL_YmnOMg+)NjmX)`B|CIyUZ9Rz07c3{vMP($GkCD'
        'nNQu3JPZ!ansWnYm}}5haiU%nQ~5P(rI8VLc1E!;R1(XNdGHVxv;o6QF)d~rOT-z_E-u*Pi_fzoRWg!B4#AGaN3oWJm<R92h7Y(p'
        '?yPy&lg15sJTRi9U9i$;+PF~?fR(T0m+v=%@R+j=dv|dQUGtanL7884!NxdXDmW_WAoJjA^O5vbqPd^ML7AU&gTya)|9fI$;-TOq'
        '&LWR1lJv<DE=`PJh6py~BxPFjfM^-}oaiLtgeg#=m>Q7?K4U{<4Ez<Rapq8{T?e6wk^|UYmJWArR9xs_;xWxvh}0zDeF;7xDOW9)'
        'rlItiftWi4#rT<0C}(^GHD#L5L7<4oiQ<3CAU1Hkuaf9cx*mtG5=J60jH??&b6zp|3CPtcTvWybSXDy_cdJa1mG(Kf1sFGEVaCx)'
        'laQDX(M|AQKTP&&`^Nj7trob1?8yM^<URu%-<q2vq(#>M(AhffSzu>gk{PnT-tCYPXG-57dqVmGx1c;?C<t<!Y;9IDkDLX&Gsqo9'
        '_L3|NKoMvlB#UG2bFG<@;ixtN5`jpg$JT<|;22no5$S+dBa%!bSEU}dgA7Cv2HHR{-<RO8*gzf=Ur8;sQ(tB~gj|q*Yx{POEXRo<'
        'civqgkO?vPQh`37DM*SeMStBS-Ux~mHKuG7Caj7v1PXeBQyKoS2^ERZ`~fg)!NL$DjOjKAd8=ZtRrL9xqaqFqb&i^G93Ux{45kJ8'
        'K;do-fg#{T?UYam=kl5DB*ro^<GK@z;x$WMqh0Zac#}?GJ&C2dbfzEmXz$*Ky;7{?*FWMad0KUqZxA>1#^X5Ii=8q*?N$br`KwJ+'
        ';QJ{g95%CKEn((Cm7gqZ>=B)O7Ow2$s)qeLmWKU&a<xRuw3m52Up&$WU2jx(TD--wxGFY8D}#m-a8L^6#Dnr6Kj-%4J`Y?Blq-X>'
        'moK<F$&}AwBjj$%pk3sqEueDS5CGNgCyGPAYS(>nxYm+!Kg{+6ueGP3@2hs2c~Gvd;@HeV%VA&D_D~zW(|%?%b=I6!r{;pz=nAI6'
        '1T1#fmScGUF8_D0E^m}fP%`EQRC}VJ_R*!7rBK2Q%G2y6>T#>ee|<z_6`@Kc<b@H(>InoSVOCdsRq%&;;6uoPfQkYiCK0r=z$(V<'
        '^b(K+y{PHARmBZ~Cs8e(a$ol4k*tPs@R&Q;dA$&#dcDbt!$u94Hcx+-`I%oy^Fj5!!^bI`pLCP7%*peF=uzY)5Et<3T^=R21>S?&'
        'V<u6D1Lw5s3n=zd+|SS7X90G?A25kWxZBG@7|x@ocSYx~<udIS+Jmv3))GoOlX-B@NX9tCfMEMbOyeMfEJ2}k63<N(^n}Heh$jkq'
        '%6?BFP8RgEU7xn=GZts<`W)ivg3eq1Gl(+<J&Sm%pyw?AdBpjGUa<QMh*Jf9!OB@ge4(Hh5ib<<65_dnUPe4q&=(Qs3VOw!f63~-'
        'YW2Kq<-B6`y^8p9L0?0>TF}=KUn(d;yi(9>h%XlO4aCa@{So4&g1(7(v7kRjTrB8yYu6IuLP3|UeJhCP3;Gjl=T8yO7W9U-w`K3^'
        'Si9SZvjttX_OBsM7j)g;W5fDm)840w>&b#{*?Zlz{_WcP-KyhG-?I2Ki$Aycw#9cW{=(ufExu=Q*P^hvZ}Ex6FD-s$@oS6USp3%F'
        'cNV{|@$Sr|C9X8Yazk_*;=P90Z3xj2`wj7=A--&guNva(hWMr-zHNx_8sd9PWbl@Q{tr_F8@XNcu#LlfnKg&6%awcr$JF>u3D3US'
        'J1{uSv6mvuDFSn9T`WBT!4Vt4lO@AP;@kPs#^&mJcYR}XYipz1S?_i`x4LU<H&-{;x*MC_&Cc4^t@Y04W<5tL^$UsxlEp5Rwrk&q'
        'VnzHDCXBd^y8a;+#DB!UGO>Li-tCEB=b!wa2ZWaG`Zq!Q>E8tH`ZvMRIU#;?fYyok#Rqi<x+flt8`Xzn>cNrbbqOXuj==btT`-@m'
        'n;^^`{4w!NX*<HDli;jB!t;Q^p9gyX-h+kT9qEDux**rcv<pnThfFRu#2+kU@SXnwPb{yRWeorT'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
