from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Banca Blindada Bot está funcionando en segundo plano."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)