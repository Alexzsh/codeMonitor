# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from flask import Flask
from flask import request
import json
from colorlog import ColoredFormatter
app=Flask(__name__)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import logging


def getlogger():
    logger = logging.getLogger(__name__)  # 创建一个logger对象
    logger.setLevel('INFO')
    BASIC_FORMAT = '%(asctime)s  %(filename)s : %(levelname)s  %(message)s'
    DATE_FORMAT = '%Y-%m-%d %A %H:%M:%S'
    formatter = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)
    color_formatter = ColoredFormatter('%(log_color)s[%(module)-15s][%(funcName)-20s][%(levelname)-8s] %(message)s')
    chlr = logging.StreamHandler()  # 输出到控制台的handler
    chlr.setFormatter(color_formatter)
    chlr.setLevel('INFO')  # 也可以不设置，不设置就默认用logger的level
    fhlr = logging.FileHandler('logger.log')  # 输出到文件的handler
    fhlr.setFormatter(color_formatter)
    logger.addHandler(chlr)
    logger.addHandler(fhlr)
    return logger

logger=getlogger()


"""Start the bot."""
#bot name: dlMonitor
# Create the EventHandler and pass it your bot's token.
updater = Updater("682756941:AAE4qh79rk4JY6cMVrv_mh3_2QKT29Dr0_0")
update1 = Updater("682756941:AAE4qh79rk4JY6cMVrv_mh3_2QKT29Dr0_0")
# Get the dispatcher to register handlers
dp = updater.dispatcher
dp1 = update1.dispatcher

tele_bot=telegram.Bot(token="682756941:AAE4qh79rk4JY6cMVrv_mh3_2QKT29Dr0_0")

def command(add_type,handler=None,cmd=None,**kw):
    def decorater(func):
        def wrapper(*args,**kw):
            return func(*args,**kw)
        if handler is not None:
            func_handler=handler(func,**kw) if cmd==None else handler(cmd,func,**kw)
        else:
            func_handler=func
        add_type(func_handler)
        return wrapper
    return decorater
# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
@command(dp.add_handler,CommandHandler,'start')
def start(bot, update):
    bot.send_message(chat_id=140514984,text='i love u more than i can say')
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')
    logging.info('start')

@command(dp.add_handler,CommandHandler,'help')
def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

@command(dp.add_handler,MessageHandler,Filters.text)
def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

@command(dp.add_error_handler)
def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)



@app.route('/post',methods=['POST'])
def testPost():
    logger.info(request.get_json())
    tele_bot.send_message(chat_id=140514984,text=request.get_json())
    return "hello"




# on different commands - answer in Telegram
# dp.add_handler(CommandHandler("start", start))
# dp.add_handler(CommandHandler("help", help))

# on noncommand i.e message - echo the message on Telegram
# dp.add_handler(MessageHandler(Filters.text, echo))

# log all errors
# dp.add_error_handler(error)

# Start the Bot
updater.start_polling()
# update1.start_polling()
# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
# updater.idle()
