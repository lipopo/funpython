# -*- coding: utf8 -*-


class ScenShow(object):
    """
    一出舞台剧
    包含了可以呈现的所有元素
    文字 图像 视频等
    将所有元素放置到对应的位置
    """
    def __init__(self, drama, items):
        """

        :param drama: 剧本
        :param items: 演员
        """
        self.drama = drama
        self.items = items
        # 指定剧目当前所处的位置
        self.drama_cursor = 0

    def play(self):
        """跳到下一个剧目"""
        if self.show_end:
            return False
        for item in self.items:
            item.to_next(self.drama[self.drama_cursor])
            self.drama_cursor += 1
        return self

    @property
    def show_len(self):
        """舞台剧长度"""
        return len(self.drama)

    @property
    def show_end(self):
        """舞台剧播放结束"""
        return self.drama_cursor <= self.show_len
