# coding=utf-8
import os
import unittest
from common.HTMLTestRunner_cn import HTMLTestRunner

cur_path = os.path.dirname(os.path.abspath(__file__))

case_path = os.path.join(cur_path, 'case')  # 获取脚本路径（test_case的路径）
filename = os.path.join(cur_path, 'report', 'result.html')    # report的路径

discover = unittest.defaultTestLoader.discover(case_path,
                                               pattern='test_*.py',
                                               top_level_dir=None)

fp = open(filename, 'wb')
runner = HTMLTestRunner(stream=fp,
                        title=u'测试报告',
                        description=u'用例执行情况：')
runner.run(discover)
fp.close()