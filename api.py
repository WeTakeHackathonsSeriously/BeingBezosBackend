from flask import Flask, request, jsonify
from base64 import b64decode

import os
import io

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
# Return:
#   JSON file.

@app.route('/api/upload/', methods=['POST'])
def upload():
    # Code goes here
    print(request.form.getlist('image'))

    return jsonify(items=[
        { "item": "laptop"
        , "box" : [0.25, 0.25, 0.75, 0.75]
        , "rel" : 0.0043
        }])
