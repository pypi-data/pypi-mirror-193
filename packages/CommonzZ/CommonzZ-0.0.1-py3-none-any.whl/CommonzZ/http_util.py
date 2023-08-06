import json


def params_sort(params: dict, return_text=False):
    """
    参数排序
    :param params:
    :return:
    """
    result = {}
    for i in sorted(params.keys()):
        result[i] = params[i]
    if return_text:
        return json.dumps(result, separators=(',', ':'))
    return result


__all__ = ["params_sort"]
