"""
**************************************************************************
*  @Copyright [2024] etongfu@outlook.com.
*  @Date [2024-03-28 16:51:39].
*  @Description .
**************************************************************************
"""
import os
from reporter import core
"""
获取报告保存位置, 属于配置文件
"""
def get_static_location():
    dir_path = os.path.dirname(__file__)
    print(dir_path)
    return os.path.join(dir_path, "./static")
  
# Test
config = core.get_config()
save_path = get_static_location()
core.do_generate(save_path, core.init_data(config))

local_reports = core.get_local_reports()
print(local_reports)