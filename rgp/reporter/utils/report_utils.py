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

def create_report_save_folder(save_path, context):
    """ Generate report folder
    _summary_
    Args:
        save_path (_type_): _description_
        context (_type_): _description_

    Returns:
        _type_: _description_
    """
    now_date = dt.datetime.now().strftime("%Y-%m-%d:%H-%M")
    folder_name = context["project"]["special_name"] or context["project"]["name"]
    suffix = context["config"]["timestamp"] and now_date or ""
    report_folder = os.path.join(save_path, folder_name, suffix)
    file_utils.create_folder(report_folder)
    return report_folder
