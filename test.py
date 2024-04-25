"""
**************************************************************************
*  @Copyright [2024] etongfu@outlook.com.
*  @Date [2024-03-28 16:51:39].
*  @Description .
**************************************************************************
"""
from reporter import core

# Test
config = core.get_config()
core.do_generate("/static/dist/reports", core.init_data(config))

local_reports = core.get_local_reports()
print(local_reports)