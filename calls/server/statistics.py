class Statistics(object):
    """Class that represent the Statistics"""
    def __init__(self, total_duration_by_type,
                 total_number_calls, number_calls_by_caller_number,
                 number_calls_by_callee_number, total_calls_cost):
        self.total_duration_by_type = total_duration_by_type
        self.total_number_calls = total_number_calls
        self.number_calls_by_caller_number = number_calls_by_caller_number
        self.number_calls_by_callee_number = number_calls_by_callee_number
        self.total_calls_cost = total_calls_cost

