from flask import Flask, request, make_response
import csv

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def handle_files():
    uploaded_files = request.files
    for key in uploaded_files:
        file = uploaded_files[key]
        print(file)
    return "hello\n"

if __name__ == '__main__':
    app.run(debug=True)

