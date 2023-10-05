#!/usr/bin/env python

# https://docs.python.org/3/howto/logging.html#configuring-logging
# https://www.toptal.com/python/in-depth-python-logging

from config import environments as env
import logging
from logging.handlers import RotatingFileHandler
# from logging.handlers import TimedRotatingFileHandler
import os
import sys

if not os.path.exists(env.LOG_PATH):
    os.mkdir(env.LOG_PATH)

def get_console_handler():
   console_handler = logging.StreamHandler(sys.stdout)
   console_handler.setFormatter(logging.Formatter(env.FORMATTER))
   return console_handler

def get_file_handler():
#    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
   file_handler = RotatingFileHandler(env.LOG_FILE, maxBytes=10240, backupCount=10)
   file_handler.setFormatter(logging.Formatter(env.FORMATTER))
   return file_handler

def get_logger(logger_name):
   logger = logging.getLogger(logger_name)
   logger.setLevel(logging.DEBUG) # better to have too much log than not enough
   logger.addHandler(get_console_handler())
   logger.addHandler(get_file_handler())
   # with this pattern, it's rarely necessary to propagate the error up to parent
   logger.propagate = False
   return logger
