# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/pnp/cluster/Entry.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:22.845997 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.pnp.cluster.Entry
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_
import uavcan.node


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Entry_1_0(_dsdl_.CompositeObject):
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
                 term:      _ty_.Optional[_ty_.Union[int, _np_.uint32]] = None,
                 unique_id: _ty_.Optional[_ty_.Union[_np_.ndarray, _ty_.List[int], bytes, bytearray]] = None,
                 node_id:   _ty_.Optional[uavcan.node.ID_1_0] = None) -> None:
        """
        uavcan.pnp.cluster.Entry.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param term:      saturated uint32 term
        :param unique_id: saturated uint8[16] unique_id
        :param node_id:   uavcan.node.ID.1.0 node_id
        """
        self._term:      int
        self._unique_id: _np_.ndarray
        self._node_id:   uavcan.node.ID_1_0

        self.term = term if term is not None else 0

        if unique_id is None:
            self.unique_id = _np_.zeros(16, _np_.uint8)
        else:
            if isinstance(unique_id, (bytes, bytearray)) and len(unique_id) == 16:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._unique_id = _np_.frombuffer(unique_id, _np_.uint8)
            elif isinstance(unique_id, _np_.ndarray) and unique_id.dtype == _np_.uint8 and unique_id.ndim == 1 and unique_id.size == 16:
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._unique_id = unique_id
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                unique_id = _np_.array(unique_id, _np_.uint8).flatten()
                if not unique_id.size == 16:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'unique_id: invalid array length: not {unique_id.size} == 16')
                self._unique_id = unique_id
            assert isinstance(self._unique_id, _np_.ndarray)
            assert self._unique_id.dtype == _np_.uint8
            assert self._unique_id.ndim == 1
            assert len(self._unique_id) == 16

        if node_id is None:
            self.node_id = uavcan.node.ID_1_0()
        elif isinstance(node_id, uavcan.node.ID_1_0):
            self.node_id = node_id
        else:
            raise ValueError(f'node_id: expected uavcan.node.ID_1_0 '
                             f'got {type(node_id).__name__}')

    @property
    def term(self) -> int:
        """
        saturated uint32 term
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._term

    @term.setter
    def term(self, x: _ty_.Union[int, _np_.uint32]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 4294967295:
            self._term = x
        else:
            raise ValueError(f'term: value {x} is not in [0, 4294967295]')

    @property
    def unique_id(self) -> _np_.ndarray:
        """
        saturated uint8[16] unique_id
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, x: _ty_.Union[_np_.ndarray, _ty_.List[int], bytes, bytearray]) -> None:
        if isinstance(x, (bytes, bytearray)) and len(x) == 16:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._unique_id = _np_.frombuffer(x, _np_.uint8)
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size == 16:
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._unique_id = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size == 16:  # Length cannot be checked before casting and flattening
                raise ValueError(f'unique_id: invalid array length: not {x.size} == 16')
            self._unique_id = x
        assert isinstance(self._unique_id, _np_.ndarray)
        assert self._unique_id.dtype == _np_.uint8
        assert self._unique_id.ndim == 1
        assert len(self._unique_id) == 16

    @property
    def node_id(self) -> uavcan.node.ID_1_0:
        """
        uavcan.node.ID.1.0 node_id
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._node_id

    @node_id.setter
    def node_id(self, x: uavcan.node.ID_1_0) -> None:
        if isinstance(x, uavcan.node.ID_1_0):
            self._node_id = x
        else:
            raise ValueError(f'node_id: expected uavcan.node.ID_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Entry_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u32(max(min(self.term, 4294967295), 0))
        assert len(self.unique_id) == 16, 'self.unique_id: saturated uint8[16]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.unique_id)
        _ser_.pad_to_alignment(8)
        self.node_id._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 176 <= (_ser_.current_bit_length - _base_offset_) <= 176, \
            'Bad serialization of uavcan.pnp.cluster.Entry.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Entry_1_0._DeserializerTypeVar_) -> Entry_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "term"
        _f0_ = _des_.fetch_aligned_u32()
        # Temporary _f1_ holds the value of "unique_id"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, 16)
        assert len(_f1_) == 16, 'saturated uint8[16]'
        # Temporary _f2_ holds the value of "node_id"
        _des_.pad_to_alignment(8)
        _f2_ = uavcan.node.ID_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = Entry_1_0(
            term=_f0_,
            unique_id=_f1_,
            node_id=_f2_)
        _des_.pad_to_alignment(8)
        assert 176 <= (_des_.consumed_bit_length - _base_offset_) <= 176, \
            'Bad deserialization of uavcan.pnp.cluster.Entry.1.0'
        assert isinstance(self, Entry_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'term=%s' % self.term,
            'unique_id=%s' % _np_.array2string(self.unique_id, separator=',', edgeitems=10, threshold=1024, max_line_width=10240000),
            'node_id=%s' % self.node_id,
        ])
        return f'uavcan.pnp.cluster.Entry.1.0({_o_0_})'

    _EXTENT_BYTES_ = 22

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8W}=N@0{^X-TW=i2636YtjxR|}B{m@>kTkbo0-42J4LNWKn2@N6vBE{Xpi%EmuX~c&nPD!D7YQjmoTKDuBwC`6#3N5A;tBD9'
        'B0wM^AtCVv_y~Li9;w=`j-4ewPsft=ukNm{uIk?T^~}|Y|GqRgHu!6f=l!URk{~Q~5vwHrNVO9kgq^IHXJuSz*X)10D(X&E7y6xk'
        'uH9$uu}|E`Zn2pRQ`N)q!?oJzs5HpaJm@5KS?MBpJ*|qqYo@~uU6gT_Iy2Txy~p-vPL9j5f4fgyvo};#RmAPO(xv+VgYJ;dEiczh'
        'o{e=9ZKW|AMygU_MY-)XJul*3T*VvcG5>B_#_Oq$&Zm`L*TwBM?G4*;6(%}euZ)udgLhO}g}p4&&MY*C)_fqE7QBXI7ib788vB>K'
        '=$eJFtW+AQBHAA4THQ92%>-^t&ovWalyzLQcu{wCA*xJNMvIH8TZvrd*wf7lp*QnHrK-Z+3LH*`VR~l1Il9CC6otb5UN{?X>gdhE'
        's%NO{_UiVBI?+9yR>R#ghdAuLa@rg*$INj|w3)$@bJdBfzLS92wv*B|C;YNoRbd9zXxlaWUX82a`fp>CS8jHPS?(IKQ;@RXYiCJ}'
        'yE1=4_cAPsDt`-iLseO^mH(cwV`4me^K5hQqRw>{-`Q_hco}myFQVUFt96p7qCe_{u{KmvYxk*Jl+(6sW91WJFHW7jN`~4bV~S3`'
        'P83Cz<K#MK<u2CUq`Rz~;PxcxZY%e2{}k&qkI!&>cDSV6OFCucK5p+P-D~9>``yL;!1E7~&RBVn$LC4stXyEfySe`m=|L;+A>D7~'
        'VIIGi^E*O%*vg}%3s&Ao3Rd1vy3fjE?0=ke!b-vGKR|lFl@F30vGO6(d#rqz<2*uoz{(Sx*P~p|BFB4-bkfR`oaf`DC#`&fbkWLF'
        'q$jKlNFTPcMf#wXPm&5Nmq?FU`4s7WRzA&nJj3-oOM1x4=Qy9|c^{U!z85&J7rD;Uq_bB3gY$cdbdQxUbKU>sJYV7Z&yg-$`99}s'
        'c->8&e~t92m7lZTV7<xuE9>v9f3W^J)C<$&Y#jE+qBoYkan2j>d&78R(;L^k@wqo{c;luwe)Y!h-uS~Cf3i^{{E$N`9Wa~w+Vr3x'
        '%Vz2{{;<|zj1S`jP4MoZb?W?z$hye0xD+Z$vd-W!J}o}dMJD2|sME`7c4dTUW*1wN%^Y7ODIzsEzv9f4nejJ;+4q6lHff7oaEn|R'
        'VRHCPV@hMVh-&7yT`ys~KfJI$cII32O^K|JbY5u8Qb+E3GZ%IVo?)I971g!c90<#-E;<?q5*_9WN#3ZI$$Gj~BYs;*YK>P(Ynb-N'
        '(y2J@CiQ02K6RzQo3m);bsMP`7J3~Sf~#!ZR3%SpQLU}>E5TCmWH9VP2!=+LxL!e|#)UTGj&|3vsGnAJH%>L~uAq6i-@)uVczYnN'
        ';$GboSbZFc!5#=a11wLc5e5-iI=E$OY!yjAPS-_M;K5R<B2j(3uxH<+S*1v_D|9Ovm5QaOmIda3M|nl{OAb!A6Q1qX{4$um?ItU8'
        '-HE&L@azZfJ=`XNTayLO1ZHV)a^@NHJRjkJ(rYS;Fs;9#97oR#C#(#g;<Ak|75UKH$!R?Gv-lHu1OLzM$msDAMvpV2Cw5@;6f=4c'
        'GkTI4J;99LJ;Lbm5k><u8ko_*j0R>jFr$GP4a{g@Mgub%n9(r8XkbPIGa8uDz>EfFG%%xq84b*6U`7Ko8ko_*j0R>jFr$GP4a{g@'
        'Mgub%n9;zD24*xcqk$O>%xGXn12Y;%7!Ay5U`7Ko8ko_*j0R>jFr$GP4a{g@Mgub%n9;zD24*xcqk$O>%xGXn12Y;tqro#8Jfp!g'
        '8a$)HGa5Xj!7~~>qro#8Jfp!g8a$)HGa5Xj!800cZN6l~gL#U;z*s)II)ua>piB(b<|aL1!W=L+%tMz>j*pF*uWIw%b@TnI`JuV|'
        'e<mG%9<=!Lpf&hB*v>rjBk}D&Z>3tSrE8vU+Y%OfFa>dkbx>RaoWfUTB-o%leuwU4X{pn)refDKOwRNIv6g66YEf+G)F8&0oCrzT'
        '#K=B^RirBwC*@A4`sJ3j9bb39mZfx!q<4I8r8jDNZAF~ZC(i$lc4--pVbHjA8m*oDw?k1N6wPmPe8571EEL2-^W`dbEbEebzrfxv'
        'wt9bKaE^5UJaqmVd%ym>^X=XAa|`|gSqG#vNDcr1'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
