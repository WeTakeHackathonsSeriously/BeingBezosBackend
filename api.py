from flask import Flask, request, jsonify
from base64 import b64decode

import os
import io
import random

from google.cloud import vision
from google.cloud.vision import types

app = Flask(__name__)


# return list of:
# { 
#   "item" : *item name*
#   "box"  : [*array of 4 box values*]
#   "rel"  : *price float*
# }

# Post request to upload image.
# Parameters:
#   ?image - used to pass the base64 encoded image.
#   ?income - the user's average income
# Return:
#   JSON file.

@app.route('/api/upload/', methods=['POST'])
def upload():
    # Code goes here
    image  = request.form.getlist('image')
    image2 = request.args.get('image')
    app.logger.error(image)
    app.logger.error(image2)
    print(image)
    print(image2)
   
    x1 = random.uniform(0, 0.5)
    x2 = random.uniform(0.5, 1)
    y1 = random.uniform(0, 0.5)
    y2 = random.uniform(0.5, 1)

    return jsonify([
        { "item": "laptop"
        , "box" : [x1, y1, x2, y2]
        , "rel" : 0.0043
        }])
