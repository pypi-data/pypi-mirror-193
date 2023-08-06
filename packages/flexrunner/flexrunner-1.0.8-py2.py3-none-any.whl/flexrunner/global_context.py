#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:TXU
@file:global_context.py
@time:2022/12/26
@email:tao.xu2008@outlook.com
@description: 
"""
import os
import json
from datetime import datetime
from loguru import logger
from threading import local

from flexrunner.base.db import TestDB
from flexrunner.base.models import TestConf, TestEnv, ReportSummary
from flexrunner.config.cf_xml import ConfigXml
from flexrunner.config.globals import FILE_LOG_LEVEL, MAX_ROTATION, REPORT_DIR, CWD
from flexrunner.utils.util import zfill


class GlobalContext:
    """全局上下文配置参数"""

    driver = None  # 浏览器 driver
    timeout = 10

    # 配置文件/输入参数 解析
    test_conf_path = ""
    test_conf: TestConf = None
    env: TestEnv = None

    # 输出配置
    debug = False
    log_level = FILE_LOG_LEVEL
    max_rotation = MAX_ROTATION

    # 输出信息记录
    report_summary: ReportSummary = ReportSummary()

    # 全局动态缓存
    current_local = local()  # local cache

    # 常量
    time_str = datetime.now().strftime("%Y%m%d%H%M%S")  # 时间字符串

    def __init__(self):
        pass

    @classmethod
    def set_env(cls, env):
        cls.env = env

    @classmethod
    def get_env(cls):
        return cls.env

    @classmethod
    def del_env(cls):
        del cls.env

    @classmethod
    def set_global_cache(cls, key, value):
        if not hasattr(cls.current_local, "glb_cache") or cls.current_local.glb_cache is None:
            cls.current_local.glb_cache = {}
        cls.current_local.glb_cache[key] = value

    @classmethod
    def get_global_cache(cls, key):
        if not hasattr(cls.current_local, "glb_cache") or cls.current_local.glb_cache is None:
            return None
        return cls.current_local.glb_cache.get(key)

    @classmethod
    def del_global_cache(cls):
        if not hasattr(cls.current_local, "glb_cache") or cls.current_local.glb_cache is None:
            return None
        rc_l = cls.current_local
        del rc_l.glb_cache

    @classmethod
    def get_global_step_id(cls, start=1):
        if not hasattr(cls.current_local, "step_id") or cls.current_local.step_id is None:
            cls.current_local.step_id = start
        return cls.current_local.step_id

    @classmethod
    def reset_step_id(cls, start=1):
        cls.current_local.step_id = start

    @classmethod
    def count_global_step_id(cls, start=1, step=1):
        if not hasattr(cls.current_local, "step_id") or cls.current_local.step_id is None:
            cls.current_local.step_id = start
        cls.current_local.step_id += step

    @classmethod
    def get_time_str(cls):
        return datetime.now().strftime("%Y%m%d%H%M%S")  # 时间字符串

    @classmethod
    def get_test_conf(cls) -> TestConf:
        """
        xml测试配置文件-解析
        :return:
        """
        if not hasattr(cls.current_local, "test_conf") or cls.current_local.test_conf is None:
            if cls.test_conf_path:
                logger.info("XML配置文件参数解析...")
                cx = ConfigXml(cls.test_conf_path)
                cls.test_conf = cx.parse_test_conf()
                logger.info(json.dumps(cls.test_conf.dict(), indent=2))
            else:
                logger.info("测试输入参数解析... TODO")  # TODO
                raise Exception("输入参数解析暂不支持，请输入XML配置文件路径！")
        return cls.test_conf

    @property
    def zfill_report_id(self):
        return zfill(self.report_summary.id)

    @property
    def webdriver_path(self):
        return os.path.join(CWD, self.test_conf.project, 'bin', 'webdrivers')

    @property
    def testcase_path(self):
        return os.path.join(CWD, self.test_conf.project, 'testcase')

    @property
    def testdata_path(self):
        return os.path.join(CWD, self.test_conf.project, 'testdata')

    @property
    def log_name(self):
        return '{}_{}.log'.format(self.test_conf.project, self.zfill_report_id)

    @property
    def project_reports_path(self):
        return os.path.join(REPORT_DIR, self.test_conf.project)

    @property
    def output_path(self):
        return os.path.join(REPORT_DIR, self.test_conf.project, self.zfill_report_id)

    @property
    def log_path(self):
        return os.path.join(self.output_path, "log")

    @property
    def log_full_path(self):
        return os.path.join(self.log_path, self.log_name)

    @property
    def html_name(self):
        return '{}_{}.html'.format(self.test_conf.project, self.zfill_report_id)

    @property
    def html_report_path(self):
        return os.path.join(self.output_path, "html")

    @property
    def html_report_full_path(self):
        return os.path.join(self.html_report_path, self.html_name)

    @property
    def xml_report_path(self):
        return os.path.join(self.output_path, "xml")

    def _init_db(self):
        """数据库初始化、插入测试session数据到test report表"""
        db = TestDB()
        db.create_table_if_not_exist()
        self.report_summary.id = db.get_last_id() + 1
        db.insert_init_testreport(self.report_summary.id)

    def init_data(self):
        """解析配置文件并初始化全局变量"""
        self.get_test_conf()  # 解析测试配置文件
        self.set_env(self.test_conf.testbed.env_list[0])  # 环境信息设置为env
        self._init_db()

        self.report_summary.log_path = self.log_path
        self.report_summary.report_html_path = self.html_report_path
        self.report_summary.report_allure_path = self.xml_report_path

    @classmethod
    def add_case_passed(cls):
        cls.report_summary.testcases_stat.total += 1
        cls.report_summary.testcases_stat.passed += 1

    @classmethod
    def add_case_failed(cls, case):
        cls.report_summary.testcases_stat.total += 1
        cls.report_summary.testcases_stat.failed += 1
        cls.report_summary.testcases_stat.failed_list.append(case)

    @classmethod
    def add_case_error(cls, case):
        cls.report_summary.testcases_stat.total += 1
        cls.report_summary.testcases_stat.error += 1
        cls.report_summary.testcases_stat.error_list.append(case)

    @classmethod
    def add_case_skipped(cls, case):
        cls.report_summary.testcases_stat.total += 1
        cls.report_summary.testcases_stat.skipped += 1
        cls.report_summary.testcases_stat.skipped_list.append(case)


if __name__ == '__main__':
    pass
