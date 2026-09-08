from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Cloud AI Agent شغال!\n\n"
        "ابعتلي أي رسالة للتجربة."
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"وصلتني رسالتك:\n{update.message.text}"
    )


def main():
    TOKEN = "PUT_YOUR_TELEGRAM_TOKEN_HERE"

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        __import__("telegram.ext", fromlist=["MessageHandler"]).MessageHandler(
            __import__("telegram.ext", fromlist=["filters"]).filters.TEXT
            & ~__import__("telegram.ext", fromlist=["filters"]).filters.COMMAND,
            echo,
        )
    )

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
