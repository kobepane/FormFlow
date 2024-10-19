from flask import Flask, request

app = Flask(__name__)

@app.route("/upload", method='POST')
def handle_files():
    return "hello\n"

if __name__ == '__main__':
    app.run(debug=True)

