# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/primitive/array/Real32.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:22.655647 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.array.Real32
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Real32_1_0(_dsdl_.CompositeObject):
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
                 value: _ty_.Optional[_ty_.Union[_np_.ndarray, _ty_.List[float]]] = None) -> None:
        """
        uavcan.primitive.array.Real32.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated float32[<=64] value
        """
        self._value: _np_.ndarray

        if value is None:
            self.value = _np_.array([], _np_.float32)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.float32 and value.ndim == 1 and value.size <= 64:
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.float32).flatten()
                if not value.size <= 64:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} <= 64')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.float32
            assert self._value.ndim == 1
            assert len(self._value) <= 64

    @property
    def value(self) -> _np_.ndarray:
        """
        saturated float32[<=64] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _ty_.Union[_np_.ndarray, _ty_.List[float]]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size <= 64:
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size <= 64:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} <= 64')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.float32
        assert self._value.ndim == 1
        assert len(self._value) <= 64

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Real32_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.value) <= 64, 'self.value: saturated float32[<=64]'
        _ser_.add_aligned_u8(len(self.value))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 2056, \
            'Bad serialization of uavcan.primitive.array.Real32.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Real32_1_0._DeserializerTypeVar_) -> Real32_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 64:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 64')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, _len0_)
        assert len(_f0_) <= 64, 'saturated float32[<=64]'
        self = Real32_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 2056, \
            'Bad deserialization of uavcan.primitive.array.Real32.1.0'
        assert isinstance(self, Real32_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=1024, max_line_width=10240000),
        ])
        return f'uavcan.primitive.array.Real32.1.0({_o_0_})'

    _EXTENT_BYTES_ = 257

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8W}=N@0{`t<TW{M|5|(&RoV#;rlcr|VT$Co3EL*mfOH;MQ1`ei^7U^!$?xLV6@z^9vQ35Zny+8r?VHYYuU<vf>TOR!ApW#RU'
        '4EN1HV~3(_M|GUUiS3|U>qUoW=KJP5a}FtvW>Na@qoG{)6A!f)tiW=MM!<Z>be(^ib(a;5MyuIw1y0C#eEjRsj~Zd*v%fC18UK~v'
        '{F(p63$bi?W|QofBXh1{dd0TyG@a0yV@1>V&4uC<X1ZgeJl2dk<_Av8<904qzv+#C<&cNmzxmHR9x%)>^qqPXvVecjcapT}#AErP'
        '!(3}i%2C5IL(>RTeetCo;HfAcU--tPS(^ERd9$JYX*%1#uHy!CS(ABTk8cM#o6F_#k%w-}4EtFIjJgvVZZ`-Aog_BQAT*jSi*fs6'
        'eEzEqcnT|iPBu(Ul$PAT_!AzVHG<IeEYr81CF&4Q)1393FtXCXGrrjfDV+hO`C)HN9Py2@%E)MSbgVKlF;*QPtyahHRLkYbkxIEb'
        'R;gCT%M*7-$19Z)p2mvm@exwjHXBa3z@ZkO>4h_9(llpjAkBk+^8#nqW7Z=tWV6igTd+L@nyuScAfHm&*E+;18FiPGUEfIH)<P(k'
        ';qR|`eC#tP%(mrgy6iE>qS0#eSl@{xSZLN;uG8T0AhKqQwkJ)(mu=>oVawmz5XETN4jmf%ethopme(*t<~`RnO-AbJGmlPVf&5QC'
        'j$GID7q)pS#+>O!jQ@uhKudzU{h*hOPYHG5iRsO<C#=mvXD3NN&~DCC$_enOJ86HBa_Pj?&0o{;=s=_ca>JY!tLX`fTr<T(KK0Ed'
        'AoRY)?l;|6LIP56PTrgY5u^l^>{>|2YM%{cP!iC3xFg$apwb%Q=q8?K=z8F}esBbiCU7jXX=$wEJNm%@982ItA1}?)+{qVW;5eK}'
        ';8aiV>6iM#NjR0jnQd{%Li2;Kgoo2`CV{h=uSE7^DfZkeV_^`^CUE|_8pukv3%lZib8tR^cQ*1&THf6?9xlK;30&M!6M2yR(rfX;'
        'yKpgq_xkchR^q$-+I(;c-b>*97wRQ1@)>%g7;qWhPeAXTuMggs3x?>vhASD5{vzdR+z<C89(({-61ch%^O+q;^K)&_V!(%RHG%6d'
        '-4jCS<W0Ue_B1wJgX;+tHr7dZLVCt-?s*Kj0fhuUdgXNzg8Xmoiw?L6A0=>mYj3X-XW`lX9p1ONa0_lHP~24>2t}CEzG{MDC?+tH'
        '#W<DTZ{>ZD2PGIuV072HASB_&4n!Z6VKjlt_Oo)ExJNe5%lLt5fib8gF!5SBBQ#+r4^%6R!$bnrt>;Ujn>TvK+&OR^FbUNJ?!I>J'
        'h=K6;-imIx19ua+zw<e)P>gDN7C(M#`rsbiPvF5D<(F89<CC|#2KX2rBv9++I*F)sWb<v)>z3cy>>}p!xR}SBfQtg=L|haxC*h)m'
        '(=x8fIIZBCg3~IASVBFIOL^1<ToO<haY;m7!X*iF<f`JLj5!4t70l6Cg&M42EsraCtO>XxU`@mo5o;2zNT`#mhD$Q)3N9(AtGJ}X'
        'G_2ut9@p|XE#R7f(;}{kI4$9tgf$sgWUMK;qF_zM6*Y<KjH<0~spR|)HO>C}AEp}8()Zwfu7<S3YN-1Lm^-Y7_N5xq_P83-U-q2c'
        'hiXXg-+}+zYDmxi7x+_EL+P5Yc6ax%8rrCaG(r^)tD$YxQ2$vutcG@54Q0=l0@+R-Rzq)44Q0Paht<$QR6~^GB(k5<5DO|UlL*xE'
        '*vUf&H32&UY9e+-)FkXkxGLe4jH@!P=W$9wTfkKX*9DwX(H3!4B?Ze^$m4Pz3j!_+SP*ep#Dav&650~3OE3kiIF-j$A|NzD2`A!|'
        'gc`9@C>b>cI|^zlc2r!aAjC~38Ep!sQh@_DtfNg4WL%c9py0AXB~aQUvgKILdQh=sSgi(+b3Ce>@!&H(RinO;wQ7Ij_L_Y<hzAUd'
        'wSAVhz%2ete8QM<=9y)*TYhLb7JnR{HiA~<Hy9aQX0*-F=5f1Zx0<XJ1<Wtaw0!2wdZn!MJ69fdycsu|x9Y<``c6m=?WpcL4Z~-%'
        'k()-@>dyu}P-(M&TIzOYOIf?PST2qfGY?LSu+4zN`)M<l;?6k@#(%MYizogvZ#F`ALHE;j1Y}NovbvM?C4;;AKZeT_larI9<%!$+'
        't&QRL+#a{9S)1)%U#srqSEgk--t4v(9a%q#HImRZbI_vxs?&b@INOKf{{V;Lt3*^E000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
