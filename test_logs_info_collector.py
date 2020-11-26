from fetch_logs_info import *


class TestLogInfoCollector:

    def test_top_requests(self):
        res = get_top_requests()
        assert type(res) is list
        assert len(res) == 10

    def test_top_hosts(self):
        res = get_top_hosts()
        assert type(res) is list
        assert "edams.ksc.nasa.gov" in res

    def test_successful_request_percentage(self):
        res = fetch_requests_percent()
        assert type(res) is str

    def test_percent_failed_requests(self):
        res = fetch_requests_percent(is_success=False)
        assert type(res) is str

    def test_top_failed_requests(self):
        res = fetch_failed_requests()
        assert type(res) is list
        assert "GET /elv/DELTA/uncons.htm HTTP/1.0" in res

