# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/primitive/Unstructured.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:22.625779 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.Unstructured
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Unstructured_1_0(_dsdl_.CompositeObject):
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
                 value: _ty_.Optional[_ty_.Union[_np_.ndarray, _ty_.List[int], bytes, bytearray, str]] = None) -> None:
        """
        uavcan.primitive.Unstructured.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint8[<=256] value
        """
        self._value: _np_.ndarray

        if value is None:
            self.value = _np_.array([], _np_.uint8)
        else:
            value = value.encode() if isinstance(value, str) else value  # Implicit string encoding
            if isinstance(value, (bytes, bytearray)) and len(value) <= 256:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._value = _np_.frombuffer(value, _np_.uint8)
            elif isinstance(value, _np_.ndarray) and value.dtype == _np_.uint8 and value.ndim == 1 and value.size <= 256:
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.uint8).flatten()
                if not value.size <= 256:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} <= 256')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.uint8
            assert self._value.ndim == 1
            assert len(self._value) <= 256

    @property
    def value(self) -> _np_.ndarray:
        """
        saturated uint8[<=256] value
        DSDL does not support strings natively yet. To interpret this array as a string,
        use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
        .value.tobytes().decode()
        When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _ty_.Union[_np_.ndarray, _ty_.List[int], bytes, bytearray, str]) -> None:
        x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
        if isinstance(x, (bytes, bytearray)) and len(x) <= 256:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._value = _np_.frombuffer(x, _np_.uint8)
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 256:
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size <= 256:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} <= 256')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.uint8
        assert self._value.ndim == 1
        assert len(self._value) <= 256

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Unstructured_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.value) <= 256, 'self.value: saturated uint8[<=256]'
        _ser_.add_aligned_u16(len(self.value))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 2064, \
            'Bad serialization of uavcan.primitive.Unstructured.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Unstructured_1_0._DeserializerTypeVar_) -> Unstructured_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u16()
        assert _len0_ >= 0
        if _len0_ > 256:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 256')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
        assert len(_f0_) <= 256, 'saturated uint8[<=256]'
        self = Unstructured_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 2064, \
            'Bad deserialization of uavcan.primitive.Unstructured.1.0'
        assert isinstance(self, Unstructured_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % repr(bytes(self.value))[1:],
        ])
        return f'uavcan.primitive.Unstructured.1.0({_o_0_})'

    _EXTENT_BYTES_ = 258

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8W}=N@0{`t=No*U}8RqP?<%QlAFY&}%=tQRIHB929Obrw&{(cVYw1F<gXh=S32IVps4i&0E0Oim^0S4#;JOy;rQAZth)KN#>'
        's-uoN>ZoJikkrD+@+!$_B3?N2FW<j{<i~lF>VKNo6YW=c)te|c%9V`OV7_Zt+<(}`3d>lfdey5p+<-;l@$Uk^Sqhpy`^$vKqUX`='
        'pQ0b5bf{T1yDIcon)Z0fu4O#mt-66b&N6?kH8xzzQJA#Gncr~hwa7_?#`oRp=MhPi_*e8(6!uwm5cqDf8L&q5w`jMNHjScC`-96W'
        '<*ihXT4g)1tsu@XytIqE@7ohmc;S0nNQLB2tTq-n-^9}1x{h0{!m6wmbn$jcXS3WWJR=Hr$7-zn$6CO~nBR-nXBFMRs<gvJloZL9'
        '>_%W!>tz->7sK;~4WQU9^F-(nt3-nm|BRkR;aRH@*tN3lm$w5=HH+a9f#lgGH<*Z!kiyeloi!SFr<1*Nxs!!+l~RuBTq7yQbZ*A('
        's#UBsqVU#6eOu_F)Zmx*QF!e4ZqVu4cjC5NU#M7hFAB}wKpGR(V!h&)M3=y-b<w>*jQ?AY`F2qEx4NWTCC3#rb?%4fp44k4J7BdJ'
        'n#NVfmOiVAWl0PBlTVwKitSJAu+*(_yV7LQzoRszc%$e%>^37Oye>SmYh&yg^H|{SmeSv?s@;lvD?IXTsq-WTOA4@d1FLRLj48fo'
        '+a*IIo@=vW#{eY7wh2yh_g!hfi@ldQsa=`2DI<kcPI~8Fj<1a#9ciR<N_PE@?9h=R@}i@g{z4+|`(9{AN9ZW0V;x;Gj&*!jJL;oj'
        'oKE!M3aOBte5nr|rxTn~-58usz0#UaiZRjY9g&1a$j`i%Kb@k}oX&P^RiQr?`<{DkUphl)Ih}uD4niw*7v2bq&e3^J{TrPYxqR@('
        '{&a!*IbGZ}Ct)G<m);7OKA?-7F8B0HXa(Mtx5lGObeYqKFU?n237f0$6oanNhn&pK-o{yf^v;NMl}t|8IymOb@{glm-;;Rs5nbbS'
        'V<YCaImBJMxo0uxI^E!O>y?uc9;UDswjb|lY`RIeIHfo0?9S}=p2wh%Db4AV*RE4|2>Va>B@enypKu!3n(YmNnchC%JNp)wKBWOp'
        'nK$Z#@De_Q`<fHop$w<&)*hrgn{apEqtYN{Io*5XjtEcTcmF{0qq}sE(}SHGGa#_D8(Z`6z;dDc^nlZ&x9XYj7QUYyXs+~-9&yU`'
        'ZdW$mug?!W5BiL9oW6ML-U$TZ|K)qhn?9#6I6dBd4<Cpaxp)`9dT;sBm-Lv^*YDI{fg&(|_g-tDujp$|`5ikerr#8lk+nR#)+Wwv'
        '3nXMDR3vo4IVg#wjHHTn4N09+NXba4Na@s%ei{8L`gN=uWWtnTsxWm*BP}DXBCS&vSs7UsS)Fpo$;he5>6AxaMqWi;ry&f<7*a8$'
        'Qvn4T1r-IIhA}K-SjDhTBN&k}qGCiR2aXI!g`<-PPll($)2W4)jFyU)PLr6FF{xrwrzuRym{KvN69<>URdAiAF)d?S#k5W{n2|A~'
        'Vn(M~%*vQmF{{%Y=48yNnA2$<^D^dD%<Hs(1sMw}7Ia#~qKriqi#jb~Nyd_jC7qVBEMr;4vQ8^lk+Gs;MW<D)%2-vgs?!?QWUQ%J'
        '(`g;+GS)>uMRz466eKhx3?wBa6(mKI4WuNb6r?ny4D?IrSJ1Da-+(E>RA6c_4WuQc6{Iz!4P+%`6=XGJ4df)`6y!AI4CE!`734MK'
        '4Gc*bQZS@p$Us3tK|w)7!N9PDVFkk)h7F8J7*Q~yVZ?wV!BOC7a13}7JO!Qx&p=B;OF>IR%fO_BNd=P{CJjtUm{KsMVafoPz!h)}'
        '+`zPiX$8|7rVY$Um{BmJVaC9$gjof%8fFd5NtjbGr(w>(yo7lL^BU$2EJ#>Tu%KbVz@mgj1&bOM4J=7mQm~|9$-uINWd-XBmNhIJ'
        'Sdp-zU`4}<fmI2s3RX3&8d#ICreICOnt^qRH;YUV_HQZW6p%_ffBwJW)5(}e9rEb|;M1v29}fBSKJaPrYrNClJ>}EptG=W6flr&g'
        'bNJQrX>;p8klzfSj%&Ulkkh^M{Y~@fxF_k2O*rJ!zu?oo8*|8~-;_^xK4sEEmpbIr@4%-!-%5vk`XKo9)+b_@Pdm?rcsqp_ycx;l'
        '28Wir99kE|BWBVuiEfi=^?lN4L7xSWj>)w8Vj3OO=Pr{zq|v`t8r|X0f=s_QjgFsGJ6fo99)*XhRj!w!FcCG2c6esn$qTDE(K*oZ'
        'W90nTIn@aJtTOX_7C(tEM?Z%rtWmec%9dC61IsN(Ps3AIqu%sOOeiYM^6bEgLT}KiSJ_~*!TiC|y3gFP+F<8=$oSnmZf&&EY?X_5'
        'e(>Eu7<kQM#VuJr8*5hLC|jpE8eONs%~KYG+Ygmw?q;%?jzuJjaO{Q%@5e_rMBH(=#G;>_<?!)0HM6<R%PiF^6;_HL_M7!lvp6BD'
        '9xz#EEHhyG_77&!t=ayB=~nGAmWiAJXR!0g|6b3zfs+NhTy|??JI)IT?V~U$5^1X=N;Z4{zi^&E?Mx%{KNQdRe1IbW00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)