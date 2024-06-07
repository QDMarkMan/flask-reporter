"""
**************************************************************************
*  @Copyright [2024] Tongfu.E.
*  @Email etongfu@outlook.com.
*  @Date [2024-03-26 18:04:05].
*  @Description Reading local reports.
**************************************************************************
"""
import os
from datetime import datetime


class ReportReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, "r") as f:
            return f.read()

    def get_folders(self):
        folders = os.listdir(self.path)
        results = []
        for i in folders:
            location = os.path.join(self.path, i)
            if os.path.isdir(location):
                results.append(
                    {
                        "name": i,
                        "location": location,
                        "relative_location": location.replace(self.path, ""),
                        "create_time": datetime.fromtimestamp(
                            os.path.getctime(location)
                        ).strftime("%Y-%m-%d %H:%M:%S"),
                    }
                )
        return results

    def get_report_zip(self, report_name):
        # report_path = os.path.join(self.path, report_name)
        # report_zip_name = report_name + ".zip"
        # with ZipFile(report_zip_name, 'w') as f:
        return None
