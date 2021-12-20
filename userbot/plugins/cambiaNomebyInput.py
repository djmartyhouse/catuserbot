import asyncio
import re
from telethon.errors import FloodWaitError
from telethon import events
from telethon.tl import functions, types

from . import (
    _catutils,
    catub,
    edit_delete,
    logging,
)

from userbot import catub

LOGS = logging.getLogger(__name__)

@catub.cat_cmd(
    pattern="cambian",
    command=("cambian", "tools"),
    info={
        "header": "Cambia il nome a seconda del valore che hai inserito",
        "description": "Aggiorna il tuo nome",
        "usage": "{tr}cambian",
    },
)
async def cambia(nomei):
    "Scrivi un nome."
    if nomei.message.message == ".cambian":
      await edit_delete(nomei,"`Devi inserire il nome che vorresti cambiare, stronzo.\nEsempio .cambian sei uno stronzo`")
    else:
     nome = nomei.message.message.replace(".cambian ", "")
     LOGS.info(nome)
     await catub(functions.account.UpdateProfileRequest(first_name=nome))
     await nomei.edit("`Sto cambiando il nome... `")
     await asyncio.sleep(10)
     await edit_delete(nomei, "`Nome cambiato con successo --> Kill u X_X`")
     ss = await borg.send_message(-657785913, f"~Nome cambiato con successo!!~") #ss avrà dati 'json' dove ci sarà l'id del messaggio, la data e altre informazioni a riguardo
     await asyncio.sleep(60)
     await ss.delete()
