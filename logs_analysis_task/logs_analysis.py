import argparse
import json
import re
import os

from collections import defaultdict

parser = argparse.ArgumentParser(description='Process log files')
parser.add_argument('-p', dest='path', action='store', help='Path to logfile or folder')
args = parser.parse_args()

log_files_abs_paths = []


def parse_logs(path: str):
    request_no = 0
    requests_by_method = {
        "GET": 0,
        "POST": 0,
        "PUT": 0,
        "DELETE": 0,
        "HEAD": 0,
        "CONNECT": 0,
        "OPTIONS": 0,
        "TRACE": 0

    }
    requests_by_ip = defaultdict(int)
    requests_by_time = dict()
    requests_by_time_top = []

    with open(path) as f:
        for line in f:
            request = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s\S\s\S.*HTTP.*\"\s(.*)", line)

            if request is not None:
                request_no += 1
                requests_by_ip[request.group(1)] += 1
                requests_by_time[line] = int(request.group(2))

                method = re.search(r"] \"(GET|POST|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE)", line)
                if method is not None:
                    requests_by_method[method.group(1)] += 1

    requests_by_time_sorted = sorted(requests_by_time.items(), key=lambda kv: kv[1], reverse=True)[:3]
    for i in requests_by_time_sorted:
        requests_by_time_top.append(i[0])

    result = {
        "TOTAL REQUESTS NUMBER": request_no,
        "REQUESTS NUMBER BY HTTP METHOD": requests_by_method,
        "3 TOP IPS (BY NUMBER OF REQUESTS)": sorted(requests_by_ip.items(), key=lambda kv: kv[1], reverse=True)[:3],
        "3 TOP REQUESTS (BY DURATION)": requests_by_time_top
    }

    result_json = json.dumps(result, indent=4)
    print(result_json)

    with open(f"{path}[PARSED].json", "w", encoding='UTF-8') as f:
        f.write(result_json)


def parse_logs_in_folder(folder_path: str):
    for file in os.listdir(folder_path):
        if file.endswith(".log"):
            log_files_abs_paths.append(os.path.join(folder_path, file))
    for file in log_files_abs_paths:
        parse_logs(file)


if os.path.isdir(args.path):
    parse_logs_in_folder(args.path)
else:
    parse_logs(args.path)
