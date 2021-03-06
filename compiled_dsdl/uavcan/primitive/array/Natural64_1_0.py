# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/primitive/array/Natural64.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:22.647711 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.array.Natural64
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Natural64_1_0(_dsdl_.CompositeObject):
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
                 value: _ty_.Optional[_ty_.Union[_np_.ndarray, _ty_.List[int]]] = None) -> None:
        """
        uavcan.primitive.array.Natural64.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint64[<=32] value
        """
        self._value: _np_.ndarray

        if value is None:
            self.value = _np_.array([], _np_.uint64)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.uint64 and value.ndim == 1 and value.size <= 32:
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.uint64).flatten()
                if not value.size <= 32:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} <= 32')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.uint64
            assert self._value.ndim == 1
            assert len(self._value) <= 32

    @property
    def value(self) -> _np_.ndarray:
        """
        saturated uint64[<=32] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _ty_.Union[_np_.ndarray, _ty_.List[int]]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.uint64 and x.ndim == 1 and x.size <= 32:
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint64).flatten()
            if not x.size <= 32:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} <= 32')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.uint64
        assert self._value.ndim == 1
        assert len(self._value) <= 32

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Natural64_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.value) <= 32, 'self.value: saturated uint64[<=32]'
        _ser_.add_aligned_u8(len(self.value))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 2056, \
            'Bad serialization of uavcan.primitive.array.Natural64.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Natural64_1_0._DeserializerTypeVar_) -> Natural64_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 32:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 32')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint64, _len0_)
        assert len(_f0_) <= 32, 'saturated uint64[<=32]'
        self = Natural64_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 2056, \
            'Bad deserialization of uavcan.primitive.array.Natural64.1.0'
        assert isinstance(self, Natural64_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=1024, max_line_width=10240000),
        ])
        return f'uavcan.primitive.array.Natural64.1.0({_o_0_})'

    _EXTENT_BYTES_ = 257

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8W}=N@0{`t<TW{M&7S>%%?8J5)=blEnE2$&dPU5<0x7BWdg%_ujX4BoiEeJ}Qm_#W`;Khv#6mTC}xB!6?$n5{|qyNEf|4q+u'
        'I2uy2;`q{s0yPASnmM=coHN63$nDa9pIyntf8mY6R@dv=4c()zW!TntM%$(hz0>av`kv)e7M}UacY}@}xb$CJ1IpgA2S2dySv@T4'
        'j?u&UT3~E;45u-0t)Asuo3vrLuCdj4VW5s-uRdX+rf*W$v-%D*b7A%C<oYdxJmh|2Kd^90H+<i<+JR3!_8&GWs-X}I%YV11-Br<?'
        '*1Lvp=spiIygEUh$Hl^nUmG}zBVSNw!#DrRN3+n*=+ve?>iCJh3E>P8vvB_3j%RH+wEGXoryJDG+MCkbmap5fI|eNbwqtm{-s^WM'
        'Gp~dfUP?n;t??Y^2%o|P<$h$ZSa@Fde8cG)ZZ~acCuoPK(9*!@SpF7+T6iv*(qHrBh~Uj@A_(&aXlBj41$l1LyvwyqdfWC`cu&Gp'
        '#u2GM`kRH*f3tj%w6E}I0xvA;{Q<VYBqQEduidw;4kn4vULTX^WA(orP}lJLu1Zox@0b>r)O;K+JnuUl!>7)^q8v1rbg6^AQb+lj'
        '7lCaX?$(%OMc*{+fU;j$9kj@6n@^KutfAJ$SBA4eU(o^etw|w$qxXzAm|9e5#e?Q^ZmWg1;{5e22aCinP>kfXu*$0%*ap{!JeSQy'
        'P)NRu@i%sTA%apeRvwN)5lRtM#P0&Xu4d+-43!A9MDNtt98?h_oF3}q2>zbhR}N0W=?JF9oW^~fnJ5QSFdf0!j9nbXv6*-3z!^9j'
        '!E6%m+<~$%1G5pF8}oxRI6nVg`Y;FQA~-K(OE^Exbr;@S7v|x71Q+&=0cUaU;-PH80$hmTlF*su^|*X!eYgmhBDgX!CX~SWt4Fd6'
        'm*GkT*E0FSS+sZk$oAkWT#Mj?cgBlSD0AajKHxfh5J4^JubaoV1vj7;!7X8@_O8ge-`k`9l(+Zv1vlYV1b3vrRQ7pp?kf9fG~-yt'
        'ttYnOHr$Ee-hp+%Xlf{pviGw-v-z8ewZ`#WkM$FOa2M`HP?wlA)WKeQFpfpql}P5}c!X7%BWV?F!hNVm@bJB{pa#l+DC7_7gpry^'
        '9NZ^7fQJz*N<4Sab3I$9M-rRtIxUqk=|drter^qYJb({jF@naSu)#yF)08^JSgShpt#Z1M$*I66JjdAJ5i}xLlKT_(|FW{F>LhZ;'
        '(JaK#T#n<BHRAR}t`G@YY{F6mD~HAd4X*ci|8+cCwb7N7)GCPpF+EAwOvBk}oLN$Jdz$Xa(W<FcCF7KxnAD5M3M=p=g4HA86uKYD'
        'eOImTG)}d~R9`BLEASYez*AU_U`?&JI_fU*HTQAWw(NY_^K!S4mSz4Lyn3+A?ZQW}7QwS4<3kIm|B1@8h$P*iVlNS~h)RmJH|)(A'
        'WgN$+YM;C_tS85M9z9)xHD1%dsNNMT@zijSnTsP{NNTEfE$;7r>}v@<t-{CfX#}4g3o|_9Ha<V0`%z2W-vT@|&^H6aiH}b47|G>f'
        'n{4Mvu0V1nvW*|SD3a|W$(6}=ndB;DyFzkRvR#E1?2=ZV?B+?UKw2fTi~oyc7e6JWt)x{ZyJga<klhMtRmpBO3fdI;@|SpMcu6$P'
        '{O2Er&uYBue`h|c{mEzJJkS2gXMYzytDP{PtsS(R?Zam)`|!U>jB}LF*0R}8@!4_fX)OD*%j5Cc`~;ub?8*DWC=*nCwich1C-K=V'
        'mT}&9ZD>`p%cJwzQA7uI!v1`g<5ApboX-}9oKl@SW>fi+_7yJa<KeORY<|c+waghocuup~bUp=RSWNL*4JGRtKAYyqs!AeX9F012'
        'D29Bpe0F^Oj#g{*^dZ>TO2TK;HCv3Uwv^$s`Iz~rZXB&x_WW^g$eB6DWzHv0fX}8oGrhLcNY(mMtbJKB+Jw)F^;VBL`#7Ifwq?)D'
        'ZkJ41T23-}!hDv;A+ju@NOz~$Lqr^+j)Jj^I5@L@mhf4zPrjSa=21d+tyqKVv@FkIqN2BlUCaG7V_$3V$qDk=L*IW!&(jH?)uO<B'
        'ix)(zk{tv`v^?3#!w%63L@SXU{1nJuiL95&UYV>{$X<o4SIJ(LXhpJ9gmu^>>v^)5C+h{WULt$=zex6qL@Se>GSMnzr-G~%Ni2U('
        'YnH>Zcn%zv^lrby!W;|QMmV2(>!7!{#QTiznfX6+&I_mXE*-d(KZfqIpTo2IYwHc|>Vv-P>sFV&2<LRKAGjTg6E@WchHtXaYnuHY'
        'Z3Z57o3HyWwKkllcs;VY{K#@%+rgV|`_Z?q<)gqLXxmmtcj-o8b1&)*hL<Qchi@2~@w<!W@SRFyxv|s`LJV=3hKCWj{EY>=-n2TD'
        '{cQf<{MB4Eo8qzcO6Jk`%uA!&wVaKyN8UKQ8fs`Oo@Ss0*)xFo_Jzo4<2NP&UA;vb000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
