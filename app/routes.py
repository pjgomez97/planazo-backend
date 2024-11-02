from flask import current_app as app


@app.route("/")
def hello_world() -> str:
    return "Miguelom Maricon"
