# -*- coding: utf8 -*-

class Shower(object):
    """
    表演者 拥有自己的执行轨迹和执行权限
    """
    @property
    def status(self):
        """表演者当前的状态"""
        return None

    def calc(self):
        """计算状态变更"""
        pass
