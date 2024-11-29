from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_snake():
    return send_from_directory('.', 'snake.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True)