from flask import Flask, jsonify

from medalbot.get_counts import get_counts

app = Flask(__name__)


@app.route("/")
def docs():
    return app.send_static_file('endpoints.html')


@app.route("/api/v1/medals")
def medals():
    return jsonify(get_counts())

if __name__ == "__main__":
    app.debug = True
    app.run()
