# bot_b.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if args:
        file_id = args[0]
        await update.message.reply_text("🎥 Showing your media...")

        # Try sending video first, fallback to photo
        try:
            await update.message.reply_video(video=file_id)
        except:
            try:
                await update.message.reply_photo(photo=file_id)
            except:
                await update.message.reply_text("❌ Couldn't load media from file_id.")
    else:
        await update.message.reply_text("🤷‍♂️ No media ID provided in the link.")

app = ApplicationBuilder().token("7956658585:AAEu1b5zrEfNJnbWfMV5h036ivi21nzwaME").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
