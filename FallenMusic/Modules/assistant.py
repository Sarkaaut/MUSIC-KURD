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
from pyrogram.types import Message

from FallenMusic import ASS_MENTION, LOGGER, SUDOERS, app, app2


@app.on_message(filters.command(["asspfp", "setpfp"]) | filters.command(["وينه","وێنە"],prefixes= ["/", "!","","#"]) & SUDOERS)
async def set_pfp(_, message: Message):
    if message.reply_to_message.photo:
        fuk = await message.reply_text("⎊ وێنەی ئەکاونتی یاریدەدەرەکە دەگۆڕدرێت")
        img = await message.reply_to_message.download()
        try:
            await app2.set_profile_photo(photo=img)
            return await fuk.edit_text(
                f"⎊ {ASS_MENTION} وێنەی ئەکاونتی یاریدەدەر گۆڕاوە"
            )
        except:
            return await fuk.edit_text("⎊ شکستی هێنا لە گۆڕینی وێنەی ئەکاونتی یاریدەدەر")
    else:
        await message.reply_text(
            "⎊ پیویستە ریپلە ی وێنە کە بکە یت"
        )


@app.on_message(filters.command(["delete", "Delete a photo"]) & SUDOERS)
async def set_pfp(_, message: Message):
    try:
        pfp = [p async for p in app2.get_chat_photos("me")]
        await app2.delete_profile_photos(pfp[0].file_id)
        return await message.reply_text(
            "⎊ وێنەی ئەکاونتی یاریدەدەر لابرا"
        )
    except Exception as ex:
        LOGGER.error(ex)
        await message.reply_text("⎊ شکستی هێنا لە سڕینەوەی وێنەکە")


@app.on_message(filters.command(["Bayou", "Bayou status"]) & SUDOERS)
async def set_bio(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            newbio = msg.text
            await app2.update_profile(bio=newbio)
            return await message.reply_text(
                f"⎊ {ASS_MENTION} بایۆکە گۆڕاوە"
            )
    elif len(message.command) != 1:
        newbio = message.text.split(None, 1)[1]
        await app2.update_profile(bio=newbio)
        return await message.reply_text(f"⎊ {ASS_MENTION} بایۆکە گۆڕاوە")
    else:
        return await message.reply_text(
            "⎊ ریپلە ی شتیک بکە بۆ بایۆ"
        )


@app.on_message(filters.command(["name", "name mode"]) & SUDOERS)
async def set_name(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            name = msg.text
            await app2.update_profile(first_name=name)
            return await message.reply_text(
                f"⎊ {ASS_MENTION} ناوەکە گۆڕاوە"
            )
    elif len(message.command) != 1:
        name = message.text.split(None, 1)[1]
        await app2.update_profile(first_name=name, last_name="")
        return await message.reply_text(f"⎊ {ASS_MENTION} ناوەکە گۆڕاوە‌‌‌")
    else:
        return await message.reply_text(
            "⎊ ریپلە ی ناوە کە بکە"
        )
