"""
**************************************************************************
*  @Copyright [2024] Tongfu.E.
*  @Email etongfu@outlook.com.
*  @Date [2024-03-12 09:45:26].
**************************************************************************
"""
import os


def create_file(path, content=""):
    """
    创建文件

    Args:
        path: 文件路径
        content: 文件内容

    Returns:
        None
    """

    with open(path, "w") as f:
        f.write(content)


def create_folder(path):
    """
    创建文件夹

    Args:
        path: 文件夹路径

    Returns:
        None
    """

    if not os.path.exists(path):
        os.makedirs(path)


def save_file(path, content):
    """
    保存文件

    Args:
        path: 文件路径
        content: 文件内容

    Returns:
        None
    """

    with open(path, "wb") as f:
        f.write(content)
