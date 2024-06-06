import os
from rgp.reporter import core
from rgp.server import run_app

def hello(name: str) -> str:
    """Just an greetings example.

    Args:
        name (str): Name to greet.

    Returns:
        str: greeting message

    Examples:
        .. code:: python

            >>> hello("Roman")
            'Hello Roman!'
    """
    return f"Hello {name}!"

def generate () -> None:
    dir_path = os.path.dirname(__file__)
    save_path = os.path.join(dir_path, "./static")
    config = core.get_config()
    core.do_generate(save_path, core.init_data(config))
    local_reports = core.get_local_reports()
    return local_reports


def run_server():
    run_app()
