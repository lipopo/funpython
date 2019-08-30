# -*- coding: utf8 -*-
# 剧本元素集合


class BaseScenItem(object):
    """
    初始化舞台剧元素 演员
    """
    def __init__(self, name, local_status):
        """初始化"""
        pass

    def to_next(self, drama):
        """去下一个场景"""
        pass

    @property
    def status(self):
        """
        舞台剧元素的状态
        状态是随机的 与舞台演员的性格相关
        """
        pass


class WordScenItem(BaseScenItem):
    """字元素 单个字符"""
    def __init__(self, name, word, shower):
        # 元素的名称
        self.name = name
        # 字元素
        self.word = word
        # 当前表演者
        self.shower = shower
        # 当前要做的事情
        self.thing_doing = None

    def to_next(self, drama):
        # 在舞台剧中找到自己的这一幕要做的事情
        next = drama.get(self.name)
        # 由表演者决定自己接下来的行为
        thing_do = self.shower.calc(next)
        self.thing_doing = thing_do

    @property
    def status(self):
        """自己当前的状态"""
        return self.shower.status


