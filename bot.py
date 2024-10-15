import requests
import json
import os
import sqlite3
import re
from datetime import datetime, timedelta, timezone
from telegram import Update, Bot, ChatPermissions, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler, ContextTypes, CallbackContext
from telegram.ext import CallbackQueryHandler


单py文件运行，极致的安装效率
源码作者  @houguo
