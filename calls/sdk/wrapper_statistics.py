import sys

sys.path.append('../')


class WrapperStatistics(object):
    """Class that represent one Wrapper Statistics"""
    from server.statistics import Statistics
    def __init__(self, statistics: Statistics, result_status):
        self.statistics = statistics
        self.result_status = result_status
