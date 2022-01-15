import socket
import re

from http import HTTPStatus
from collections import defaultdict


def get_open_port():
    with socket.socket() as s:
        s.bind(('', 0))
        s.listen(1)
        port = s.getsockname()[1]
    return port


def parse_request_line(line: str):
    request_pattern = re.search(r"\'(.*)\s/.*Host:\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,})", line)
    method = ''
    addr = ''
    port = int

    if request_pattern:
        method = request_pattern.group(1)
        addr = request_pattern.group(2)
        port = int(request_pattern.group(3))
    return method, addr, port


def get_request_status(line: str):
    status_pattern = re.search(r"\s/\?status=(\d{1,3})", line)
    status_value = 200
    status_name = 'OK'

    if status_pattern:
        status = HTTPStatus(int(status_pattern.group(1)))
        status_value = status.value
        status_name = status.name
    return status_value, status_name


def get_request_headers(line: str):
    headers_patterns = {
        'Connection': re.search(r".*Connection:\s(.*?)\\r\\n", line),
        'Upgrade-Insecure-Requests': re.search(r".*Upgrade-Insecure-Requests:\s(.*?)\\r\\n", line),
        'User-Agent': re.search(r".*User-Agent:\s(.*?)\\r\\n", line),
        'Accept': re.search(r".*Accept:\s(.*?)\\r\\n", line),
        'Accept-Encoding': re.search(r".*Accept-Encoding:\s(.*?)\\r\\n", line),
        'Accept-Language': re.search(r".*Accept-Language:\s(.*?)\\r\\n", line)
    }
    request_headers = defaultdict(str)

    for key, value in headers_patterns.items():
        if value:
            request_headers[key] = value.group(1)
    return request_headers

