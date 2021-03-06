# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/si/sample/force/Vector3.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.186478 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.force.Vector3
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
                 timestamp: _ty_.Optional[uavcan.time.SynchronizedTimestamp_1_0] = None,
                 newton:    _ty_.Optional[_ty_.Union[_np_.ndarray, _ty_.List[float]]] = None) -> None:
        """
        uavcan.si.sample.force.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param newton:    saturated float32[3] newton
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._newton:    _np_.ndarray

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if newton is None:
            self.newton = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(newton, _np_.ndarray) and newton.dtype == _np_.float32 and newton.ndim == 1 and newton.size == 3:
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._newton = newton
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                newton = _np_.array(newton, _np_.float32).flatten()
                if not newton.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'newton: invalid array length: not {newton.size} == 3')
                self._newton = newton
            assert isinstance(self._newton, _np_.ndarray)
            assert self._newton.dtype == _np_.float32
            assert self._newton.ndim == 1
            assert len(self._newton) == 3

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
    def newton(self) -> _np_.ndarray:
        """
        saturated float32[3] newton
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._newton

    @newton.setter
    def newton(self, x: _ty_.Union[_np_.ndarray, _ty_.List[float]]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._newton = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'newton: invalid array length: not {x.size} == 3')
            self._newton = x
        assert isinstance(self._newton, _np_.ndarray)
        assert self._newton.dtype == _np_.float32
        assert self._newton.ndim == 1
        assert len(self._newton) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Vector3_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.newton) == 3, 'self.newton: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.newton)
        _ser_.pad_to_alignment(8)
        assert 152 <= (_ser_.current_bit_length - _base_offset_) <= 152, \
            'Bad serialization of uavcan.si.sample.force.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Vector3_1_0._DeserializerTypeVar_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "newton"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f1_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            timestamp=_f0_,
            newton=_f1_)
        _des_.pad_to_alignment(8)
        assert 152 <= (_des_.consumed_bit_length - _base_offset_) <= 152, \
            'Bad deserialization of uavcan.si.sample.force.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'newton=%s' % _np_.array2string(self.newton, separator=',', edgeitems=10, threshold=1024, max_line_width=10240000),
        ])
        return f'uavcan.si.sample.force.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 19

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{^X7TW{RP6_#Y{ZuutLacsvK=VD2%m#f>#>$GX>DpeCqEE~QgMvImilB1o0xg;|)l(Yc?G!HE-fIta^1^g586Y^Lz'
        'c?i%S(7g90=zD-X<{WakyK>~W8j!!Ub2;bCxqLJH%kh7FKQ~hT%U(@-feu2))m%vy%1@XVa>w=KZW3#0c#+LLFe>#;s`$fR!i&#~'
        'rO%2_i^Xi*jaV1vucmC*XOW|&qggkB-8-@Jx$^<{O{~_6Y|7o`O3OGZ#7H*zft5cm=qMfeTk%<u&AQAOCB4*eUHl1Dzrd;fsv;ZT'
        'k~|Cs&dj(0Gt4#Up%|+M#dvnj`etO8I}du1FH{`KPk8VU2DAZp3o$9CYfr=pur5y9?ej14BT=#|jobx4<{w2`b|N0U7a88+>Trl='
        'T~8V}<Wa|ng0{g+pK0TE;{d$8l3lo0E5dEgCd}QzDGbeDi~B`(&IKQ%fT>_u(Lw6L(Pq2SSFz@P90f&o+zn#Cc>KSyk&%ajlPK+a'
        'T#<N(46V|{2xf?2yPPCUYaS3SBcBr;cR67SOem&$qzgYILu3T&%az8NL8W#al*USSV0uwH+__P%!T=MGX}(0HCIR1(5EGJc)nG{y'
        'N}n0XxkFHmpDKlV`diRas`(5gig=tT{&5Pqf$cjg?hdr;e)>vfqzjI5b%SWm%SC<+dUXN^l~D&q)vkoIm9EIr`V5=`oZDq#%F#;`'
        'lZfwPnBc#iFy5>D>(93~8W0k)Cj;=4`wV=1Yi5R!23h@cYvXWaVL9{S)R5KHc8l~lQ~Czk6Vewr1x*o|o<nYvjrCIJ&|dI6h1yYM'
        'FHXY%41ong(kS9S*P1CA_9_>k5QsFo?=6H4wt=^pkrr4rB2G1~D$T=mkb(-rz#1s#`x4?68K`68E2*V+s>5uCPz%y;Y~J1`i&1RI'
        ');miCDj|YcDzN7>1x1l27_Xbe>p_#E#f0_3n3Xw(L;({xrQ;9lRFN*a-+{$iurS07W4U!g-YAz>CU*EBP+blKRgIc{9-t@|43-7P'
        'K;dizi6Ia~?G(@mC$p)|IKnnD{k{|P;;NOd(YAO^yg^5>pTt7dI+KsK>Gs_Zw+pe9UH=1D@$;t3dV{=SG@eB9UgQ+ngj+gPWUthu'
        '!1og<I3%+}lrVL_tWOr!{)kpK4M+BIRKxt1m0>;`T`tfw?WG>i=7)ID^?DV*;wcuzC9x(NDG*A)!6>v74~m2Aq`M>cdEjEATp1MG'
        '*%?>IDX=e0gxpOS&_!mN0y?(|2~bU-W)6JStax#Er6Hr8Fx?Nl#-0MUSIs2#pj}<XJ86hk2E3~6rY1(Gc_f)SE6%c0tpaLv1=HXH'
        'HoI%vu{eN`|9iV?Z`4dsGu8%ld#s@MF{D_f(83Jb)9l6SNu#WPJ!G-WP-znC!iYot1PbCXtvbGJ_<<exA!J8DM?nnZF3?$E4P$kB'
        'F=zrVsyVmpxLsHitA<XvFL&fnRl{}gggeN*UI<yeURT9{sNvA&`QJr$;<wVgU;ci;`z4zlbK|7Q$cvQdUe}8uFA&u`yc=5zybHa@'
        ';Eo+!I1{cfpxFy?FFSRQ1;~UyStK6e>~<Q4K=#kiiq_wYMcU4_2iJB|X(;Ga>cKg?GQvv?1h$XDBwl1tC8(5+;=Ylbj#)g0IF{4n'
        '_V+mAXig{W_@o`5vN&zWXAmcHI&0UTK%C0y9OChup0w*vA<pLXw4FbLIG)q9R?j@**_@t3Je||?h$nM;0r5mmUqYP8=|#K$Wo!46'
        'wR73(xnk|Tf_OQnR}nAe^i{-{b4m~|=JXokOF4ZF@j^~tM?9a?HxSR|^i9P1oL;wnEg+uB>7w;-3Gq};e`fvsIpSPSZ&-gD_Pmbu'
        'yNNiR(`D=b3gTo=SM530Y&_QOdCI&V%jt$a*G(JWwmsjiD)00yi@&h=ON(z?{FTLDTl|g1cP&1)C@k(<d}{HT#V;&=Y4ID2-&*|6'
        ';tv(xnHsgi#adXbg?25xTMLhCLDa&2Ej+D-XSMJ}EqqxE-_*jlweVdn{9uI?-g3bIaBCou+c6Jm9PXECGk9GtWg~b^4c?TOU+}h7'
        'iuK^dw}pgW@xyH#I{cuVb9u<|6=q+$SF-6XxP{H3RdDGMxb#-V!c*|F%R2D>N%6(`cDAs#zP#FAU0dJSSZlXd+wIn^_R7l5<@J^J'
        '+IoAvwX$(*wY9!pT}sgO)9_$Tm@iGQpvS~};{A#w?uz?ETypk4Pq>jsGt!v*1h+mCe;nc$l9!SCh<+p({CS@iHGgRF&+UF3CnCOQ'
        '@Uvk_d<FNTxQ!P7CC-Tdimy|#c_7}|7Qf3r{y$%DS~jcim}dDM)3o0)!*`qb{Q>%PbU;4rOT$4r53dxwwxc7N8v~8R4R<Ae03E6A'
        'fpF<)8MQV<t&LGDgC+jMHI6=m(Px8E7g_r!!x&lTNAx7a0ssyG00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
