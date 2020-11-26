from collections import defaultdict
from re import findall
from pprint import pprint

from fetch_logs_info import get_top_hosts
from config import Config


def all_info():
    """For each of the top 10 hosts, it fetches the top 5 pages requested and the number of requests for each"""
    top_hosts = list((get_top_hosts()).keys())
    top_requests = defaultdict(int)
    top_hosts_data = dict()
    for each_host in top_hosts:
        req_count = list()
        with open(Config.log_file_path, "r") as file:
            # Read all lines in the file one by one
            for line in file.readlines():
                try:
                    if each_host in line:
                        match = " ".join(findall(Config.regex_for_requests, line)[0])
                        top_requests[match] += 1
                except IndexError:
                    continue
        for request, count in sorted(top_requests.items(), key=lambda item: item[1], reverse=True)[:5]:
            req_count.append({request:count})
        # Updating the dictionary where host is the key and value denotes a list of dictionaries containing
        # top 5 requests and their count
        top_hosts_data[each_host] = req_count
    return top_hosts_data


if __name__ == "__main__":
    pprint(all_info())