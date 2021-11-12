# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/file/Path.2.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.060631 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.file.Path
# Version:       2.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Path_2_0(_dsdl_.CompositeObject):
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
    SEPARATOR:  int = 47
    MAX_LENGTH: int = 255

    def __init__(self,
                 path: _ty_.Optional[_ty_.Union[_np_.ndarray, _ty_.List[int], bytes, bytearray, str]] = None) -> None:
        """
        uavcan.file.Path.2.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param path: saturated uint8[<=255] path
        """
        self._path: _np_.ndarray

        if path is None:
            self.path = _np_.array([], _np_.uint8)
        else:
            path = path.encode() if isinstance(path, str) else path  # Implicit string encoding
            if isinstance(path, (bytes, bytearray)) and len(path) <= 255:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._path = _np_.frombuffer(path, _np_.uint8)
            elif isinstance(path, _np_.ndarray) and path.dtype == _np_.uint8 and path.ndim == 1 and path.size <= 255:
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._path = path
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                path = _np_.array(path, _np_.uint8).flatten()
                if not path.size <= 255:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'path: invalid array length: not {path.size} <= 255')
                self._path = path
            assert isinstance(self._path, _np_.ndarray)
            assert self._path.dtype == _np_.uint8
            assert self._path.ndim == 1
            assert len(self._path) <= 255

    @property
    def path(self) -> _np_.ndarray:
        """
        saturated uint8[<=255] path
        DSDL does not support strings natively yet. To interpret this array as a string,
        use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
        .path.tobytes().decode()
        When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._path

    @path.setter
    def path(self, x: _ty_.Union[_np_.ndarray, _ty_.List[int], bytes, bytearray, str]) -> None:
        x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
        if isinstance(x, (bytes, bytearray)) and len(x) <= 255:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._path = _np_.frombuffer(x, _np_.uint8)
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 255:
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._path = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size <= 255:  # Length cannot be checked before casting and flattening
                raise ValueError(f'path: invalid array length: not {x.size} <= 255')
            self._path = x
        assert isinstance(self._path, _np_.ndarray)
        assert self._path.dtype == _np_.uint8
        assert self._path.ndim == 1
        assert len(self._path) <= 255

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Path_2_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.path) <= 255, 'self.path: saturated uint8[<=255]'
        _ser_.add_aligned_u8(len(self.path))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.path)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 2048, \
            'Bad serialization of uavcan.file.Path.2.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Path_2_0._DeserializerTypeVar_) -> Path_2_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "path"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 255:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 255')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
        assert len(_f0_) <= 255, 'saturated uint8[<=255]'
        self = Path_2_0(
            path=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 2048, \
            'Bad deserialization of uavcan.file.Path.2.0'
        assert isinstance(self, Path_2_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'path=%s' % repr(bytes(self.path))[1:],
        ])
        return f'uavcan.file.Path.2.0({_o_0_})'

    _EXTENT_BYTES_ = 256

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{?|oZExH}5WciYb4h7S2~dd_brltKk%$ihfr?KYQ3L3j7cNOvippwj&)qJy*VgX(5+fne4<IV7M5QkOiXVjd0<*R+'
        '*R(ltU(TMLd1mIBXUD(H|M}NqtNPiSc^T_C38)4oSR#I6VFCe-vNX@MFyQQ!1EY$_6bcT@9NaUv_SpUGI(C6dmg4!V1sg|9219{?'
        '`^<1>+jI;{i%dG+vWxec=Vz{eq2Kz=J$CjoWyUBG76!C?h+s3yIQ4RNVOu~FPtz~cm>EWmugShWBU~v~I(y?DLn~VDf*cv%^VYMy'
        'T%nLa3eq%qGs?-8NQDt&^jJBPT8t#b-$(-^P-pQj(@+?iROwv5jm1Vx8=7V@IR2J>bAJNl!-6e5+wn)pQ0rGWaQ1bo4U;ib@$*2x'
        '7olB3q?|><l&=4;eXTj7Lr+d!Jb$Myg5T`7IpM4QIS<L-^U?D(OtiD_PuiP;W2ffDcV}PuQka^w1AJ}TvlnTWJ4<GP=rRqnL_|o^'
        '4x|~9XK?&`IVff_H6`g1jkv&(@{jEsTbYcQ0eP;gZ`yk*kX|h4e{Hu&5~j+RJTK8POA2s*xK6+QREK=CA>%ei-54-Af&t`U#H^AY'
        '(UhGawHWY4W#n5Etct%>NF0)XK)0R07ww{-YLPG>-=Fiot*8BV{a@hV;Us6W(*JG|0#>w#W7*$nwfVQ_MerkZ^SStfozJV=G*9CU'
        '$!s|^UbStc%8TQ4938&$!pLt`!$yFmgFE}ZLGN%6=l_6z&$sNmlc8Z*3be25jI7&(Y62{opkvI^P_f8cQ914H<{8iJg-<?nURzbU'
        '5C5;2<(=MrdiT!mSBGCW)o^H1@E`5Pjm^zdFt97nEeINx^{Vlp-|_1_<Uer5Wr5c$25iGCCw5QlRlEi#5Ys$UhKktj+Urzjg^Gas'
        '<wR>bqb|=<=oWajyTeQY-r{b(!p0x13pq@RlQ>*IR=E6BH!ng|GF33b5o4C=($P&&*F$&x-U~K@4};o>(x;qh%&7cQ!Bk@rfqTLq'
        '-2Z2;)!GG(Sj58w%RS-|h%V8V5?><$8R0sJiIC*zaQk*Z4mpraCM7|2i<oFYV6R*vG%<LFeH`PmAUa{1lhy93ht)!kJaA>}pmB{T'
        '7~(P}Caa=UmKhQYBoLuW(($$=iz)?>Y)Fo|h`3J?!%*O=BVk#^`F2391<M0KQcyQFE>;bibRZZ7WHksd9d=Ko&(Xx=N~_-S-l5<;'
        '1s#?co)sgGz?djyC5gDdrM~y7v%-IQFc->xj9hvdl8y%fiCsq!uYJBu$U5oO)a98#Cpq#xvYJ_>iIGIeN8VO*jVY756u^>>1qQMy'
        'tHEr*DO-qISth{KlLq}<WXC_?-CFe<XLi%IeHO=<=B1s4r=Q{nHLs8HV^W-5A*Tx?_zyM8Zrj%f000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)