from flask import Flask
from flask_dropzone import Dropzone
import os
from flask_session import Session
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
app = Flask(__name__)
app.config['SECRET_KEY'] =  'aa44ac7b39e9c77d56ed8382358b1cb12f7508cb7aba762437b2a0c40d36'

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)


dir_path = os.path.dirname(os.path.realpath(__file__))

app.config.update(
UPLOADED_PATH = os.path.join(dir_path, "static/uploaded_files"),
DROPZONE_ALLOWED_FILE_TYPE = "image",
DROPZONE_MAX_FILE_SIZE = 3,
DROPZONE_MAX_FILES = 1
)

app.config['DROPZONE_REDIRECT_VIEW'] = 'decoded'

dropzone = Dropzone(app)
from App import routes





