from flask import Flask, request, make_response, jsonify
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", 'utils')))
from utils.run_utils import run
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import CSV_HEADERS
# from flask_cors import CORS
import csv
import io


app = Flask(__name__)


@app.route("/upload", methods=['POST'])
def handle_files():
    uploaded_files = request.files
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(CSV_HEADERS)
    for key in uploaded_files:
        file = uploaded_files[key]
        # Add your file processing logic here
        file_bytes = file.read()
        row = run(file_bytes)
        print(row)
        writer.writerow(row)
    buffer.seek(0)
    
    response = make_response(buffer.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=data.csv"
    response.headers["Content-Type"] = "text/csv"

    return response


if __name__ == '__main__':
   app.run(debug=True)
