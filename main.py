from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os
import asyncio
import threading
from fastapi import FastAPI
import uvicorn

BOT_TOKEN = os.getenv("BOT_TOKEN")

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Bot is running fine!"}

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hey there! I’m the official bot of **YouTube 1K Boosters 🚀**.\n\n"
        "Join our mission to help creators reach their **first 1,000 subscribers** faster!\n\n"
        "💡 How it works:\n"
        "1️⃣ Subscribe to 20 member channels\n"
        "2️⃣ Send your proof in the group for verification\n"
        "3️⃣ Once verified, your channel gets shared next 🎯\n\n"
        "Let’s grow together 💪🔥",
        parse_mode=ParseMode.MARKDOWN
    )

# Triggered when a new member joins
async def new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            f"🎉 Welcome **{member.first_name}!**\n\n"
            "You’ve joined **YouTube 1K Boosters Verification 🔰** — "
            "a growing community helping creators hit **1K subscribers faster!**\n\n"
            "✅ Step 1: Subscribe to 20 channels from the pinned post\n"
            "📸 Step 2: Share your screenshot here for verification\n"
            "🚀 Step 3: Get your own channel shared next!\n\n"
            "Let’s grow together ❤️‍🔥",
            parse_mode=ParseMode.MARKDOWN
        )


async def main_bot():
    # Initialize app
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_member))
    print("🤖 Telegram bot started...")
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    # Keep it running
    await asyncio.Event().wait()


def run_bot():
    """Runs the Telegram bot in its own independent event loop."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main_bot())


if __name__ == "__main__":
    # Run bot in separate thread
    threading.Thread(target=run_bot, daemon=True).start()

    # Start FastAPI server (Render will bind to this)
    uvicorn.run(app, host="0.0.0.0", port=10000)