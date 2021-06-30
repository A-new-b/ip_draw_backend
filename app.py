from flask import Flask
from rule_init import rule_init, counter, stop
import json

app = Flask(__name__)

num = 0
byte = 0

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/init')
def api_init():
    rule_init()
    global num
    num =0
    global byte
    byte =0
    return json.dumps({"result": "OK"})


@app.route('/api/counter')
def api_count():
    packets_list = counter()
    (now_num, now_bytes) = packets_list[0]  # 获取最新的收包数和字节数
    global num
    global byte
    second_num = now_num - num
    second_byte = now_bytes - byte
    num = now_num
    byte = now_bytes
    return json.dumps(
        {"second_num": second_num, "second_bytes": second_byte, "now_num": now_num, "now_bytes": now_bytes})


@app.route('/api/stop')
def api_stop():
    stop()
    return json.dumps({"result": "OK"})


if __name__ == '__main__':
    app.run(host="localhost", debug=True,port=5001)
