from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage(tgbot):
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/cbe826936d4de9ec1838a.jpg",
                caption="✨ **ALBY-Userbot Berhasil Diaktifkan**!!\n╭╼┅━━━━━╍━━━━━┅╾\n├▹ ᴀʟʙʏ Vᴇʀsɪᴏɴ - {} •[{}]•\n├▹ Usᴇʀʙᴏᴛ Vᴇʀsɪᴏɴ - {}/n├▹ @{}/n├▹ **Ketik** `.ping` **Untuk Mengecek Bot**\n├▹ **Ketik** `.help` **Untuk Melihat Informasi Module**\n╰╼┅━━━━━╍━━━━━┅╾\n➠ **Powered By:** @ruangprojects ",
                buttons=[(Button.url("ɢʀᴏᴜᴘ ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/ruangdiskusikami"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
