from dotenv import load_dotenv

load_dotenv()

import os
import telebot
import sqlite3

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

'''
/menu
'''
@bot.message_handler(commands=["menu"])

def get_food_options(message):
    conn = sqlite3.connect('food_options.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, ROUND(price, 2) FROM food_options")
    food_options = cursor.fetchall()
    options = ""
    for option in food_options:
        options += "ID: " + str(option[0]) + "\n" + f"*{option[1]}*" + " - " + "$" + str(format(option[2],'.2f')) + "\n" + "\n"
    bot.send_message(chat_id=message.chat.id, text=options, parse_mode ="Markdown")
    conn.commit()
    conn.close()



'''
/help
'''
@bot.message_handler(commands=["help"])




def get_functions(message):
    functions = """
Welcome to utown-dabao-bot! 
Click or type any of the following: 
/new *[closing time]* - Creates a new order with the closing time
/join *[order id]* -  Join an existing order
/menu - Show the menu of the selected store
/add *[item id]* - Add item to order
/view *[order id]* - Show the list of orders
/pay - After you have paid, remove your order from the list 
/help - Get help on how to use the bot
"""
    bot.send_message(chat_id=message.chat.id, text=functions, parse_mode ="Markdown")

bot.infinity_polling()


