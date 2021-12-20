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

async def savebot(ss, controllo=1,id_chat=[]):
    chat1 = ss.chat_id
    await edit_delete(ss, f"id chat spam salvato")
    for x in id_chat:
        if x == chat1:
            controllo = 0
            break
    if controllo:
        indice = len(id_chat)
        id_chat.insert(indice, chat1)
    print(id_chat)
    
    
    
@catub.cat_cmd(
    pattern="spambot(?:\s|$)([\s\S]*)",
    command=("spambot", "tools"),
    info={
        "header": "Manda sticker",
        "description": "Cambia sticker",
        "usage": "{tr}ms",
    },
)
async def spambot(ss, id_chat):
    print (id_chat)
    await edit_delete(ss, f"spam avviato")
    for x in id_chat:
        
        await client.send_message(x, 'si no fesso')
    

