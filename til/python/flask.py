import os
import pandas as pd  # note: pip install xlrd

from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

CSV_DIR = "files"

# file server


@app.route('/upload', methods=['POST'])
def excel_upload():
    file = request.files.get('file')
    if file is None or file.filename is None:
        print("ファイルが見つかりませんでした")
        return jsonify(message=f'ファイルが見つかりませんでした'), 200

    filepath = 'files/' + secure_filename(file.filename)

# file server csv


@app.route('/upload_csv', methods=['POST'])
def csv_upload():
    file = request.files.get('file')
    try:
        df = pd.read_csv(file)
    except:
        return jsonify(message=f'読み込みエラーが発生しました'), 200
    return jsonify(message=f'読み込みました'), 200
