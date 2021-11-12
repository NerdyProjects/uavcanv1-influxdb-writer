# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/pnp/8166.NodeIDAllocationData.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:22.827128 UTC
# Is deprecated: no
# Fixed port ID: 8166
# Full name:     uavcan.pnp.NodeIDAllocationData
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
class NodeIDAllocationData_1_0(_dsdl_.FixedPortCompositeObject):
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
                 unique_id_hash:    _ty_.Optional[_ty_.Union[int, _np_.uint64]] = None,
                 allocated_node_id: _ty_.Optional[_ty_.Union[_np_.ndarray, _ty_.List[uavcan.node.ID_1_0]]] = None) -> None:
        """
        uavcan.pnp.NodeIDAllocationData.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param unique_id_hash:    truncated uint48 unique_id_hash
        :param allocated_node_id: uavcan.node.ID.1.0[<=1] allocated_node_id
        """
        self._unique_id_hash:    int
        self._allocated_node_id: _np_.ndarray

        self.unique_id_hash = unique_id_hash if unique_id_hash is not None else 0

        if allocated_node_id is None:
            self.allocated_node_id = _np_.array([], object)
        else:
            if isinstance(allocated_node_id, _np_.ndarray) and allocated_node_id.dtype == object and allocated_node_id.ndim == 1 and allocated_node_id.size <= 1:
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._allocated_node_id = allocated_node_id
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                allocated_node_id = _np_.array(allocated_node_id, object).flatten()
                if not allocated_node_id.size <= 1:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'allocated_node_id: invalid array length: not {allocated_node_id.size} <= 1')
                self._allocated_node_id = allocated_node_id
            assert isinstance(self._allocated_node_id, _np_.ndarray)
            assert self._allocated_node_id.dtype == object
            assert self._allocated_node_id.ndim == 1
            assert len(self._allocated_node_id) <= 1

    @property
    def unique_id_hash(self) -> int:
        """
        truncated uint48 unique_id_hash
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._unique_id_hash

    @unique_id_hash.setter
    def unique_id_hash(self, x: _ty_.Union[int, _np_.uint64]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 281474976710655:
            self._unique_id_hash = x
        else:
            raise ValueError(f'unique_id_hash: value {x} is not in [0, 281474976710655]')

    @property
    def allocated_node_id(self) -> _np_.ndarray:
        """
        uavcan.node.ID.1.0[<=1] allocated_node_id
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._allocated_node_id

    @allocated_node_id.setter
    def allocated_node_id(self, x: _ty_.Union[_np_.ndarray, _ty_.List[uavcan.node.ID_1_0]]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == object and x.ndim == 1 and x.size <= 1:
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._allocated_node_id = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, object).flatten()
            if not x.size <= 1:  # Length cannot be checked before casting and flattening
                raise ValueError(f'allocated_node_id: invalid array length: not {x.size} <= 1')
            self._allocated_node_id = x
        assert isinstance(self._allocated_node_id, _np_.ndarray)
        assert self._allocated_node_id.dtype == object
        assert self._allocated_node_id.ndim == 1
        assert len(self._allocated_node_id) <= 1

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: NodeIDAllocationData_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(self.unique_id_hash, 48)
        _ser_.pad_to_alignment(8)
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.allocated_node_id) <= 1, 'self.allocated_node_id: uavcan.node.ID.1.0[<=1]'
        _ser_.add_aligned_u8(len(self.allocated_node_id))
        for _elem0_ in self.allocated_node_id:
            _ser_.pad_to_alignment(8)
            _elem0_._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        _ser_.pad_to_alignment(8)
        assert 56 <= (_ser_.current_bit_length - _base_offset_) <= 72, \
            'Bad serialization of uavcan.pnp.NodeIDAllocationData.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: NodeIDAllocationData_1_0._DeserializerTypeVar_) -> NodeIDAllocationData_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "unique_id_hash"
        _f0_ = _des_.fetch_aligned_unsigned(48)
        # Temporary _f1_ holds the value of "allocated_node_id"
        _des_.pad_to_alignment(8)
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 1:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 1')
        _f1_ = _np_.empty(_len0_, object)
        for _i0_ in range(_len0_):
            _des_.pad_to_alignment(8)
            _e0_ = uavcan.node.ID_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            _f1_[_i0_] = _e0_
        assert len(_f1_) <= 1, 'uavcan.node.ID.1.0[<=1]'
        _des_.pad_to_alignment(8)
        self = NodeIDAllocationData_1_0(
            unique_id_hash=_f0_,
            allocated_node_id=_f1_)
        _des_.pad_to_alignment(8)
        assert 56 <= (_des_.consumed_bit_length - _base_offset_) <= 72, \
            'Bad deserialization of uavcan.pnp.NodeIDAllocationData.1.0'
        assert isinstance(self, NodeIDAllocationData_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'unique_id_hash=%s' % self.unique_id_hash,
            'allocated_node_id=%s' % _np_.array2string(self.allocated_node_id, separator=',', edgeitems=10, threshold=1024, max_line_width=10240000),
        ])
        return f'uavcan.pnp.NodeIDAllocationData.1.0({_o_0_})'

    _FIXED_PORT_ID_ = 8166
    _EXTENT_BYTES_ = 9

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8W}=N@0{^X9>uwxX5<X7iWHJdMAwa?{IfP4W7?14`l8}UpvBSnYBt%XK0fa_prq8&0x2L<ePxsh^gtYwF6_G~561@_Sz$3t~'
        ')k-TZkH8bGcm#fK)j8EQJ-+Os6_KE7y3eIf)mPuCYXAAb-=@z9`)_nM8G6PGn{A`hK!w5QsuSvFyBqhD*aVp_MvvUh(!87HslGQ%'
        'bn#6w`(^P(F*BNON2(9+&*o~-RZ%mElIHE$)2k~>VHkH+7R1qt%2Y9`wFf#i@U!s6=+J%AzbRT%E%Ddl%VKn-t+Ff)I(eo|@fobW'
        'hgCeP7)`$y=+GNmQ*V2)S35%!_nMxhK|jcX0gO2LVPt~!NPDYMrq^{kd9)+#PLQ=j9j#}6(OQ7TyUJwkKAf)bA0It=r(6i9HJ9Pt'
        'EqsM1`b)7^j2>^BOhukbz3M^_^Nv3~I+jPlpK{#}ytc25UyKg4y|`P9t}jJWr7%2I=}=z0G6$-}5i;({%-7P*n_FEeAE1*%8NtrY'
        '0+v4RjQ3BDp4r2DX{v_B=+u1$PvOb?)~qFbI(hs@+B(#I9c9j){yth6jd!uOo35@D{vrQx8Abo-XT{hE|4GuGY905V_MdGD^o)P@'
        'E9->mfeLe2`T3Cm)79u?1pw{N&>`!K!oTb<8i<CclT-tuv{yVF9c%Z3P3^UlIL*L|#qH6Fwu$q!tKmhc+lc~SkJP*$_w{@ZE|~Ad'
        'sfJ+BJL3n7b3xP#^G&Zaw~+$G)A=Otgh98R>h(OtUB*~4G-)1BJiofqTx>2h-6H@IMiBN((N(a~An5AiAsp)OE4mj%+DK)?12JpX'
        '??J@+YBT8PeF>)zJZXI(10&&hI`Uu<8AlXqPp9E9h}I>*Au@PW8LFX9oAvuR%RulqbP9u2Bo{AS0pw_@!VNVvv^bm@9)#ohrdeOp'
        'J)9HUJxrpzK`(H5YKQm1O%hxaHxZPb&=jMWOC*h93<u4&|1L&H-wiT{r@QczkTlxgj+0^}_gcgZ`<)mZ51zcG`!V1YZTTS4smkJX'
        'jK_oRt{*_M`!`3A-cg<he%Ud|zlCpa=V1uxv;8fs-~jh^G1EG}Wja7fiCd^>)$$G;w;x1B>o_WE6O}`l?SKYcyETRL#8zt`$^9s&'
        'wps`1_cZ-Ji1NTz>k!I)Tdf+sKaBFwR;!Nk;8yDh%IU4vQ5ydU%KcldV>ItkTJJc`KjG|dJx1~*$;U}PLGnqGr%0YA`4q{gNj^jJ'
        'S(49@JVWv<NlEf~lIKXiK=MVBFOhti<av@aBxgy!Lh@CT4U%&tn<VE+E|6R#d4c3>BrlSDo#Z8wmq}hB`3A|WB(IUYPV!BXZ;^bP'
        '<U1s9l6*kYC%H-TE0W)m{Ep=JB!49N6Um=R{^I1V+7v0LOJ$~1u9V8nQh87+eyMDh%2%cGZK-@$D&LpNkEQZcsr+0jzmSr{g{L<Y'
        'AP&5z=~>5gAW;s(O_-=|kPYFk8$DL0a}O_Lx-G`UUjyPl<0ya0U$Kw<-}%3<B<vH*afG}c?V9<x8zw&RD^>;mUAM%2w5SGIJh9ZN'
        'H5IMvHK5Wg*o#K~=(2kXCbYn)k6Xh31g@t~F~`eX-8I+6j%*j4?}9U4VD27vTAA&F^IdSp3(k4LSuZ&6#g5Duocn^aUvT~lW&pt)'
        'AeaRN^MGI`5X=RF*+4KK2xbJqoFJGL1oMJmW)RE`g4sbZKL}<B!5kr&B?R+?V5Shv6@uA9Fkc8}48fcsm^B3RhG6Cp%pHQ+Loj~`'
        'W)Q&~BA7)4^N3(35zHlm*+ej(2xb()oFbT21oH}Nx&H&J9c>VjHGt&lUj@m1+aS3gVRew-Sx8PHz$_$d2*kS64iF@3IPR#^1VOUa'
        'Izo`Fwdw@PTI(=DvPO`sA;2Hwbx%5NnjmR+c*1G>36gfNQ%;*ANZMVWa@uKvq}85b?OE2IW9<xUXIYc1J<r-X)?Q%kMb=(o?Pb=^'
        'vo^!pENic@_9|-)*5+7ivNq4!0&9z`U104s)-JO4I%}6$yUf}Z*4|+4Dr?tRyUyC1ti8qB+pN7)Y6MBETF!@Z{e*HI9aP3x&tlaL'
        'Rqp$DeXKA$TIzn14WV?DsfHHCWU{Y~QR^CNP9BrQi7T$%IH*Y@qsIfG4bc7@NaoT%@rRG5gz#U;{c8{X>$m=W)_-%f@f+9k(5=p2'
        'S-f;<*Os+f<@;|#MgQRSV?x~XZLJQKy}e+{Hcau<@-$e}2hdkS74Hghuv%^enO~{K<%X}ZW{=`%*pGALUO|0sY%L#RgQ>kb6zi8|'
        'X9#T(ZkMQG7%Q(KP2TmTGIBXo#spotymY%MvBRjC2S#+E<qN=u82WG7OXI#ZI8KB0AcEHM!=?K$Q4SU+n}NDD)quO9CGhyMY0CHD'
        'ER`d~up0Fs6+`5VZmu^QR()>;Y_&~jL+Y&CoJ9jt>mX(OjrzKd;GTxpw)?>10y@*`F?NfO99)0^*#qB+?#LvKv$z|FGRTY$d#<H2'
        'UFatr+VIfOW9Qh?x)Wkh@af<}Wh?Svbs#Q12r!J+>`o5Vh>>|heHs}LW*ZF$jRDunLx*It7o?B}NvPpfvu?Y;9yBM|tl7?f+|2{X'
        '&S#h*s@skG;PEm^lr+$wgnF)*LOWc6N(r+PGA_QA5TGsfY#Uq+q%)L8*kW7bC(HpmY}8@TJ^&h)+x7(_$eeqsk750|lPTzQJ-}#P'
        'C5h`<RrO1T9ofsHt~G+1&++N4v*J8UasU*l=&%fSk+=)&i<#?oPBps6B^54O=S2f|pz@oGTwYtAyL9oR8<b;l6b|Ww$%dX-JhRK1'
        'Jj`s;L7I9HE5cfw8fTr!6Wf6AOmv%+kRcEQ?B3}smyyPg^U#BKA6P)SNcymWS6w2rK&LhxdvnX229K$O0gN34%3*Yo10Ht<0RRAw'
        '<Ha(HGue&Z1{_az?6oR4#l$KV7b3HSx|hv;uG4rfv9Q%H_>(aPo=ZLV*}w%GPIE3XItLSYw{r~$x@URL!j3*|Si|Z&4y`cz$8eNo'
        'HbVAPPSBLA8HN^(UXOy$HD#9F04@s!zDNPJU@+*w9Xdtx>IU*vYKTcUGh?Q-r?Y89SDB{cAYjKK<cqHSaN~|rext#`aEuK<fK@5n'
        'bpld_{1HeEU<))>53TDVQfL^0Ad4Zt>?b+Kn%0E1z8cC%+d(q69gN<Q-C$%4cG!INgLQxI*1Zp_w2W(X{W!*8#Ar*MG5~J`Faw6#'
        'l<n)xk3EENB|;brYpa3#t2?w|H9<cK`5pkPS1X_}=z9Y_;W&;6oQBns6hAqo6?fWz_G1J%Ur1CnxHR7pfjUfK8YZll^+QAYkkjCw'
        'Ywmb>uRzPF2bPiGgy0l=KrlE#;{jl{S9RWo;h06$(xhH7$VL!%ua+*=?a^Y~72Q)tu=?JH0-0U*fnx$9@{+b2b%!HsbXO-XIe_!K'
        ';}u-q8iXdCXPnLr!l27)EOS!pFXIx?-m+LGF#v5AZa83JnwFEc-z5+pHNMt68WB&$2u|Jm5;8We$8d%{0Vy9uRUXp%Jdh*irvpcM'
        'ZPPtvGdzv+b>9(Mj3%Q2Mq9d0^H7_s^}3X6pvk4Cgyrq^W<PRce6PYwDHkW9q%GOldce3FC}8`WcEW`n6EcOVgk}&k%X>jzr{ygP'
        'hxP!ySmmX_5NO@K62@%cyVgLxnFOh-R*aJ?&e*;1asZ^kZ+l9))R6BsAj{<PET3s|9zety`M*t)Gr$J`A_$+}nBC*ZofJw-{5yxS'
        '7x<VGwiWdax>jw7Fqa%g$4LU`aG^8Ka`-p-HxGO=2NwUDKXR~r&2p_By$G!38jzWZWS$)dV%Y{lMZ;b0a41X%;F+LD<*akR3Za_o'
        'tE}t)_TDe8S|O`;>mWY5d1LJcK*RoBqe`BTe{-CK4H+~wl-gx7PXx^o$ZYAh|MqX`_6q!eh9kN?Ue*y*Hda&l;`Uk=NB@62?u=@c'
        'c=yTylf{YI1J6thU^p}e>_pdyxq^}^Exh90Dz9x{1;W{fW+|gZh)9yMnBAo&bPHW<${U+dG#9&n`uu>k@w0!rVgJHUox6>!e*Rp*'
        '&z}$QZx{Z@tp)!R`0rDA_rq;?@DKMP=?Xl(IeuCWo_vfAe)B)>)M}3q9smF'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
