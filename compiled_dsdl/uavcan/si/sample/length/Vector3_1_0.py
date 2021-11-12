# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/si/sample/length/Vector3.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.169489 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.length.Vector3
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
                 meter:     _ty_.Optional[_ty_.Union[_np_.ndarray, _ty_.List[float]]] = None) -> None:
        """
        uavcan.si.sample.length.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param meter:     saturated float32[3] meter
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._meter:     _np_.ndarray

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if meter is None:
            self.meter = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(meter, _np_.ndarray) and meter.dtype == _np_.float32 and meter.ndim == 1 and meter.size == 3:
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._meter = meter
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                meter = _np_.array(meter, _np_.float32).flatten()
                if not meter.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'meter: invalid array length: not {meter.size} == 3')
                self._meter = meter
            assert isinstance(self._meter, _np_.ndarray)
            assert self._meter.dtype == _np_.float32
            assert self._meter.ndim == 1
            assert len(self._meter) == 3

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
    def meter(self) -> _np_.ndarray:
        """
        saturated float32[3] meter
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter

    @meter.setter
    def meter(self, x: _ty_.Union[_np_.ndarray, _ty_.List[float]]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._meter = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'meter: invalid array length: not {x.size} == 3')
            self._meter = x
        assert isinstance(self._meter, _np_.ndarray)
        assert self._meter.dtype == _np_.float32
        assert self._meter.ndim == 1
        assert len(self._meter) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Vector3_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.meter) == 3, 'self.meter: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.meter)
        _ser_.pad_to_alignment(8)
        assert 152 <= (_ser_.current_bit_length - _base_offset_) <= 152, \
            'Bad serialization of uavcan.si.sample.length.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Vector3_1_0._DeserializerTypeVar_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "meter"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f1_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            timestamp=_f0_,
            meter=_f1_)
        _des_.pad_to_alignment(8)
        assert 152 <= (_des_.consumed_bit_length - _base_offset_) <= 152, \
            'Bad deserialization of uavcan.si.sample.length.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'meter=%s' % _np_.array2string(self.meter, separator=',', edgeitems=10, threshold=1024, max_line_width=10240000),
        ])
        return f'uavcan.si.sample.length.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 19

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{^X7NpBp-6(%WB+(d1ZWLc7}lH-VEqUqr_)X0hBD0CPbWl@3_TS$<!tGkP=f_h6;HOVnxAU-4zfd<lmJAi(Ie}a#J'
        'or8h=fcTz^kslEFnD@G?XNEF$iva3-UCVo4y{&5gbo_7sogJzE<=4_)po7qHHCK{_@)PET+;RORN)s&&FZ0=lMrFRq6o1r9dHH#{'
        '_*waBxsZ>$F^gdSTE=#L7CTxxnnfw>4tcy|g!3WyO`=xIeA3<JO3NfJ#YjH!p_M-`=_nofOZi!u&$!GOCB4jWUH%?)zl2qPRhf@('
        'N*)FSHq&mv408=q6l3+E7|*X;az;kndDx46p^{jB!h=UJpbhXX#e|q@n23{LU7WGo=U&DmRWg!B?gEdw$FY_>F%RC44d3DFu#aY3'
        'Pa3!OM@hTD(r4PZQ4#>ltNF$IjUwFUY{1-IoI=<9xqMLO=Uw0!2TTRSiViXljy4lXUnQFRNgR~<aW_c(^2vY3Mn)b9PU0-`xFX3m'
        '8Cs=@5zG+5b~#Cz);u6u#y%%Hi8x^jOem&$B!bV_5E;YzYNc_eQK=mVrHPU|Fufoh?%b?ap@WIXG+!iAlYnna@Ciw|YOyp8rOyn+'
        '+##sO&y+$v{VixI(|j5NMLbRv|6>NRf$iHWi3ZwrKYW!k5&<!;ZW7ITwa8CEuTJ5hGTwnvwJYIl6%|=opN3Naxm^}!99f!##C#Xs'
        '1pjS^$zIK`Ki^qzflJ7q41g#18E|}SdYX_HS@}a}{jg_YIrEatkd>8ghx9m8`X<>E(ib=dRS}z>L++6EwMysEUf`WU?kKXCWMKe?'
        'zycvz9CM#*&6Es#H3dinB8~2|1-HRAV2csyfK?-sOyjD`JWK}}s2~iifnvTd!C$d~JSM)9T56|0%ti>gApO?Hoh`BuCx&dkyGS4t'
        'V(_H`dp=W;6j_S?x<$Mm6e(IvSuadj6=Mh#v;wCh{-_BRiIDydEY^aBAx0R}Z71ZdYI$v9n-3fnaTus`)b!&3NilCQEzk!FXJZHq'
        '0ViswghDu#Pi`bJmWk=totP7^Tj@IOiZ{fYbOh^3%-5we@py}F-TP>(6pQ(d-*T0_Xu8Tbh#Pw2X`JlEPMM!@D?(-dTGJHxehLYP'
        '&FoN1n0!#>Ckq=sqLWX-k$oK1Fu!SKn9oO-N@S+J%;WjoP#<)?Ufp2v6bs_ASQV`d8cM*yD3lWq%7grryDj&5;9{U$8I)W3Syv~S'
        '@;OX|+)Wv@i`=vYRBjsrpxWDs;?S?!bzj_FZpnB%%=QDXwWpxnt9F`sP_C}xJ6VWU27OiAO>Oi}`^aYMEIUh1y$V{RE0_ifSnRGX'
        '$MOJN{?Dztyiqej&6pcd?TLcgN0(xjLJ2b{PqUY(r>!dg^^nCXLX}C#3nLEI6DUZ+tgiT~;0Jc#L&zNg6$L&_B4}rUHH_KmC7=m<'
        'QPXp)ira-XiE8PT`*K?jWi?y}Pq~Ag*9#%4H=3*%G-^1sdGWi<PyR}p5328nyq~i9F*ixeoV-kl?nPb#aRIO1<xyf=;612426yb>'
        '!a3pk0*bv9_w&>DS%97J2aCjGoZZU85Ssmqv!e6Ya)EXW?ZLI3)*4DWnR#%|NXB@Hfxz}rn81q+vILdVQQS9D&@qe05XTC7+<uQE'
        'ju!NU9iOn{lNP7!_%z~)g3j3WClMzLI*WL`pr`Em(}*(#J!9w3B90gIoYgajc&?!55ziF#0^+HHUPL@u&{q(r3wp`!f7RN(Z0%gJ'
        'dahb~uOVJ3=<A4=3wjOl)q)blO9j1-_)0<FK)hJcA0b{S=$nY=3;JWkxq{xXyyg+l7IeY#TSPov(4SbIKSi7^=uOMFWzXwa-fhIG'
        'f-YJ9%ZL*NU9sm_wf<PM=c(d)tf1@mT(_)$yY_sy>$uamEdI>m&n>=f@fQ}~vG_}i?^%3eQCQr!_{`#Si(gp$(&9H3zqR<C#qVpp'
        'J2`5FOO3G52;D|_uMwU!f@p;OMtIf;&l};3M)<N3zG;MS8{xY~_}&T`yyc+(!>xgh+>UwJ#^HXMGK1IUVm^Y`)Zk5d<t1-hrC1MM'
        'e4E(N>;7;DhYmj|XI&n0e1+MU?$vy16K-L1Xcb&~1TMW5G5-u$Mr;S(KN-F_-_GY(*OpegE30ek>#N<)O1Im&-CbV3wY0X}U0v(0'
        'b(Ys}uXNVd>PrcVehMC}Df6Z2mGqc+UwlwEiF@L~P%k<6fT!HZqdU@=`xLi67QY+nFQlkE^)dZeF!=L6Et~$K#oxF3ejJZDTuI<V'
        '@iknJ;tm@8N}Lt{7XQe^#({WuOZ+-l|L5CH%Xa-crd>DSw*4J5e7A|;93ZKq9r96M8g|kJc%|UA9Us}b(b3qr;jY9VKu2nOC|o*P'
        'd94dx>!Q~xXNiAtjib+D^!Z@a#jgE>Vf3u?KlL4&_W=$700'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)