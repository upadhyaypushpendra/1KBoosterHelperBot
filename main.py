from telegram import Update, ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

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

# Initialize app
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_member))

if __name__ == "__main__":
    print("🤖 Bot is running...")
    app.run_polling()
