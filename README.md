# Logs examiner
The tool enables one to gather information around the top hosts making the requests and the most number of requests
through each of them, the success and failure percentage for every request and the requests being
unsuccessful on a daily basis. It works on a filter using which the desired data can be fetched.

## Getting Started

This project uses Python 3.7.

### Developer Environment Setup

Create a virtualenv using the Python [venv module](https://docs.python.org/3/library/venv.html) or [pew](https://github.com/berdario/pew) (*P*ython *E*nvironment *W*rapper):

```
# Using venv
python -m venv venv

# The virtualenv won't be activated by default so activate it with:
. venv/bin/activate
```

#### Run Unit Tests
Pytest can be installed using 
```
pip install pytest
```
Executing ```pytest fetch_logs_info.py``` would thus run the test cases fot the log info collector

#### Assumptions
1. The format will remain constant for all the log files.

#### Filters
Filters help to fetch a particular data from the logs as and when required. Below is the mapping for the filters added.

|   value                                       |   Filters                         |
|---------------------------------------------- |-----------------------------------|
|1                                              |top_requests                       |
|---------------------------------------------- |-----------------------------------|
|2                                              |top_hosts                          |
|---------------------------------------------- |-----------------------------------|
|3                                              |percent_successful_requests        |
|---------------------------------------------- |-----------------------------------|
|4                                              |percent_unsuccessful_requests        |
|---------------------------------------------- |-----------------------------------|
|5                                              |top_failed_requests                |
|---------------------------------------------- |-----------------------------------|

### How to use
Run the python script
```
fetch_logs_info.py
```
Choose from the filter mapping displayed and enter the value you want to gather information for.


Example :
```
{1: 'top 10 requests',
 2: 'top 10 hosts',
 3: 'percent successful requests',
 4: 'percent unsuccessful requests',
 5: 'top 10 failed requests'}
Enter value to fetch data for : 1
```
Output :
```
{'163.206.89.4': 4791,
 'edams.ksc.nasa.gov': 6530,
 'piweba3y.prodigy.com': 4416,
 'piweba4y.prodigy.com': 4846,
 'piweba5y.prodigy.com': 4607,
 'www-b2.proxy.aol.com': 3534,
 'www-b3.proxy.aol.com': 3463,
 'www-b5.proxy.aol.com': 3411,
 'www-c5.proxy.aol.com': 3423,
 'www-d1.proxy.aol.com': 3889}
```