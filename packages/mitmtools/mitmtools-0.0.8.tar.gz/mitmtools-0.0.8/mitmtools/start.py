"""
    快捷启动方式，便于调试
"""
import os
import sys
from mitmproxy.tools.main import mitmdump, mitmweb

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def execute(filepath: str, port: int = 8866, args: str = ''):
    """
    通过本地文件的形式启动

    :param filepath: 启动文件路径
    :param port: 端口
    :param args: 其余参数
    :return:
    """
    command = ['-p', str(port), '-s', filepath, args]

    mitmdump(command)


def execute_web(port: int = 8866, args: str = ''):
    """
    以 Web 页面的形式显示

    :param port: 端口
    :param args: 其余参数
    :return:
    """
    command = ['-p', str(port), args]

    mitmweb(command)
