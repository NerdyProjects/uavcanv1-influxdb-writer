# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/foreign/uavcanv1-influxdb-writer/public_regulated_data_types/uavcan/time/7168.Synchronization.1.0.uavcan
#
# Generated at:  2021-11-11 23:08:23.009306 UTC
# Is deprecated: no
# Fixed port ID: 7168
# Full name:     uavcan.time.Synchronization
# Version:       1.0
#
# pylint: skip-file

from __future__ import annotations
import numpy as _np_
import typing as _ty_
import pydsdl as _pydsdl_
import pyuavcan.dsdl as _dsdl_


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Synchronization_1_0(_dsdl_.FixedPortCompositeObject):
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
    MAX_PUBLICATION_PERIOD:              int = 1
    PUBLISHER_TIMEOUT_PERIOD_MULTIPLIER: int = 3

    def __init__(self,
                 previous_transmission_timestamp_microsecond: _ty_.Optional[_ty_.Union[int, _np_.uint64]] = None) -> None:
        """
        uavcan.time.Synchronization.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param previous_transmission_timestamp_microsecond: truncated uint56 previous_transmission_timestamp_microsecond
        """
        self._previous_transmission_timestamp_microsecond: int

        self.previous_transmission_timestamp_microsecond = previous_transmission_timestamp_microsecond if previous_transmission_timestamp_microsecond is not None else 0

    @property
    def previous_transmission_timestamp_microsecond(self) -> int:
        """
        truncated uint56 previous_transmission_timestamp_microsecond
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._previous_transmission_timestamp_microsecond

    @previous_transmission_timestamp_microsecond.setter
    def previous_transmission_timestamp_microsecond(self, x: _ty_.Union[int, _np_.uint64]) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 72057594037927935:
            self._previous_transmission_timestamp_microsecond = x
        else:
            raise ValueError(f'previous_transmission_timestamp_microsecond: value {x} is not in [0, 72057594037927935]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: Synchronization_1_0._SerializerTypeVar_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(self.previous_transmission_timestamp_microsecond, 56)
        _ser_.pad_to_alignment(8)
        assert 56 <= (_ser_.current_bit_length - _base_offset_) <= 56, \
            'Bad serialization of uavcan.time.Synchronization.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: Synchronization_1_0._DeserializerTypeVar_) -> Synchronization_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "previous_transmission_timestamp_microsecond"
        _f0_ = _des_.fetch_aligned_unsigned(56)
        self = Synchronization_1_0(
            previous_transmission_timestamp_microsecond=_f0_)
        _des_.pad_to_alignment(8)
        assert 56 <= (_des_.consumed_bit_length - _base_offset_) <= 56, \
            'Bad deserialization of uavcan.time.Synchronization.1.0'
        assert isinstance(self, Synchronization_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'previous_transmission_timestamp_microsecond=%s' % self.previous_transmission_timestamp_microsecond,
        ])
        return f'uavcan.time.Synchronization.1.0({_o_0_})'

    _FIXED_PORT_ID_ = 7168
    _EXTENT_BYTES_ = 7

    _MODEL_: _pydsdl_.StructureType = _dsdl_.CompositeObject._restore_constant_(
        'ABzY8XQGW^0{^XAZI9c=5x%r}ahWzn;2=QT6xm$gr1+$}gON7%#RV>BJ67$p5BHK92n>QESK{_auF55)Qvw6chZYSWpasJIp#Gcw'
        'jLyvNlB?Hqfa;4Ra(8xi=9y<^mi+6h|NhU1TlAT|Kbl4=O1i${xd;;RWzbJ}*AHbnl1dc3n*Hdk$jh)ObACP@@#@>E{dM)CYRz8r'
        'vmk~0KP!WA7-Zc-q`Z4J&B8dB8OSMw%&OT9f6Q}*KjW?08=srs-&T)ad9?NS>g#IurXLhVF8XD`RrMU?uF<F-Rn1;|Ab1irns|N`'
        '6oFr$dh4c-a*>KcjA6vhi%f}O#-m<V@FCCVxAmsq7lohjY*@tAqmMy&7^uQeWyGuao!Pr5RuE3>9>Kk1yoEdZTXkB^-tkotWKobu'
        'uApzqe*D_()+py=Axq^Kd6218D71!;mV-&@$WKL>OT|N(Mb+$8KaycJ`|o+o84h8Sm}jhje<!E+Kkq%gIAbtR1w*(KC}u<!1&`Pu'
        'mnn@5%RJ{<!A5025h~{S4ig!3mQh`=H-Mo+)xzMX9S)LYPJ#v^R|ToD!{Cw_&{ex1=I)2INo5XN$3f=Fj5EC!3x;w>uQfmqG8G3&'
        '!up(j$#dDQz(#M)ZXC%BEm+hpiEqa5nqNP8bR+(0{NAH2G<E#`Kgg=@9v?pQPcA-v+&elv?>&9upWHv~J-t`OAIzdJ^vch@6Wmcq'
        'pkyOJhKyK(j)eUmvJ||?b5KW?pj9Rd7J}wzio)1pe&!?=31@kkWg;7PtJ&-RI7mu>*3T{Y_!XFjtT6|@8>b{ENbKg~&g=(+JP7fs'
        'g8L85Z@52uWxv90sy^)UmupP%p*6xU$N*;#@1OeTz2o~&FV2k_{Nszq=e?81z58IX51t)-Z)<BINSR84F;~s@^Ay}NWojadFlL2h'
        '0n7NrTFJQHBFkJwpDVCRR(KjRxd=H86cA-O*a!SvOt?XC&O<(;#ibUP1PHH*v?z2j*q?$Uy50kj%da3z62PEHgQ3U>VnrjsjR#x;'
        'j1H*N11N-^?Jx+=dF+}=-r7m6XRO2ax*r)BtM-8wpuqrWcJ9^kb3V`^z?<OnP@F6aoYQh9u@BkpHoMFAn@e3rVF_YrGg)nz<=D1<'
        '$vg_JAeALtMY~e8Vu%?JPXzw1y$_;A5re`K7pgsp*HC`OuZm7AhIlUnj_dU9bpf#Po<VN>(d?DmHAMOBro-fZf2z|1LY2jD$G75N'
        '#dqW1m%y(P2h&49@u>P{_Le^oS3L4ZGB11)RmWTJ&EEEvEc1}Vt%Uod0QhsJc4L|H-4a-R7Yz#pzN-_@c)ugEK~i2t{mvwZl$G!5'
        'ko9vuEE8O($q&j*+C|&!{%-%bA1|h??tXW#s|P`<@Z&&%254tYC}RM1^$moP*xuTD0(h4BWoIHH0~ECoSjJ^QG1-(%sNrhypjgfP'
        'fH>6A#vp7{^CXD{C;<+#5CnO3GFV(INQM%2AEyYeexN|2)Uk$2dfPpWn-ul|lm!8OPblN7h&==!cTTyINlBtkd60C@agn1$hL@lX'
        '&OuQ}hfg}6mTDVA^0>=B<N1&$ToeTQhg}Ax0vBQ2B{hdU<2l4Vm?yAdKBpxxOANSVm?0pxDP^FQlra;<7f>&fk+B(QZsS0jw1sZ<'
        'AZCg{WL8h0iLhv_Yge!H=3Kgx^Z5@G!b)GcIdV=np|p!~uqCo3#30*V4G0Rc?HzA|kxg-3Z`X}WP*&tDMC+?2AWeV*8W-1Fy_$~t'
        'Z9vUa01qfdqYxXYau`DikO7lIwhJ;$dXR{9-iuIXA`vJGnK0o<uIMH*jKNi=@lV?~snF|zIf+c*4w7Nbp|tAqIy#dsNRwdQpdfjN'
        '88H2*&cD`G!q`k$j?^}ZN+`Utf^D$9)@iC)5z7xx#~O?Wx@vSap_VsM0c!$t@hn2lH6|b&A$3szP_+<G6~Y4Y(G;sKh%g%nh!nCl'
        '8X!=rOnKyi|Ii$XL@gxQ7|KSY2h7#>D$ws(P0;|Sd}A%%9d>u9ObggYdwcA%KT;T{Fk9_-#nK)q$2#?2yUWfATUR12Qx=4fR)UZ~'
        '9fYyqW2~QHS=4^8uxZ+(r^*rjQ<zahp?DK_7>-bG#!w7Tz(WTb8xt6#kx?&}22(Uc#D{qh@raC%3e;=?){_&Z{iJgl7|W~&n!$2V'
        '5ER;xkr)`hWG&I<V4YEn=!1ZfdD|^RMD9U|fwRcmwlFYZM$u=$lDlw1*n(2pZjFlQ0zD^3O@ippr7DncJ=h8IZjPD?OTz@pPQ(XL'
        '#ef?JZgB&7fW~RXJ17*!BvOtT`T3-GPcMSBm&+tUbv3R4%~9Kc*M=0{0#nNrni!l_*XD$#4Z%Wt8kIS;f?#n7K9Pk;Tc8YVMg)D4'
        'h+=xj17Hv?&7?piCiKbQrtUypMOJd{IXR}R>1e5I5kf?vodGixq$zGA8qz%0rj(_1bP9EeYC+g@C2~S4p;N#d<&cYseeK9eFv5I`'
        'Yz}4l5DNs%XF62=Qi7jSS`rBcX~IliLln%6BGB(3VS+9pq*i3nz8qU7S*)%A&wyH6SP>zE7_K3>9m!N=L0#N!Yp~ghZ{aQr(I*rV'
        'eafcj5F{h2iPsb*R8}@Mc7uuA&+4+2`ZY>b?3w0VZatxEde5!tX|;9L^>RJWdYLA3=&ubQyhH`+5tfSJ5;i)<WT?!@$)Z&@n~cOD'
        '<p?!Of)MeL0v`)N14Jn{GZKp`<u%RkTme4U5^3m?OLNzw3Qc2D1<)}dp_f_fC?Y5TZ(1gWz+hiaP`2pN<-n#AQ(>@}y`ugOCUvOP'
        'Jsw_9D5?-I#r4Rf%r?wyGqc*CHo#DbH}5e<y)kb7$m+LavNlpYm8TTJ`2?~6=oIlWPk`!hVVEn3vjT=vVQaYrOBO&fV788_6tJUS'
        'X&$ekXANT~fk5KmVPW<Jj?dhfPO10-Qw3vSGa?qdMOZMl*;rS`lpNtA9d)cTBUz!#9!Sh&bzP30ii={T?(AY)Q>Lc%=*oQ9Wq-m0'
        'A3Tanc)`udNxdV_LO6&bgfE~Kln*Z<(?%Vf1QtNO(W+R+0TOk`jiipo>^K|_hJ)Ru=p}5k4JVu0(<!WM>UT;zU18Jq98ADEHV+q?'
        'E(Q=~RJkSM5@U?m%Bu(MK+eO6Xl6Bw5pOqD6xKxiY6RZX1#o{pJ3||?vJm!A3KbH18uEDnjhSstYEL)&breUdE%jW52~A)TNQ^o$'
        'QMe7r%?OT>;$<X5tec^^Gc`;iha$v<gH7od84PO&T^5*<Q8h;%dXyJQuE-`C*Bf&?2}}cWl9|ec-061v%AqHudT8D((TCJ0tUB!R'
        '%m~80zGM#toqTysLlf9Y29D=B2C#1WcbKkd1NPaIvonKBI;2#<3)oLu`Kz|;tb=DzvK+?E_Vi6{dmB8sdKQ_Ij)IuL(otBR^f~mW'
        'f+{me5>%++c|s0OX7t(Jg_alTX&mGNv7^il!Y<(07ZJO2m+c*x>&*f1m2>Pn!hs00FP>Z+`@IK;NB7U3<Gio-UK}`U5gZ0(7V5*u'
        'x;1T@Vq;nb!660$?PC-{3Ub(r3ctFJuVLObYb~yEti`vSZ9(IRGkgKoyV_x?8n%~I#fk<g2_Yr2vAm>?k7ujeh??hAbJyw6oj_?C'
        '^?J3ZeLS3TP6L+)Q?5yX3l&w@*)ZXqL5`K29ROKuEb^kHq>N#sQfd+bR$X^rAl&gCP}8uadeIy~sFep0D|W3{pHRV=2!OUmb6qPe'
        'c*3Z8esykz9vSPl<{aTF*ET}FGT$$QKt~us&>dz`{K9ecNsYp~GC)F|j-VG=|6mAr%Avn>Sa$;)VVNEsnwqZJ`q_;J7h*aH=wK1d'
        '3^hH}S~_j$5{+{AJ_8yozFY@+G&3sQT4h8`1}&i@n+f&_YvLCE-@4Uy#=7(HWAO%)HyEhZK3F}kd)+f6NNXVqzt+*u7gxA`#vGT`'
        '(>8I$j@5f^KQEl$&iGrm4k(%-7zS7+)z62(UlI03p@cjXLIv3Xu?6&PQ@G9yn!7d4H`%wnJ}=vb?d5Va<%bO!;Lak|=T|;7&56Sq'
        '8aK|TCQM3Pc!0}MN4Kh3Ar*>LS-{<JjcAa1Y=`K*bUF;Hh3q$Urbnj<=1CVe-Ag%YO%hYIVYqU3et3T0zc{%EUk7aE2Xy!xEd%}d'
        'ow@Nl=HKDHKVF=j8_C*%KGw`;(a!!F!9)rf^#{86G$I`S+B|=ih;^w}ALdwm;E9p;lsPtN(ye~@vPda<`eU4kw9=wu9bcbE)k$+<'
        'bj!xg3i<*4^vQg4$W#|J5UzMi0=i(iG_{Xj?L)3c2<?NA<2(AyF~>4;JDBLZ-{CQ~8}*B3SgpYvQLKjAVj8MVSB|h*yvB5gb2Wj@'
        'DCSuN9*@==sbks9Wb|l6|Lx#8&?uRE*lx<spx79~wXh~QJMP>J9Y^u0s0Y^nb(|_UP_Jhhn=_Vf9;^|uhEg0kD@M4&mLu5CHP7_S'
        '9e2(`$l3|c<(29#(373!T;6~rO*^X!n!^wuO)K}X<7FzEMJVc&b!wg`+iJol$qfjlc%WX`ueS<8=WcP8mpa$^u_hY)VDF^BwxU3}'
        'tp%@r!uHyXN*u>CcyZ34^m>4APLI|)8s^PQpVPxs)bpnYx$itD$F_i;QqG;Mip(Wm^K__n`>H;fbStoVxsi{Ov9eub=szqgGN&`N'
        'xh=<jcrGw!3OX}iT5(fJxIkO$DkYxij=a@c5hCpFT{n>0L>;X)K7q0GPHAsa51e$09Hd(-9Z0~JE+wN{Xp=dTv&Pah?#_o^dtu<>'
        'qC_TY2)oe<+5y;iNI$shQo(AQ#+NQL-OmI<eh7=L;~e$@#M4TSy2bX}2OA`&m@hWsa`lT&t7M|tUF!iR8^xVJxMq9B{8iq#HXpm6'
        '7vARoVE>0??YZ+M694~1&_XSBaE(?NVJ{(dL%c3ZeWCZNLzhm`SGO+Csnb&Dg0BMh6IIQAZC@{I-YoPLFBbn-vmbscipTW-jMp#H'
        '&A#u;Q8i=hgs5rSmx&0g+0A2~N|V=~(h<ANn>Qq1_rq8uQ5B!fetZ%{5kP2ZQ2Y$<J}HwV$ft{U<IX>;)}xRArTViQ{zyxx9^EMW'
        'uulLazI6#df-C&-2EKV&CIRa2;cIpHbWdj0ld_L*9d-W)_*HZS%qjo?'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)