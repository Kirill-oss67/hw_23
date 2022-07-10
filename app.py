import os
from functions import make_query
from flask import Flask, request
from flask_restx import abort

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=["POST", "GET"])
def perform_query():
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    cnd_1 = request.args.get('cnd_1')
    val_1 = request.args.get('val_1')
    cnd_2 = request.args.get('cnd_2')
    val_2 = request.args.get('val_2')
    file_name = request.args.get('file_name')
    if not (cnd_1 and val_1 and file_name):
        abort(400)
    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        return abort(400)
    if cnd_1 not in ["filter", "map", "unique", 'sort', "limit"]:
        return abort(400)
    with open(file_path) as file:
        res = make_query(cnd_1, val_1, file)
        if cnd_2 and val_2:
            if cnd_2 not in ["filter", "map", "unique", 'sort', "limit"]:
                return abort(400)
            res = make_query(cnd_2, val_2, res)
        if not res[:5] == "Wrong":
            res = "\n".join(res)
    return app.response_class(res, content_type="text/plain")


if __name__ == "__main__":
    app.run(debug=True)
