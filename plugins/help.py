from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/ZeroxTeamCh")
      ],
      [ 
        InlineKeyboardButton(
            "Group", url="https://t.me/ZeroxTeamChat")]
    ])  
    helptxt = f"<b> Just send a Youtube url to download it in video or audio format!\n\n ~ @zerothv🇯🇵 </b>"
    await message.reply_text(helptxt, reply_markup=joinButton)
