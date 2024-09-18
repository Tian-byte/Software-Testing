from flask import Flask

app = Flask(__name__)


# 定义接口
@app.route("/login", methods=["post"])
def login():
    return {"status": 200, "msg": "登录成功！", "token": "xxx123123123"}


@app.route("/login/lgy", methods=["post"])
def lgy():
    return "haha", 407, {"status": 200, "msg": "登录成功！", "token": "xxx123123123"}


app.run()
