from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup 

async def pyro_fsub(c, message, fsub):
    try:
        user = await c.get_chat_member(fsub, message.chat.id)
        if user.status == "kicked":
            await c.send_message(
                chat_id=message.chat.id,
                text=" عذراً لكنك محظور ",
                parse_mode="markdown",
                disable_web_page_preview=True,
            )
        return True
    except UserNotParticipant:
        await c.send_message(
            chat_id=message.chat.id,
            text="عذراً لكن ينبغي أن تشترك في قناتي أولاً لكي تستعمل البوت ",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("انضم الآن", url=f"t.me/{fsub}")]]
            ),
        )
        return False

