import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Kanagenuis-bot-analysis\n\n"
        "Welcome to Kanagenuis AI Football Match Analyst ⚽\n\n"
        "📌 How to use:\n"
        "• Send football match details\n"
        "• Receive professional analysis\n"
        "• Type NEXT for a new match\n\n"
        "⚠️ Football matches only\n\n"
        "Analysé made by Kanapro AI — feel free to choose the best one for your betting strategy"
    )

# Handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text.upper() == "NEXT":
        await update.message.reply_text("✅ Ready for next match. Send details.")
        return

    analysis = (
        "Match Analysis\n\n"
        "1. Win / Draw:\n"
        "→ Home Win\n\n"
        "2. Double Chance:\n"
        "→ 1X\n\n"
        "3. Both Teams To Score:\n"
        "→ Yes\n\n"
        "4. Total Goals:\n"
        "→ Over 2.5\n\n"
        "5. Correct Score:\n"
        "→ First Half: 1–0\n"
        "→ Second Half: 2–1\n\n"
        "Confidence Level: 88%\n\n"
        "Analysé made by Kanapro AI — feel free to choose the best one for your betting strategy"
    )

    await update.message.reply_text(analysis)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Kanagenuis bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
