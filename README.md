# Flask restx sample app

Flask-RESEX  
https://flask-restx.readthedocs.io/en/latest/index.html

Qiita 記事  
https://qiita.com/kiyo27/items/d928f65b215d914f1979

## 環境作成

docker 起動

```
docker run -it --rm -p 8080:80 -v ${PWD}:/app python:3.9.6 /bin/bash
```

仮想環境作成  
https://flask.palletsprojects.com/en/2.0.x/installation/#python-version

```
git clone git@github.com:kiyo27/flask-sample-app.git
cd flask-sample-aa
python -m venv .venv
```

環境をアクティブ(windowsの場合)

```
venv\Scripts\activate
```

mac の場合

```
source <venv>/bin/activate
```

ライブラリインストール

```
pip install -r requirements.txt
```

flask 起動

```
# FLASK_ENV=development FLASK_APP=app flask run --debugger --reload --port 80 --host 0.0.0.0
```

postman 出力

```
python postman.py
```
