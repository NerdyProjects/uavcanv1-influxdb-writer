# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/si/sample/angular_velocity/Vector3.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.164136 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.angular_velocity.Vector3
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
class Vector3_1_0(_dsdl_.CompositeObject):
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
                 radian_per_second: _ty_.Optional[_ty_.Union[_np_.ndarray, _ty_.List[float]]] = None) -> None:
        """
        uavcan.si.sample.angular_velocity.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp:         uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param radian_per_second: saturated float32[3] radian_per_second
        """
        self._timestamp:         uavcan.time.SynchronizedTimestamp_1_0
        self._radian_per_second: _np_.ndarray

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if radian_per_second is None:
            self.radian_per_second = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(radian_per_second, _np_.ndarray) and radian_per_second.dtype == _np_.float32 and radian_per_second.ndim == 1 and radian_per_second.size == 3:
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._radian_per_second = radian_per_second
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                radian_per_second = _np_.array(radian_per_second, _np_.float32).flatten()
                if not radian_per_second.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'radian_per_second: invalid array length: not {radian_per_second.size} == 3')
                self._radian_per_second = radian_per_second
            assert isinstance(self._radian_per_second, _np_.ndarray)
            assert self._radian_per_second.dtype == _np_.float32
            assert self._radian_per_second.ndim == 1
            assert len(self._radian_per_second) == 3

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
    def radian_per_second(self) -> _np_.ndarray:
        """
        saturated float32[3] radian_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._radian_per_second

    @radian_per_second.setter
    def radian_per_second(self, x: _ty_.Union[_np_.ndarray, _ty_.List[float]]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._radian_per_second = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'radian_per_second: invalid array length: not {x.size} == 3')
            self._radian_per_second = x
        assert isinstance(self._radian_per_second, _np_.ndarray)
        assert self._radian_per_second.dtype == _np_.float32
        assert self._radian_per_second.ndim == 1
        assert len(self._radian_per_second) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Vector3_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.radian_per_second) == 3, 'self.radian_per_second: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.radian_per_second)
        _ser_.pad_to_alignment(8)
        assert 152 <= (_ser_.current_bit_length - _base_offset_) <= 152, \
            'Bad serialization of uavcan.si.sample.angular_velocity.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Vector3_1_0._DeserializerTypeVar_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "radian_per_second"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f1_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            timestamp=_f0_,
            radian_per_second=_f1_)
        _des_.pad_to_alignment(8)
        assert 152 <= (_des_.consumed_bit_length - _base_offset_) <= 152, \
            'Bad deserialization of uavcan.si.sample.angular_velocity.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'radian_per_second=%s' % _np_.array2string(self.radian_per_second, separator=',', edgeitems=10, threshold=1024, max_line_width=10240000),
        ])
        return f'uavcan.si.sample.angular_velocity.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 19

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{^X7TW=h<6_#Yny4kX2*^Xm737w{v)Ou&7l~!J-O<Px~nt-uv_>vec+6iZdS`waHNsgoq8lZV-VF3eVfJ_1Zg#3g&'
        '7HuB_^anKWeF^#t^4N1`IlC)IeyaibJHyL4AJ2{4Kb`#RrTMYyU;akg3v>`VuI5UzP=3O^kUOrQL}{X>;bng2p;4J{GQ}VDQeJ*h'
        'u6$O0S}y04Zp<Q>U&+{>&tgYQN3$q}-7M~AAye)i4-;RSp7SC1O`_Jzd>Y1-mPuTSv3%-7D}PbaaXR*w^0P9ZbD1$pdYR$6{2f?%'
        '3BSRrGN0U*JPd}sX5D}p<{Bg`Ci;V7GQVzV8X0ltVK4TDN@Dp54<5mQHo&|TQ(~rOB2I&Kan5dEd>M~a$w(Tx2Rs%Z$69t{9=snL'
        '-sS43x8__=8aL!|*NBpKfThp0aib&vme=x2_iIJC&DnyvyEuie`E&W8%rCgWF%FmtMim`q9vp2hlD<kb_mem%^OJ6n_~n!TPK=E`'
        '5}d?Y<Z(rkT{5yt6C;=*g6(mVGOc+)w2XaDbP{pG6qry<^+*Jtu^}>s_0>w_%%V~|4oVXxyD+^h9q!z$R-uE5$24CdQj>u1O7ICu'
        'xoWU94W-Wv#M~jM#?O>OJ%cT1Dbsuw0!2Jd6#qj8v4QQoDv5^L^&oteG7<qXu5J>|d9}z-K(9{Wpfc{lsM?cowu*|Ztk1$JfZQGn'
        'Gmb1xLSnv$Zi4@I!(_kDZ!q89Y=BG1z6^jT_Ze_}dv=zP25J4iy?NBLu$*~GW=N~mX_FpjO5Y^=Liz%ypgv-#2y%yPZd5u)_5$w='
        'az~N<BntyD1QrO%;+XqfYo=t_>r;S4AkydoTW}j}1GX5EHdr+x$uzF2%)@k$feOOF8Yt!m68se#$YbIwsik)MhuI1t7o^|Vy0b%;'
        '<HV5dcUK5xLJYoCV9#d?k|ImdU$=<YgCa$XDeHv^t6~g+f~Me9#2?k6A`#N>!eT907-EDm-MS%fRLlD&cKOgz5r=_(j+#LnASsp%'
        'rUm*y;cN_nA>c&qlu!us`Sey2W0{yi-HAo<x|Ocej(AhNMaQt7#8SU>rXKImoqHeclwu{n@f)s^7fo0B2601gJdKn6*eUZ<Zbhif'
        'U#pt}KS&|ru$dic3DXa%{A6LxN3`=9II@qU8s@jH4D<Q;YKhFWmw7y29O;9u*Xy@hJjJrOBGyGCgN71tFbd_wgYqz+cX#Ch4_pkC'
        'D}!<;UvPDjDWAhc$la7dyU0ybK;<?e0IIp0C=UIq+3$;cYYiFihS@>jHTD%We$`Af56ab59J@JK8TM6eH#N~a&10LXv*xTi{Z-H!'
        'UBNU^z+!i8IhKdu@_+60%NsQl)Qq_S)t)G*eRL^iDU>jS@-+L2dfKS+UyoR<B2<}#yfETOJ%NHG%=#5y75vZ+d<fYUP*LE+B!YGp'
        'Si_i|UILn+7u7wts<=H^lc<JHxi5F+NLIsj@RU2)dA$&#dZW&YVWWman-{;!{PZuS`JnoK$OkE#pKz13%*o4?=w9R{5Et<3T^=R2'
        '1>S?&V{pd~FPu}ZFQC{<aX&wMp9R<nzqd#{#@U@Lgxk9J;;d+YUM|y4p*^^^)4qn1PG=sRGm<f0Vj!>s6sGVZgDgR%bR74M6?DSl'
        '3B-wlp0wYSh~ou4Wyh!N__W0tJ3fnes-Sar{b|JMf}TM<S<rdA{w(5LLC@Lw1;ojMp0|1y5ziO&0^+%XUPPQP=q1F{1$_l^wxE~o'
        '{#UKtE7s0ctLK`v_Zs5Wg1(M;rJ!#hzFJU%c)6h05nn0jn~0YR`UAv^1$_(gLP39sxLD8|me&&ELP3`;zZJx@1^tob`D4U01-)tc'
        'HtcyF%e#p<Q_xk*e+_Y}pe=ijb?c7}d!8z;Cknc0&vncCw`0$DyB~M@w#A=V{HeuvEdI>m&n^DK;(HdKSQHiyEIzaN+~SuOzq0tX'
        '#cwQrYw^22-klz|!sS|6u7yr5yjKfPYC+V(K`lJ1h3B>KWi5PF3t!j5H?{C>EqrH%4Bm3k|KZlaMsCMEY~ygh%$VWpawQ+bYijtW'
        'y!w*2tx~K9FTQPT=>7h12ZxS6D9^Y&<oF7+FWqbT%r@M@=Ey3z^axyfEwS_rSVpW1@1G1`obTjI>l>@BPHTN*b924ZZgo2C+nu$w'
        'TdNyuo%M~*Mtg1ZcB{Ry(Z7_S=x5-;nlgOOm-K{qUwqJS68FS|kzR8C0Z+M+$9JR&_bG0DEPgxEUr14T>SOw`VDRUCTGstTi@)s*'
        '{J5Z4AX)5!QrA9o#fta`T$SPu8vnak5dRVX%*58Acy~wqD*xmE`KHsd+5dIZeDT*!)Bd^{z464a50T#SZu)2-jk@k4yj}1zkB{x='
        '=zeVHaD(E{qGPo^6fPaFeAxkCcF>oV3&p>=#?j|6`g}O*VlV&RF#6m1A5Lrk;2{nG00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)