# index.py file
import base64
import datetime as dt
import io
import os
import random

import jinja2
import matplotlib.pyplot as plt

from rgp.reporter.utils import file_utils, reader, report_utils

# Step 1 - create data for report
salesTblRows = []
for k in range(10):
    costPu = random.randint(1, 15)
    nUnits = random.randint(100, 500)
    salesTblRows.append(
        {
            "sNo": k + 1,
            "name": "Item " + str(k + 1),
            "cPu": costPu,
            "nUnits": nUnits,
            "revenue": costPu * nUnits,
        }
    )

topItems = [
    x["name"] for x in sorted(salesTblRows, key=lambda x: x["revenue"], reverse=True)
][0:3]

todayStr = dt.datetime.now().strftime("%d-%b-%Y")

# create logo image from file
current_dir = os.path.dirname(__file__)
logo_path = os.path.join(current_dir, "./templates/assets/logo.png")

with open(logo_path, "rb") as f:
    logoImg = base64.b64encode(f.read()).decode()

# generate sales bar chart image
plotImgBytes = io.BytesIO()
fig, ax = plt.subplots()
ax.bar([x["name"] for x in salesTblRows], [x["revenue"] for x in salesTblRows])
fig.tight_layout()
fig.savefig(plotImgBytes, format="jpg")
plotImgBytes.seek(0)
plotImgStr = base64.b64encode(plotImgBytes.read()).decode()

# ------------------------------ Generate step ------------------------------ //
def init_data(config):
    context = {
        "config": config,
        # project data
        "project": {
            "name": "Bio Project",
            "version": "1.0",
            "author": "Bio",
            "special_name": "Bio 02",
            "description": "This is a sample sales report.",
        },
        # report data
        "reportDtStr": todayStr,
        "salesTblRows": salesTblRows,
        "topItemsRows": topItems,
        "salesBarChartImg": plotImgStr,
        "logoImg": logoImg,
        # "bootstrapCSS": requests.get("https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css").text,
        # "bootstrapJS": requests.get("https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js").text
    }
    context.update(config)
    print("Context generate ok.")
    return context


def get_config(config={}):
    _config = {
        "timestamp": False,
    }
    _config.update(config)
    return _config


def get_report_template(template):
    templates_path = os.path.join(os.path.dirname(__file__), "./templates")
    template = jinja2.Environment(
        loader=jinja2.FileSystemLoader(templates_path),
        autoescape=jinja2.select_autoescape,
    ).get_template(template)
    print("Template generate ok")
    return template


def get_report_content(template, context):
    report_content = template.render(context)
    print("Content generate ok")
    return report_content


def save_report_as_zip(report_path, report_content):
    with open(report_path, mode="w") as f:
        f.write(report_content)
    print("Report save ok")


def save_report(save_path, report_content, context):
    report_folder = report_utils.create_report_save_folder(save_path, context)
    file_name = "report.html"
    report_path = os.path.join(report_folder, file_name)
    file_utils.create_file(report_path, report_content)
    print("Report " + report_folder + " save ok")


def do_generate(path, context, template="template.html"):
    template = get_report_template(template)
    content = get_report_content(template, context)
    save_report(path, content, context)


def get_reports_location():
    """
    获取报告保存位置, 属于配置文件
    """
    dir_path = os.path.dirname(__file__)
    print(dir_path)
    return os.path.join(dir_path, "../static/dist/reports")


def get_local_reports():
    reports_location = get_reports_location()
    reports_reader = reader.ReportReader(reports_location)
    reports = reports_reader.get_folders()
    return reports
