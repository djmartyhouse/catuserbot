import asyncio
import re
from telethon.errors import FloodWaitError
from telethon import events
from telethon.tl import functions, types
from ..helpers import get_user_from_event, reply_id
from . import catub, edit_or_reply, mention
from . import (
    _catutils,
    catub,
    edit_delete,
    logging,
)
from userbot import catub
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID
from . import BOTLOG, BOTLOG_CHATID


@catub.cat_cmd(
    pattern="ss(?:\s|$)([\s\S]*)",
    command=("ss", "tools"),
    info={
        "header": "Manda sticker",
        "description": "Cambia sticker",
        "usage": "{tr}ms",
    },
)
async def cambia(ss):
        stickers = await ss.client(GetStickerSetRequest(
        stickerset=InputStickerSetID(id=6429567493810946050,
        access_hash=8359541497365493484)
        ))
        await edit_delete(ss, f"**STO PER SPAMMARE 106 STICKER, GODO.**")
        await ss.client.send_message(BOTLOG_CHATID,"Spam sticker avviato con successo!! ")
        replyI = await reply_id(ss)
        for x in stickers.documents:
            await ss.client.send_file(
                    ss.chat_id,
                    x,reply_to=replyI)
