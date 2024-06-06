from flask import render_template, current_app as app
from rgp.reporter import core
from nanoid import generate

@app.route('/')
def index():
    context = {
        "project": {
            "special_name": "special_name",
            "name": "name"
        },
        "reports": core.get_local_reports()
    }

    return render_template('index.html.jinja', context=context)

@app.get('/api/v1/reports')
def report():
    reports = core.get_local_reports()
    for report in reports:
        report["id"] = generate()
    return {
        "code": 200,
        "message": "Success",
        "data": reports
    }
