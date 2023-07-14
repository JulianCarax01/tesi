from threading import Thread

from flask import jsonify

from flask import Flask

from celery2 import celery

app = Flask(__name__)



receiver = "alexandros0117@gmail.com"


@app.route("/")
def preprocessing():
    with app.app_context():
        celery.send_task('sedano_to_upload.preprocessing_task', args=(receiver,))
        return jsonify("ok")

"""@app.route('/')
def preprocessing():
    with app.app_context():
        x = celery.send_task('sedano_to_upload.preprocessing_task', args=(3,))
        with allow_join_result():
            result = x.get()
        return jsonify(result)"""


def start_flask_app():
    port = 5001
    app.run(debug=True, port=port, use_reloader=False)


if __name__ == "__main__":
    flask_thread = Thread(target=start_flask_app)
    flask_thread.start()
    flask_thread.join()

