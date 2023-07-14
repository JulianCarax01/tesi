from threading import Thread

from celery.result import allow_join_result

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

# 1 terminale: redis-server
#2 terminale sudo rabbitmqctl shutdown -n rabbit@mamba-Aspire-A515-52G ; sudo rabbitmq-server
# 2 terminale: sudo /home/mamba/PycharmProjects/tesi/venv/bin/python hopelessTry.py
