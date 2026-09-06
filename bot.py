import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    parameter = context.args[0] if context.args else None

    if parameter == "ep20":
        await update.message.reply_text(
            "قسمت ۲۰ «این دریا طغیان می‌کند»\n\n"
            "ربات آماده دریافت فایل‌های قسمت ۲۰ است. ❤️"
        )
    else:
        await update.message.reply_text(
            "سلام! 👋\n"
            "به TurkMovies Download خوش اومدی."
        )


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is not set")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
