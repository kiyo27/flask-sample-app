# Flask-app
[![Pytest](https://github.com/kiyo27/flask-sample-app/actions/workflows/pytest.yaml/badge.svg)](https://github.com/kiyo27/flask-sample-app/actions/workflows/pytest.yaml)
[![Author](https://img.shields.io/badge/Author-kiyo27-lightgrey)](https://img.shields.io/badge/Author-kiyo27-lightgrey)
[![version](https://img.shields.io/endpoint?url=https://5p1ommgjfk.execute-api.ap-northeast-1.amazonaws.com/release)](https://github.com/kiyo27/flask-sample-app)

## 環境作成

https://flask.palletsprojects.com/en/2.0.x/installation/#python-version

```
cd python-flask
python -m venv .venv
```

環境をアクティブ
```
venv\Scripts\activate
```

flaskインストール
```
pip install Flask
```

docker 起動

```
docker run -it --rm -p 8080:80 -v ${PWD}:/app python:3.9.6 /bin/bash
```

flask 起動

```
# FLASK_APP=api flask run --port 80 --host 0.0.0.0
```

サーバ起動
```
$env:FLASK_APP = "hello"
flask run
// または
python -m flask run
```

開発モードオン

```
FLASK_APP=api FLASK_ENV=development flask run --port 80 --host 0.0.0.0
# または
FLASK_ENV=development FLASK_APP=app flask run --debugger --reload --port 80 --host 0.0.0.0
```

## flask-restx

```
pip install flask-restx
```

### response marshalling

## marshmallow

インストール

```
pip install marshmallow
```

## pytest

pip でインストール

```
pip install pytest
```

テスト実行

```
pytest tests/app.py
// または
python -m pytest .\tests\app.py
```
