from typing import Sequence

from trezor import ui, wire
from trezor.enums import ButtonRequestType
from trezor.lvglui.i18n import gettext as _, keys as i18n_keys
from trezor.lvglui.lv_colors import lv_colors
from trezor.ui.layouts import confirm_blob, show_success, show_warning
from trezor.ui.layouts.lvgl.common import interact
from trezor.ui.layouts.lvgl.reset import (  # noqa: F401
    confirm_word,
    show_share_words,
    slip39_advanced_prompt_group_threshold,
    slip39_advanced_prompt_number_of_groups,
    slip39_prompt_number_of_shares,
    slip39_prompt_threshold,
    slip39_show_checklist,
)


async def show_internal_entropy(ctx: wire.GenericContext, entropy: bytes) -> None:
    await confirm_blob(
        ctx,
        "entropy",
        "Internal entropy",
        data=entropy,
        icon=ui.ICON_RESET,
        icon_color=ui.ORANGE_ICON,
        br_code=ButtonRequestType.ResetDevice,
    )


async def _confirm_share_words(
    ctx: wire.GenericContext,
    share_index: int | None,
    share_words: Sequence[str],
    group_index: int | None = None,
) -> bool:
    # # divide list into thirds, rounding up, so that chunking by `third` always yields
    # # three parts (the last one might be shorter)
    # third = (len(share_words) + 2) // 3

    count = len(share_words)
    for index in range(count):
        if not await confirm_word(
            ctx, share_index, share_words, index, count, group_index
        ):
            return False

    return True


async def _show_confirmation_success(
    ctx: wire.GenericContext,
    share_index: int | None = None,
    num_of_shares: int | None = None,
    group_index: int | None = None,
) -> None:
    if share_index is None or num_of_shares is None:  # it is a BIP39 backup
        subheader = _(i18n_keys.SUBTITLE__DEVICE_BACKUP_VERIFIED_SUCCESS)
        text = _(i18n_keys.TITLE__VERIFIED)

    elif share_index == num_of_shares - 1:
        if group_index is None:
            subheader = "You have finished\nverifying your\nrecovery shares."
        else:
            subheader = f"You have finished\nverifying your\nrecovery shares\nfor group {group_index + 1}."
        text = ""

    else:
        if group_index is None:
            subheader = f"Recovery share #{share_index + 1}\nchecked successfully."
            text = f"Continue with share #{share_index + 2}."
        else:
            subheader = f"Group {group_index + 1} - Share {share_index + 1}\nchecked successfully."
            text = "Continue with the next\nshare."

    return await show_success(
        ctx,
        "success_recovery",
        subheader,
        header=text,
        button=_(i18n_keys.BUTTON__CONTINUE),
    )


async def _show_confirmation_failure(
    ctx: wire.GenericContext, share_index: int | None
) -> None:
    if share_index is None:
        header = _(i18n_keys.TITLE__INCORRECT_WORD)
    else:
        header = f"Recovery share #{share_index + 1}"
    await show_warning(
        ctx,
        "warning_backup_check",
        header=header,
        subheader="",
        icon="A:/res/danger.png",
        content=_(i18n_keys.SUBTITLE__DEVICE_BACKUP_INCORRECT_WORD),
        button=_(i18n_keys.BUTTON__TRY_AGAIN),
        br_code=ButtonRequestType.ResetDevice,
        btn_yes_bg_color=lv_colors.CHARGERWALLET_BLACK_1,
    )


async def show_backup_warning(ctx: wire.GenericContext, slip39: bool = False) -> None:
    # if slip39:
    #     description = "Never make a digital copy of your recovery shares and never upload them online!"
    # else:
    #     description = "Never make a digital copy of your recovery seed and never upload\nit online!"
    # if utils.LVGL_UI:
    #     icon = "A:/res/warning.png"
    #     description = "Never make a digital copy of your recovery seed and never upload it online!"
    # else:
    #     icon = ui.ICON_NOCOPY
    # await confirm_action(
    #     ctx,
    #     "backup_warning",
    #     "Caution",
    #     description=description,
    #     verb="I understand",
    #     verb_cancel=None,
    #     icon=icon,
    #     br_code=ButtonRequestType.ResetDevice,
    # )
    # TODO: support slip39
    from trezor.lvglui.scrs.reset_device import BackupTips

    screen = BackupTips()
    await interact(ctx, screen, "backup_warning", ButtonRequestType.ResetDevice)


async def show_backup_success(ctx: wire.GenericContext) -> None:
    text = _(i18n_keys.SUBTITLE__DEVICE_BACKUP_BACK_UP_COMPLETE)
    await show_success(
        ctx,
        "success_backup",
        text,
        header=_(i18n_keys.TITLE__WALLET_IS_READY),
        button=_(i18n_keys.BUTTON__CONTINUE),
    )


async def show_check_word_tips(ctx):
    from trezor.lvglui.scrs.common import FullSizeWindow

    screen = FullSizeWindow(
        title=_(i18n_keys.TITLE__SETUP_CREATE_ALMOST_DONE),
        subtitle=_(i18n_keys.SUBTITLE__SETUP_CREATE_ALMOST_DOWN),
        confirm_text=_(i18n_keys.BUTTON__CONTINUE),
        cancel_text=_(i18n_keys.BUTTON__BACK),
        anim_dir=0,
    )
    result = await interact(
        ctx, screen, "check_word_tips", ButtonRequestType.ProtectCall
    )
    if not result:
        raise wire.ActionCancelled()


# BIP39
# ===


async def bip39_show_and_confirm_mnemonic(
    ctx: wire.GenericContext, mnemonic: str
) -> None:
    # warn user about mnemonic safety
    await show_backup_warning(ctx)
    words = mnemonic.split()

    while True:
        # display paginated mnemonic on the screen
        await show_share_words(ctx, share_words=words)
        try:
            await show_check_word_tips(ctx)
        except wire.ActionCancelled:
            continue
        # make the user confirm some words from the mnemonic
        if await _confirm_share_words(ctx, None, words):
            await _show_confirmation_success(ctx)
            break  # this share is confirmed, go to next one
        else:
            await _show_confirmation_failure(ctx, None)


# SLIP39
# ===


async def slip39_basic_show_and_confirm_shares(
    ctx: wire.GenericContext, shares: Sequence[str]
) -> None:
    # warn user about mnemonic safety
    await show_backup_warning(ctx, slip39=True)

    for index, share in enumerate(shares):
        share_words = share.split(" ")
        while True:
            # display paginated share on the screen
            await show_share_words(ctx, share_words, index)
            # description before check word
            await show_check_word_tips(ctx)
            # make the user confirm words from the share
            if await _confirm_share_words(ctx, index, share_words):
                await _show_confirmation_success(
                    ctx, share_index=index, num_of_shares=len(shares)
                )
                break  # this share is confirmed, go to next one
            else:
                await _show_confirmation_failure(ctx, index)


async def slip39_advanced_show_and_confirm_shares(
    ctx: wire.GenericContext, shares: Sequence[Sequence[str]]
) -> None:
    # warn user about mnemonic safety
    await show_backup_warning(ctx, slip39=True)

    for group_index, group in enumerate(shares):
        for share_index, share in enumerate(group):
            share_words = share.split(" ")
            while True:
                # display paginated share on the screen
                await show_share_words(ctx, share_words, share_index, group_index)

                # make the user confirm words from the share
                if await _confirm_share_words(
                    ctx, share_index, share_words, group_index
                ):
                    await _show_confirmation_success(
                        ctx,
                        share_index=share_index,
                        num_of_shares=len(group),
                        group_index=group_index,
                    )
                    break  # this share is confirmed, go to next one
                else:
                    await _show_confirmation_failure(ctx, share_index)
