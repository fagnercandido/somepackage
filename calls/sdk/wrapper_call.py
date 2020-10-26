import sys

sys.path.append('../')


class WrapperCall(object):
    """Class that represent one Wrapper Call"""
    def __init__(self, call_list, result_status):
        self.call_list = call_list
        self.result_status = result_status
