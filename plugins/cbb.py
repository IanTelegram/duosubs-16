# (Β©)Codexbotz
# Recode by @mrismanaziz
# Recode by @RYUUSHINNI

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import CHANNEL, GROUP, OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>Tentang Bot ini:\n\n β’ π½πΌπΎπΌ πππππ πππππ >: @Doujindesukomik\n β’ πΎππΌππππ ππΌππ πππππππ >: @RareCollectionID\n β’ πππππππ ππππΌπ >: @LokalPrideid\n β’ πππΏππ ππππΌπ >: <a href='https://t.me/viralbelatungid'>Klik Disini</a></b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("β’ α΄α΄α΄α΄α΄ β’", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
