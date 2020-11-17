# import re


class Contract(object):
    def __init__(self, chars):
        self.chars = chars

        self.title = ''  # 合同标题
        self.no = ''  # 合同编号
        self.signers = []  # 合同签署人
        self.head = None
        self.body = None
        self.tail = None

    @property
    def title(self):
        pass


class Segment(object):
    def __init__(self):
        self.index = None
        self.title = None
        self.sentences = []


class Head(object):
    pass


class Body(object):
    pass


class Tail(object):
    pass


class Title(object):
    pass
