#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
import logging
from logging import Formatter, FileHandler
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')


#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return 'hello world'


@app.route('/health')
def health_check():
    app.logger.info("run health check")
    return '', 200


# ------------------ #
# Error Handlers
# ------------------ #

@app.errorhandler(500)
def internal_error(error):
    return 'Internal server error', 500


@app.errorhandler(404)
def not_found_error(error):
    return 'Not found', 404


#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


