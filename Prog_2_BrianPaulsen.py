#!/usr/bin/env python3
import requests

from flask import Flask, request, abort, send_from_directory
from Image_border_detect_crop import has_border, filter_border
from PIL import Image
from io import BytesIO


app = Flask(__name__)


app.config['DEBUG'] = True


# I'm passing the url in as an arg, I know another option is
# to use JSON. I wasn't sure which was better
@app.route('/hasborder', methods=['POST'])
def has_border_endpoint():
    if 'filename' in request.args:
        return str(has_border(request.args['filename']))
    else:
        abort(400)
        
@app.route('/filterborder', methods=['POST'])
def filter_board_endpoint():
    if 'filename' in request.args:
        file_path = request.args['filename']
        
        filter_border(file_path)
        
        path_arr = file_path.split('\\')
        file_name = path_arr[-1]
        new_file_name = file_name.replace('.','_edited.')
        new_file_path = '\\'.join(path_arr[:-1])+ \
                '\\' + new_file_name
        return 'File Edited, New file path: {}'.format(new_file_path)
        
        return str(has_border(request.args['filename']))
    else:
        abort(400)

app.run()