import json
from database import create_call
from database import remove_call
from database import get_all_and_by_type
from database import get_all
from call import Call
from statistics import Statistics


def insert_call(body: str, query_string: str):
    content = json.loads(body)
    for item in content:
        request = Call(item['caller_number'], item['callee_number'], item['start_call'], item['end_call'],
                       item['type_call'])
        create_call(request)


def delete_call(body: str, query_string: str):
    remove_call(query_string[1:])


def get_call(body: str, query_string: str):
    parameters = query_string[1:]
    if parameters == 'statistics':
        return statistics()
    parameters_dict = dict(item.split("=") for item in parameters.split("&"))
    if all(key in parameters_dict for key in ('page_current', 'records_per_page')):
        list_call = get_all_and_by_type(parameters_dict)
        return json.dumps([element.__dict__ for element in list_call], indent=4, sort_keys=True, default=str)
    else:
        raise Exception('should be 2 parameters needed.')


def get_total_duration_call_by_type(list_call):
    sum_inbound = sum(item.duration_call() for item in filter_by_type(list_call, 'INBOUND'))
    sum_outbound = sum(item.duration_call() for item in filter_by_type(list_call, 'OUTBOUND'))
    return {"INBOUND": sum_inbound, "OUTBOUND": sum_outbound}


def filter_by_type(list_call, type_call):
    return list(filter(lambda element: (element.type_call == type_call), list_call))


def get_total_number_calls(list_call):
    return len(list_call)


def get_unique_type_number(list_call, type_number):
    if type_number == 'CALLER':
        return set({item.caller_number for item in list_call})
    else:
        return set({item.callee_number for item in list_call})


def filter_by_number(list_call, number, type_number):
    if type_number == 'CALLER':
        return len(list(filter(lambda element: (element.caller_number == number), list_call)))
    else:
        return len(list(filter(lambda element: (element.callee_number == number), list_call)))


def get_number_calls_by_caller_number(list_call, type_number):
    unique_numbers = get_unique_type_number(list_call, type_number)
    unique_number_dict = {}
    for number in unique_numbers:
        unique_number_dict[number] = filter_by_number(list_call, number, type_number)
    return unique_number_dict


def get_total_calls_cost(list_call):
    return sum(item.cost_call() for item in list_call)


def statistics():
    list_call = get_all()
    total_duration_by_type = get_total_duration_call_by_type(list_call)
    total_number_calls = get_total_number_calls(list_call)
    number_calls_by_caller_number = get_number_calls_by_caller_number(list_call, "CALLER")
    number_calls_by_callee_number = get_number_calls_by_caller_number(list_call, "CALLEE")
    total_calls_cost = get_total_calls_cost(list_call)
    stat = Statistics(total_duration_by_type, total_number_calls,
                      number_calls_by_caller_number, number_calls_by_callee_number, total_calls_cost)
    return json.dumps(stat.__dict__, indent=4, sort_keys=True, default=str)
