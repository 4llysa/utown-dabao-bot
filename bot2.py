import logging
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler, ConversationHandler
import sqlite3

# havent link the db shit
data={}

ORDERS_OPEN = False

logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	level=logging.INFO
)

async def startorder(update: Update, context: ContextTypes.DEFAULT_TYPE):
	user = update.message.from_user
	await context.bot.send_message(
		chat_id=update.effective_chat.id,
		text="Order has been set up")
	global ORDERS_OPEN
	ORDERS_OPEN = True
	data[user.first_name]={}
	return ConversationHandler.END

async def choosestall(update: Update, context: ContextTypes.DEFAULT_TYPE):
	if not ORDERS_OPEN:
		return cancel
	reply_keyboard = [["Stall 1", "Other"]]
	await context.bot.send_message(chat_id=update.effective_chat.id,
		text="Which stall?",
		reply_markup=ReplyKeyboardMarkup(
			reply_keyboard,one_time_keyboard=True,input_field_placeholder="which stall?"))
	return choosedish
	
async def choosedish(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await context.bot.send_message(chat_id=update.effective_chat.id,
		text="What would you like to order?")
	return confirmation

async def confirmation(update: Update, context: ContextTypes.DEFAULT_TYPE)
	user = update.message.from_user
	order = update.message.text
	data[user.first_name] = order
	await context.bot.send_message(chat_id=update.effective_chat.id,
		text=f"Your order of {update.message.text} is confirmed")
	return end

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE):
	return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
	user=update.message.from_user
	logger.info("User %s canceled the order.", user.first_name)
	await update.message.reply_text(
		"Bye",reply_markup=ReplyKeyboardRemove())
	return ConversationHandler.END

if __name__ == '__main__':
    application = ApplicationBuilder().token('5860683402:AAELSZ23FifRqbdW09ayDeVg8UM6Yvh6w5k').build()
    start_handler = CommandHandler('startorder', startorder)
    conv_handler = ConversationHandler(
    	entry_points=[CommandHandler("joinorder", choosestall)],
    		states={
    			choosestall: [MessageHandler(filters.Regex("^(Stall 1|Other)$"), choosestall)],
    			choosedish: [MessageHandler(filters.Regex("^(Stall 1|Other)$"), choosedish)],
    			confirmation: [MessageHandler(filters.Regex("^(Stall 1|Other)$"), confirmation)],
    			end: [MessageHandler(filters.Regex("^(Stall 1|Other)$"), end)]
	    },
	    fallbacks=[CommandHandler("cancel", cancel)],)
    application.add_handler(conv_handler)
    # application.add_handler(startorder)
    application.run_polling()

