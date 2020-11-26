class Config:
    log_file_path = "access_log_Aug95.log"
    regex_for_requests = r'"(GET|POST|PUT|DELETE)\s([a-zA-Z0-9-\/\.]*)\s(HTTP\/[0-9\.]*)"'
    regex_for_status_code = r'"\s([0-9]*)'
    regex_for_hosts = r'^([a-zA-Z0-9\.-]*)'
    filters = {
            1 : "top 10 requests",
            2 : "top 10 hosts" ,
            3 : "percent successful requests",
            4 : "percent unsuccessful requests",
            5 : "top 10 failed requests"
    }