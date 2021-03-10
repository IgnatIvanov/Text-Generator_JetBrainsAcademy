import re


def matched(template, string):
    res = re.match(template, string)
    return res is not None
