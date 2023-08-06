"""
    快捷启动方式，便于调试
"""
import os
import sys
from mitmproxy.tools.main import mitmdump, mitmweb

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def execute(filepath: str, port: int = 8866, args: list = None):
    """
    通过本地文件的形式启动

    注意： -p xxx 这种 args 传进来是 2 个元素， --ssl-insecure 是一个元素

    :param filepath: 启动文件路径
    :param port: 端口
    :param args: 其余参数
    :return:
    """
    command = ['-p', str(port), '-s', filepath]
    if args:
        command.extend(args)

    mitmdump(command)


def execute_web(port: int = 8866, args: list = None):
    """
    以 Web 页面的形式显示

    :param port: 端口
    :param args: 其余参数
    :return:
    """
    command = ['-p', str(port), args]
    if args:
        command.extend(args)

    mitmweb(command)
