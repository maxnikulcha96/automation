import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from framework.web.browsers import FirefoxBrowser
from framework.websites.moiApplicationStatus import MoiApplicationStatus

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    browser = FirefoxBrowser()
    website = MoiApplicationStatus(browser)
    website.load()
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=browser.get_title())

    browser.close()

if __name__ == '__main__':
    application = ApplicationBuilder().token('6657932574:AAHK0j9Gsl4HtqAo7rKfeTwLc7QAI7dpbvs').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()