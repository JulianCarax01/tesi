import subprocess
import time
import signal
import os

from threading import Thread

from celery.result import allow_join_result

from flask import jsonify

from flask import Flask

from flask_redis import FlaskRedis

from celery2 import celery, preprocessing_task

app = Flask(__name__)

"""
redis = FlaskRedis(app)
redis_process = subprocess.Popen(['redis-server'])
command = "rabbitmq-server"
process = subprocess.Popen(command, shell=True)
time.sleep(5)


def shutdown_rabbitmq():
    command2 = 'rabbitmqctl shutdown -n rabbit@mamba-Aspire-A515-52G'
    subprocess.run(command2, shell=True)


def handle_sigint(signum, frame):
    process.terminate()
    process.wait()
    shutdown_rabbitmq()
    closeCeleryWorkerCommand = "sudo /home/mamba/PycharmProjects/flaskProject/venv/bin/celery multi stop worker1 worker2 worker3"
    subprocess.run(closeCeleryWorkerCommand, shell=True)
    os._exit(0)


signal.signal(signal.SIGINT, handle_sigint)
"""

@app.route('/')
def preprocessing():
    with app.app_context():
        x = celery.send_task('app.preprocessing_task', args=(1,))
        with allow_join_result():
            result = x.get()
        return jsonify(result)

def workers_starting():
    Wcommand = "sudo /home/mamba/PycharmProjects/flaskProject/venv/bin/celery multi start worker1 worker2 worker3 -A sedano --concurrency=2"
    subprocess.run(Wcommand, shell=True)


def start_flask_app():
    port = 5001
    app.run(debug=True, port=port, use_reloader=False)


if __name__ == "__main__":
    flask_thread = Thread(target=start_flask_app)
    #workers_thread = Thread(target=workers_starting)

    #workers_thread.start()
    flask_thread.start()

    flask_thread.join()
    #workers_thread.join()
# 1 terminale: sudo /home/mamba/PycharmProjects/tesi/venv/bin/python hopelessTry.py