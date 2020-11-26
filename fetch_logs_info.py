from collections import defaultdict
from re import findall
from pprint import pprint

from config import Config


def get_top_requests() -> list:
    """
    Desc: Method to fetch top 10 requests.
    :return: list containing tuple of request and their count
    """
    req_count = defaultdict(int)
    top_requests = list()
    with open(Config.log_file_path, "r") as file:
        for line in file.readlines():
            try:
                match = " ".join(findall(Config.regex_for_requests, line)[0])
                req_count[match] += 1
            except IndexError:
                continue
    # Get top 10 requests from a dictionary sorted in descending order
    for request, count in sorted(req_count.items(), key=lambda item: item[1], reverse=True)[:10]:
        top_requests.append((request, count))
    return top_requests


def fetch_requests_percent(is_success: bool = True) -> str:
    """
    Desc: Method to evaluate request success/failure percentage
    :return: string of success/failure percentage
    """
    request_counter = 0
    total_request = 0
    with open(Config.log_file_path, "r") as file:
        for line in file.readlines():
            total_request += 1
            try:
                match = findall(Config.regex_for_status_code, line)[0]
                if is_success and (match.startswith("2") or match.startswith("3")):
                    request_counter += 1
                elif not is_success and not (match.startswith("2") or match.startswith("3")):
                    request_counter += 1
            except IndexError:
                continue
    request_percent = (request_counter * 100) / total_request
    if is_success:
        return f"Successful requests : {request_percent:.4f} %"
    else:
        return f"Failed requests :  {request_percent:.4f} %"


def fetch_failed_requests() -> list:
    """
    Desc: Method to fetch top 10 unsuccessful requests.
    :return: list containing request and their count
    """
    unsuccessful_request_counter = 0
    failed_requests = list()
    with open(Config.log_file_path, "r") as file:
        for line in file.readlines():
            try:
                match = findall(Config.regex_for_status_code, line)[0]
                if not (match.startswith("2") or match.startswith("3")):
                    failed_requests.append(" ".join(findall(Config.regex_for_requests, line)[0]))
                    unsuccessful_request_counter += 1
            except IndexError:
                continue
            if unsuccessful_request_counter > 10:
                break
    return failed_requests


def get_top_hosts() -> list:
    """
    Desc: Method to fetch top 10 hosts.
    :return: list containing tuple of hosts and their count.
    """
    host_count = defaultdict(int)
    top_hosts = list()
    with open(Config.log_file_path, "r") as file:
        for line in file.readlines():
            try:
                match = findall(Config.regex_for_hosts, line)[0]
                host_count[match] += 1
            except IndexError:
                continue
    for request, count in sorted(host_count.items(), key=lambda item: item[1], reverse=True)[:10]:
        top_hosts.append((request, count))
    return top_hosts


def get_logs_data():
        pprint(Config.filters)
        value = int(input("Enter value to fetch data for : "))
        if value == 1:
            return get_top_requests()
        elif value == 2:
            return get_top_hosts()
        elif value == 3:
            return fetch_requests_percent()
        elif value == 4:
            return fetch_requests_percent(is_success=False)
        elif value == 5:
            return fetch_failed_requests()
        else:
            print("Please select a valid filter")


if __name__ == "__main__":
    pprint(get_logs_data())