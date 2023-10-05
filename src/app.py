#!/usr/bin/env python

"""Module providing a main api boilerplate."""

from flask import Flask, jsonify
from src.utils import dt
from config import environments as env
from src.utils import logger

app = Flask(__name__)

my_logger = logger.get_logger(env.LOG_MODULE)

@app.route('/', methods=['GET'])

def index():
    my_logger.debug('Request app.index')
    """Function printing heartbeat."""
    return jsonify({'datetime': dt.formatted_now()})

if __name__ == "__main__":
    app.run(
        port=env.HOST_PORT, 
        host=env.HOST_ADDRESS, 
        use_reloader=False,
        )