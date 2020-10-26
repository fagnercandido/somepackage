from client_sdk import get_statistics
from client_sdk import create_call
from client_sdk import delete_call
from client_sdk import get_call_with_pagination_and_by_type


def create_call_api(list_calls):
    """Used to create calls"""
    return create_call(list_calls)


def get_statistics_api():
    """Used to get statistics"""
    return get_statistics()


def delete_call_api(identifier):
    """Used to remove call"""
    return delete_call(identifier)


def get_call_with_pagination_and_by_type_api(page_current, records_per_page, call_type=None):
    """Used to get calls with pagination and if exists call type"""
    return get_call_with_pagination_and_by_type(page_current, records_per_page, call_type)


def main():
    pass


if __name__ == "__main__":
    main()
