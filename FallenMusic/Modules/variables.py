# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

import config
from FallenMusic import BOT_NAME, app


@app.on_message(
    filters.command(["config", "variables"]) | filters.command(["پێویستیەکان","token","api id","كونفنج"],prefixes= ["/", "!","","#"]) & filters.user(config.OWNER_ID)
)
async def get_vars(_, message: Message):
    try:
        await app.send_message(
            chat_id=int(config.OWNER_ID),
            text=f"""<u>**{BOT_NAME} گۆڕاوەی ڕێکخستن :**</u>

**ئایبی ئایدی :** `{config.API_ID}`
**ئایبی هاش :** `{config.API_HASH}`

**تۆکن بۆت :** `{config.BOT_TOKEN}`
**سنووری ماوەی کارکردن :** `{config.DURATION_LIMIT}`

**ئایدی خاوە ن :** `{config.OWNER_ID}`
**ئایدی ئاکاونت یارمە تێدەر :** `{config.SUDO_USERS}`

**پینگ :** `{config.PING_IMG}`
**لەوە دەچێت :** `{config.START_IMG}`
**گروپی بۆت :** `{config.SUPPORT_CHAT}`

**کود تیرموکس :** `{config.SESSION}`""",
            disable_web_page_preview=True,
        )
    except:
        return await message.reply_text("⎊ شکستی هێنا لە ناردنی گۆڕاوە ڕێکخستنەکان")
    if message.chat.type != ChatType.PRIVATE:
        await message.reply_text(
            "⎊ تکایە pm ـەکەت بپشکنە من گۆڕاوە ڕێکخستنەکانم لەوێ ناردووە"
        )
