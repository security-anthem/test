import os
import bottle
from bottle import route, run

@route("/")
def hello_world():
        return "Hello World!"

if __name__ == "__main__":
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

app = bottle.default_app()