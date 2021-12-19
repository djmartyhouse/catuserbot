
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

id_chat=[]
@catub.cat_cmd(
    pattern=".savespam",
    command=("savespam", "tools"),
    info={
        "header": "Manda sticker",
        "description": "Cambia sticker",
        "usage": "{tr}ms",
    },
)
async def cambia(event, controllo=1):
        chat1 = event.chat_id
        
        await edit_delete(event, f".savespam")
        for x in id_chat:
            if x == chat1:
                controllo = 0
                break
        if controllo:
            indice = len(id_chat)
            id_chat.insert(indice, chat1)
        await event.client.send_message(chat1,f"id_chat")

