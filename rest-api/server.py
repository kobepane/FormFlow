from flask import Flask, request, make_response, jsonify
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", 'utils')))
from utils.run_utils import run
# from flask_cors import CORS
import csv

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def handle_files():
    uploaded_files = request.files
    file_names = []
    for key in uploaded_files:
        file = uploaded_files[key]
        file_names.append(file.filename)
        # Add your file processing logic here
        print(file)

    response = {
        "message": f"Successfully received {len(file_names)} files",
        "files": file_names
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)

