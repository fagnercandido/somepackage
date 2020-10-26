import requests
import json
from types import SimpleNamespace
import sys

# To add another modules
sys.path.append('../')
from wrapper_statistics import WrapperStatistics
from wrapper_call import WrapperCall

server_url = 'http://localhost:8080/'


def get_statistics():
    """Request to endpoint to get statistics"""
    from server.statistics import Statistics
    response = requests.get(server_url + 'statistics')
    statistics_json = json.loads(response.content, object_hook=lambda element: SimpleNamespace(**element))
    statistics = Statistics(statistics_json.total_duration_by_type,
                            statistics_json.total_number_calls, statistics_json.number_calls_by_caller_number,
                            statistics_json.number_calls_by_callee_number, statistics_json.total_calls_cost)
    return WrapperStatistics(statistics, response.status_code)


def create_call(calls_list):
    """Request to endpoint to create call"""
    json_calls_list = json.dumps([element.__dict__ for element in calls_list], indent=4, sort_keys=True, default=str)
    response = requests.post(server_url, data=json_calls_list)
    return response.status_code


def delete_call(identifier):
    """Request to endpoint to delete call"""
    response = requests.delete(server_url + f'{identifier}')
    return response.status_code


def get_call_with_pagination_and_by_type(page_current, records_per_page, call_type=None):
    """Request to endpoint get calls with pagination"""
    from server.call import Call
    query = f'page_current={page_current}&records_per_page={records_per_page}'
    if call_type:
        query += f'&type={call_type}'
    response = requests.get(server_url + query)
    content = json.loads(response.content)
    calls_list = []
    for item in content:
        calls_list.append(Call(item['caller_number'], item['callee_number'], item['start_call'], item['end_call'],
                               item['type_call']))
    return WrapperCall(calls_list, response.status_code)
