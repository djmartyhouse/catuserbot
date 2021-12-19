from telethon.sync import TelegramClient, events
from userbot import catub
plugin_category = "utils"
id_chat = []
    @catub.cat_cmd(
        pattern=".save",
        command=("gpic", plugin_category),
        info={
            "header": "For changing group display pic or deleting display pic",
            "description": "Reply to Image for changing display picture",
            "flags": {
                "-s": "To set group pic",
                "-d": "To delete group pic",
            },
            "usage": [
                "{tr}gpic -s <reply to image>",
                "{tr}gpic -d",
            ],
        },
        groups_only=True,
        require_admin=True,
    )
    async def handler(event, controllo=1):
        chat1 = event.chat_id
        await event.delete()
        for x in id_chat:
            if x == chat1:
                controllo = 0
                break
        if controllo:
            indice = len(id_chat)
            id_chat.insert(indice, chat1)
        print(id_chat)


    @catub.cat_cmd(
        pattern=".spam",
        command=("gpic", plugin_category),
        info={
            "header": "For changing group display pic or deleting display pic",
            "description": "Reply to Image for changing display picture",
            "flags": {
                "-s": "To set group pic",
                "-d": "To delete group pic",
            },
            "usage": [
                "{tr}gpic -s <reply to image>",
                "{tr}gpic -d",
            ],
        },
        groups_only=True,
        require_admin=True,
    )
    async def handler(event):
        await event.delete()
        for x in id_chat:
            await client.send_message(x, 'si no fesso')


    client.run_until_disconnected()
# Remember to use your own values from my.telegram.org!
