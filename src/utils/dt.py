#!/usr/bin/env python

import datetime
from config import environments as env

def formatted_now():
    return datetime.datetime.now().strftime(env.DATETIME_FORMAT)
