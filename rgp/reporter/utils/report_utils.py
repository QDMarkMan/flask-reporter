"""
**************************************************************************
*  @Copyright [2024] Tongfu.E.
*  @Email etongfu@outlook.com.
*  @Date [2024-03-15 16:23:26].
*  @Description Utils for report.
**************************************************************************
"""
import datetime as dt
import os

from . import file_utils

"""
创建报告保存文件夹，这个是比较特殊的需求，属于半定制的。
"""


def create_report_save_folder(save_path, context):
    # Generate report folder
    now_date = dt.datetime.now().strftime("%Y-%m-%d:%H-%M")
    folder_name = context["project"]["special_name"] or context["project"]["name"]
    suffix = context["config"]["timestamp"] and now_date or ""
    report_folder = os.path.join(save_path, folder_name, suffix)
    # Create folder
    file_utils.create_folder(report_folder)
    return report_folder
