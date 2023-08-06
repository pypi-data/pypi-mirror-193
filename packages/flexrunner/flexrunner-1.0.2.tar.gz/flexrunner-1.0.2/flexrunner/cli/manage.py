#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:TXU
@file:manage
@time:2023/2/21
@email:tao.xu2008@outlook.com
@description: 项目管理相关命令
"""
import os
import typer
import shutil
from loguru import logger

from flexrunner import config


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        logger.info(f"created folder: {path}")


def create_file(path, file_content=""):
    with open(path, 'w', encoding="utf-8") as py_file:
        py_file.write(file_content)
    msg = f"created file: {path}"
    logger.info(msg)


def create_scaffold(project_name: str) -> None:
    """
    create scaffold with specified project name.
    :param project_name:
    :return:
    """
    if os.path.isdir(project_name):
        logger.info(f"Folder {project_name} already exists, please specify a new project name.")
        return

    logger.info(f"Start to create new test project: {project_name}")
    project_path = os.path.join(os.getcwd(), project_name)
    logger.info(f"Project Path: {project_path}")
    # main.py
    shutil.copy(os.path.join(config.BASE_DIR, "flexrunner", "cli", "main.py"), os.getcwd())

    # reports
    create_folder(os.path.join(os.getcwd(), "reports"))
    # demo
    if project_name == "demo":
        shutil.copytree(os.path.join(config.BASE_DIR, "demo"), project_path)
        return

    # project
    create_folder(project_path)
    shutil.copy(os.path.join(config.BASE_DIR, "demo", "__init__.py"), project_path)
    shutil.copy(os.path.join(config.BASE_DIR, "demo", "conftest.py"), project_path)
    shutil.copy(os.path.join(config.BASE_DIR, "demo", "pytest.ini"), project_path)

    # project/conf
    create_folder(os.path.join(project_path, "conf"))
    create_file(os.path.join(project_path, "conf", "debug.xml"))
    create_folder(os.path.join(project_path, "conf", "testbed"))
    create_file(os.path.join(project_path, "conf",  "testbed", "testbed_debug.xml"))
    create_folder(os.path.join(project_path, "conf", "testset"))
    create_file(os.path.join(project_path, "conf", "testset", "testset_debug.xml"))

    # project/data
    data_sample = '''{
     "example":  [
        ["case1", "dddd"],
        ["case2", "eeee"],
        ["case3", "ffff"]
     ]
    }
    '''
    data_path = os.path.join(project_path, "data")
    create_folder(data_path)
    create_file(os.path.join(data_path, "data_sample.json"), data_sample)

    # project/testcase
    testcase_path = os.path.join(project_path, "testcase")
    create_folder(testcase_path)
    shutil.copy(os.path.join(config.BASE_DIR, "demo", "testcase", "__init__.py"), testcase_path)


def install_driver(browser: str) -> None:
    pass


def startapp(
    project: str = typer.Option("demo", "--project", "-P", help="Create a new automation test project")
):
    """FlexRunner startapp 命令行 CLI"""
    create_scaffold(project)


if __name__ == '__main__':
    pass
