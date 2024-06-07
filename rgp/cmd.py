import os

from rgp.reporter import core
from rgp.server import run_app


def generate(name: str) -> None:
    save_path = core.get_reports_location()
    config = core.get_config(
        {
            "project": {"name": name, "special_name": name},
        }
    )
    core.do_generate(save_path, core.init_data(config))
    local_reports = core.get_local_reports()
    return local_reports


def run_server():
    run_app()
