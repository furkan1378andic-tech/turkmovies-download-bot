import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.environ.get("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("START UPDATE RECEIVED", flush=True)

    parameter = context.args[0] if context.args else None

    if parameter == "ep20":
        await update.message.reply_text(
            "قسمت ۲۰ «این دریا طغیان می‌کند»\n\n"
            "ربات آماده دریافت فایل‌های قسمت ۲۰ است. 🩵"
        )
    else:
        await update.message.reply_text(
            "سلام! 👋\n"
            "به TurkMovies Download خوش اومدی."
        )


async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    if update.message.video:
        file_id = update.message.video.file_id
        print(f"VIDEO_FILE_ID: {file_id}", flush=True)

    elif update.message.document:
        file_id = update.message.document.file_id
        print(f"DOCUMENT_FILE_ID: {file_id}", flush=True)


async def any_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("MESSAGE UPDATE RECEIVED", flush=True)


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is not set")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(
            filters.VIDEO | filters.Document.ALL,
            get_file_id
        )
    )

    app.add_handler(
        MessageHandler(filters.ALL, any_message)
    )

    print("Bot is running...", flush=True)

    app.run_polling(
        drop_pending_updates=True
    )


if __name__ == "__main__":
    main()
