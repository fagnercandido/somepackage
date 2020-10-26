class Call(object):
    """Class that represent one Call"""

    def __init__(self, caller_number, callee_number, start_call, end_call, type_call, id=None):
        self.id = id
        self.caller_number = caller_number
        self.callee_number = callee_number
        self.start_call = start_call
        self.end_call = end_call
        self.type_call = type_call

    def duration_call(self) -> int:
        return divmod((self.end_call - self.start_call).total_seconds(), 60)[0]

    def cost_call(self) -> float:
        if self.type_call == 'INBOUND':
            return 0.0
        else:
            cost = 0.0
            for minutes in range(int(self.duration_call())):
                if minutes <= 5:
                    cost += 0.10
                else:
                    cost += 0.05
            return float("{:.2f}".format(cost))
