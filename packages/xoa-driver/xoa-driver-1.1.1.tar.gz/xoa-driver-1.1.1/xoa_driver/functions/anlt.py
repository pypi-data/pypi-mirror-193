from __future__ import annotations
from dataclasses import dataclass, field
import typing as t
from xoa_driver import enums
from xoa_driver.utils import apply
from xoa_driver.internals.hli_v1.ports.port_l23.family_l import FamilyL
from xoa_driver.internals.hli_v1.ports.port_l23.family_l1 import FamilyL1
from xoa_driver.ports import GenericL23Port
from xoa_driver.lli import commands
from xoa_driver.internals.core import interfaces as itf
from xoa_driver.misc import Token
from .tools import (
    get_ctx,
    dictionize_autoneg_status,
    dictionize_lt_status,
    dictionize_txtap_get,
    dictionize_anlt_status,
)

PcsPmaSupported = (FamilyL, FamilyL1)
AutoNegSupported = (FamilyL, FamilyL1)
LinkTrainingSupported = FamilyL


@dataclass
class DoAnlt:
    port: GenericL23Port
    """port to select"""
    should_do_an: bool
    """should the port do autoneg?"""
    should_do_lt: bool
    """should the port do link training?"""
    an_allow_loopback: bool
    """should the autoneg allow loopback?"""
    lt_preset0_std: bool
    """should lt preset0 uses the standard values or the existing tap values?"""
    lt_initial_modulations: dict[int, enums.LinkTrainEncoding]
    """the initial modulations of each lane (serdes)"""
    should_lt_interactive: bool
    """should perform link training manually?"""

    _group: tuple["itf.IConnection", int, int] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._group = get_ctx(self.port)

    def __pp_autoneg(self, on: bool) -> Token:
        state = enums.AutoNegMode.ANEG_ON if on else enums.AutoNegMode.ANEG_OFF
        return commands.PP_AUTONEG(*self._group).set(
            state,
            enums.AutoNegTecAbility.DEFAULT_TECH_MODE,
            enums.AutoNegFECOption.NO_FEC,
            enums.AutoNegFECOption.NO_FEC,
            enums.PauseMode.NO_PAUSE,
        )

    def __pp_link_train(
        self,
        mode: enums.LinkTrainingMode,
        nrz_preset: enums.NRZPreset,
        timeout_mode: enums.TimeoutMode,
    ) -> Token:
        return commands.PP_LINKTRAIN(*self._group).set(
            mode=mode,
            pam4_frame_size=enums.PAM4FrameSize.P16K_FRAME,
            nrz_pam4_init_cond=enums.LinkTrainingInitCondition.NO_INIT,
            nrz_preset=nrz_preset,
            timeout_mode=timeout_mode,
        )

    def __pl1_cfg_tmp(
        self, lane: int, config_type: enums.Layer1ConfigType, values: int
    ) -> Token:
        return commands.PL1_CFG_TMP(*self._group, lane, config_type).set(
            values=[int(values)]
        )

    def __select_modes(self) -> tuple[enums.LinkTrainingMode, enums.TimeoutMode]:
        if self.should_do_an:
            lt_mode = enums.LinkTrainingMode.START_AFTER_AUTONEG
            timeout_mode = enums.TimeoutMode.DEFAULT
        elif self.should_lt_interactive:
            lt_mode = enums.LinkTrainingMode.INTERACTIVE
            timeout_mode = enums.TimeoutMode.DISABLED
        else:
            lt_mode = enums.LinkTrainingMode.STANDALONE
            timeout_mode = enums.TimeoutMode.DEFAULT
        return lt_mode, timeout_mode

    def __builder__(self) -> t.Generator[Token, None, None]:
        """Defining commands sequence"""
        nrz_preset = (
            enums.NRZPreset.NRZ_WITH_PRESET
            if self.lt_preset0_std
            else enums.NRZPreset.NRZ_NO_PRESET
        )
        # # Set autoneg timeout
        yield self.__pp_link_train(
            enums.LinkTrainingMode.DISABLED,
            enums.NRZPreset.NRZ_NO_PRESET,
            enums.TimeoutMode.DEFAULT,
        )

        # # Set autoneg allow-loopback
        yield self.__pl1_cfg_tmp(
            0, enums.Layer1ConfigType.AN_LOOPBACK, int(self.an_allow_loopback)
        )

        # yield self.__pp_autoneg(self.should_do_an and not self.should_do_lt)
        if (not self.should_do_an) or self.should_do_lt:
            # Disable autoneg
            yield self.__pp_autoneg(False)

        if self.should_do_lt:
            for lane_str, im in self.lt_initial_modulations.items():
                yield self.__pl1_cfg_tmp(
                    int(lane_str), enums.Layer1ConfigType.LT_INITIAL_MODULATION, int(im)
                )

            lt_mode, timeout_mode = self.__select_modes()
            yield self.__pp_link_train(
                enums.LinkTrainingMode.DISABLED, nrz_preset, timeout_mode
            )
            yield self.__pp_link_train(lt_mode, nrz_preset, timeout_mode)

        if self.should_do_an:
            yield self.__pp_autoneg(True)

    async def run(self) -> None:
        """Start anlt execution"""
        await apply(*self.__builder__())


async def anlt_start(
    port: GenericL23Port,
    should_do_an: bool,
    should_do_lt: bool,
    an_allow_loopback: bool,
    lt_preset0_std: bool,
    lt_initial_modulations: dict[int, enums.LinkTrainEncoding],
    should_lt_interactive: bool,
) -> None:
    """Start ANLT on a port

    :param port: port to select
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param should_do_an: should the port do autoneg?
    :type should_do_an: bool
    :param should_do_lt: should the port do link training?
    :type should_do_lt: bool
    :param an_allow_loopback: should the autoneg allow loopback?
    :type an_allow_loopback: bool
    :param lt_preset0_std: should lt preset0 uses the standard values or the existing tap values?
    :type lt_preset0_std: bool
    :param lt_initial_modulations: the initial modulations of each lane (serdes)
    :type lt_initial_modulations: Dict[str, enums.LinkTrainEncoding]
    :param should_lt_interactive: should perform link training manually?
    :type should_lt_interactive: bool
    """

    anlt = DoAnlt(
        port,
        should_do_an,
        should_do_lt,
        an_allow_loopback,
        lt_preset0_std,
        lt_initial_modulations,
        should_lt_interactive,
    )
    await anlt.run()


async def autoneg_status(port: GenericL23Port) -> dict[str, t.Any]:
    """Get the auto-negotiation status

    :param port: the port to get auto-negotiation status
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :return:
    :rtype: typing.Dict[str, Any]
    """
    conn, mid, pid = get_ctx(port)
    loopback, auto_neg_info = await apply(
        commands.PL1_CFG_TMP(
            conn, mid, pid, 0, enums.Layer1ConfigType.AN_LOOPBACK
        ).get(),
        commands.PL1_AUTONEGINFO(conn, mid, pid, 0).get(),
    )
    return dictionize_autoneg_status(loopback, auto_neg_info)


LinkTrainType = t.Union[
    enums.LinkTrainCoeffs,
    enums.LinkTrainPresets,
    enums.LinkTrainEncoding,
    enums.LinkTrainAnnounce,
]


async def __lt_coeff(
    port: GenericL23Port,
    lane: int,
    arg: LinkTrainType,
    *,
    cmd: enums.LinkTrainCmd,
) -> None:
    conn, mid, pid = get_ctx(port)
    cmd_ = commands.PL1_LINKTRAIN_CMD(conn, mid, pid, lane)
    await cmd_.set(cmd=cmd, arg=arg.value)
    return None


async def lt_coeff_inc(
    port: GenericL23Port, lane: int, emphasis: enums.LinkTrainCoeffs
) -> None:
    """Ask the remote port to increase coeff of the specified lane.

    :param port: The port to configure
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param lane: The lane index, starting from 0
    :type lane: int
    :param emphasis: The emphasis to increase
    :type emphasis: enums.LinkTrainCoeffs
    :return:
    :rtype: None
    """
    return await __lt_coeff(port, lane, emphasis, cmd=enums.LinkTrainCmd.CMD_INC)


async def lt_coeff_dec(
    port: GenericL23Port, lane: int, emphasis: enums.LinkTrainCoeffs
) -> None:
    """Ask the remote port to decrease coeff of the specified lane.

    :param port: The port to configure
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param lane: The lane index, starting from 0
    :type lane: int
    :param emphasis: The emphasis to decrease
    :type emphasis: enums.LinkTrainCoeffs
    :return:
    :rtype: None
    """
    return await __lt_coeff(port, lane, emphasis, cmd=enums.LinkTrainCmd.CMD_DEC)


async def lt_preset(
    port: GenericL23Port, lane: int, preset: enums.LinkTrainPresets
) -> None:
    """Ask the remote port to use the preset of the specified lane.

    :param port: The port to configure
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param lane: The lane index, starting from 0
    :type lane: int
    :param preset: preset index to select for the lane, 0,1,2,3,4,
    :type preset: enums.LinkTrainPresets
    :return:
    :rtype: None
    """
    return await __lt_coeff(port, lane, preset, cmd=enums.LinkTrainCmd.CMD_PRESET)


async def lt_encoding(
    port: GenericL23Port, lane: int, encoding: enums.LinkTrainEncoding
) -> None:
    """Ask the remote port to use the encoding of the specified lane.

    :param port: The port to configure
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param lane: The lane index, starting from 0
    :type lane: int
    :param encoding: link training encoding
    :type encoding: enums.LinkTrainCoeffs
    :return:
    :rtype: None
    """

    """
    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param lane: lane index, starting from 0
    :type lane: int
    
    """
    return await __lt_coeff(port, lane, encoding, cmd=enums.LinkTrainCmd.CMD_ENCODING)


async def lt_trained(port: GenericL23Port, lane: int) -> None:
    """Tell the remote port that the current lane is trained.

    :param port: The port to configure
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param lane: The lane index, starting from 0
    :type lane: int
    :return:
    :rtype: None
    """
    return await __lt_coeff(
        port,
        lane,
        arg=enums.LinkTrainAnnounce.TRAINED,
        cmd=enums.LinkTrainCmd.CMD_LOCAL_TRAINED,
    )


async def lt_status(port: GenericL23Port, lane: int) -> dict[str, t.Any]:
    """Show the link training status.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param lane: lane index, starting from 0
    :type lane: int
    :return:
    :rtype: str
    """
    conn, mid, pid = get_ctx(port)
    status, info, ltconf, cfg = await apply(
        commands.PP_LINKTRAINSTATUS(conn, mid, pid, lane).get(),
        commands.PL1_LINKTRAININFO(conn, mid, pid, lane, 0).get(),
        commands.PP_LINKTRAIN(conn, mid, pid).get(),
        commands.PL1_CFG_TMP(
            conn, mid, pid, lane, enums.Layer1ConfigType.LT_INITIAL_MODULATION
        ).get(),
    )
    total_bit_count = (info.prbs_total_bits_high << 32) + info.prbs_total_bits_low
    total_error_bit_count = (
        info.prbs_total_error_bits_high << 32
    ) + info.prbs_total_error_bits_low
    prbs = (
        total_error_bit_count / total_bit_count if total_bit_count > 0 else float("nan")
    )
    return dictionize_lt_status(
        status, info, ltconf, cfg, prbs, total_bit_count, total_error_bit_count
    )


async def txtap_get(port: GenericL23Port, lane: int) -> dict[str, int]:
    """Get the tap value of the local TX tap.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param lane: lane index, starting from 0
    :type lane: int
    :return:
    :rtype: typing.Dict[str, Any]
    """
    conn, mid, pid = get_ctx(port)
    r = await commands.PP_PHYTXEQ(conn, mid, pid, lane).get()
    return dictionize_txtap_get(r)


async def txtap_set(
    port: GenericL23Port,
    lane: int,
    pre3: int,
    pre2: int,
    pre: int,
    main: int,
    post1: int,
) -> None:
    """Set the tap value of the local TX tap.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param lane: lane index, starting from 0
    :type lane: int
    :param pre3: pre3 value
    :type pre3: int
    :param pre2: pre2 value
    :type pre2: int
    :param pre: pre value
    :type pre: int
    :param main: main value
    :type main: int
    :param post1: post1 value
    :type post1: int
    :return:
    :rtype: None
    """
    conn, mid, pid = get_ctx(port)
    cmd_ = commands.PP_PHYTXEQ(conn, mid, pid, lane)
    await cmd_.set(
        pre1=pre,
        main=main,
        post1=post1,
        pre2=pre2,
        post2=pre3,
        post3=0,
    )


async def anlt_link_recovery(port: GenericL23Port, enable: bool) -> None:
    """Should xenaserver automatically do link recovery when detecting down signal.

    :param port: port to configure
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :param enable: Should xenaserver automatically do link recovery when detecting down signal.
    :type enable: bool
    :return:
    :rtype:  None
    """
    conn, mid, pid = get_ctx(port)
    cmd_ = commands.PL1_CFG_TMP(
        conn, mid, pid, 0, enums.Layer1ConfigType.ANLT_INTERACTIVE
    )
    await cmd_.set(values=[int(enable)])


async def anlt_status(port: GenericL23Port) -> dict[str, t.Any]:
    """Get the overview of ANLT status

    :param port: the port to get ANLT status from
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :return: ANLT overview status
    :rtype: typing.Dict[str, Any]
    """

    # if not isinstance(port, LinkTrainingSupported):
    #     raise NotSupportLinkTrainError(port)
    conn, mid, pid = get_ctx(port)
    r = await apply(
        commands.PL1_CFG_TMP(
            conn, mid, pid, 0, enums.Layer1ConfigType.ANLT_INTERACTIVE
        ).get(),
        commands.PP_AUTONEGSTATUS(conn, mid, pid).get(),
        commands.PP_LINKTRAIN(conn, mid, pid).get(),
        commands.P_CAPABILITIES(conn, mid, pid).get(),
    )
    link_recovery, autoneg, linktrain, capabilities = r
    return dictionize_anlt_status(link_recovery, autoneg, linktrain, capabilities)


async def anlt_log(port: GenericL23Port) -> str:
    """Get the anlt log messages

    :param port: the port object
    :type port: :class:`~xoa_driver.ports.GenericL23Port`
    :return: anlt log
    :rtype: str
    """
    conn, mid, pid = get_ctx(port)
    log = await commands.PL1_LOG(conn, mid, pid).get()
    return log.log_string


__all__ = (
    "anlt_log",
    "anlt_start",
    "lt_coeff_inc",
    "lt_coeff_dec",
    "lt_encoding",
    "lt_preset",
    "lt_status",
    "lt_trained",
    "autoneg_status",
    "anlt_link_recovery",
    "anlt_status",
    "txtap_get",
    "txtap_set",
)
