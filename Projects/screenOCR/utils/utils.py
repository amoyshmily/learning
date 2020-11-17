import urllib3
import jsonpath



def anti_https_warnings(fn):
    """
    避免日志中频繁打印HTTPS访问警告信息
    :param fn:装饰对象函数
    :return:
    """

    def work_silent(*args, **kwargs):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        return fn(*args, **kwargs)

    return work_silent


def parseJsonPath(src_data: dict, expr: str) -> list:
    """
    通过jsonpath解析结果
    :param src_data:原始数据
    :param expr:jsonpath表达式
    :return:
    """
    result = jsonpath.jsonpath(obj=src_data, expr=expr)

    return result[0] if result else list()
