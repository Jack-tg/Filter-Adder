from typing import Optional, List

from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

from tg_bot import dispatcher, LOGGER
from tg_bot.modules.disable import DisableAbleCommandHandler

from telegraph import Telegraph, upload_file



__help__ = """
◆ Bot Name : *Filter Adder*
◆ Creator : [bughunter0](http://t.me//bughunter0)
◆ Credits :  @Noob_admin
◆ Language : Python3
◆ Source Code : 👉 @bughunterbots
◆ Server : Heroku
◆ Database : SQL
◆ Build Status : Beta
"""
__mod_name__ = "🔺About🔺"

