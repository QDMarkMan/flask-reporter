from flask import current_app as app
from flask import render_template
from nanoid import generate

from rgp.reporter import core


@app.route("/")
def index():
    context = {
        "project": {"special_name": "special_name", "name": "name"},
        "reports": core.get_local_reports(),
    }

    return render_template("index.html.jinja", context=context)


@app.get("/api/v1/reports")
def report():
    reports = core.get_local_reports()
    for report in reports:
        report["id"] = generate()
    return {"code": 200, "message": "Success", "data": reports}
