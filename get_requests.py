#!/usr/bin/python3
# Date: August 8, 2019
# Author: vinisgood@gmail.com (Vincent Tang)

import requests
import time
import sys
import datetime

def indefinite_http_get_call(num_calls, interval, endpoint):
    divider = "-------------------------------------------------------------------"
    while True:
        total_response_time_ms = 0
        print("Current date/time: {}".format(datetime.datetime.now()))
        for call in range(1, num_calls + 1):
            r = requests.get(endpoint)
            request_time_ms = r.elapsed.total_seconds() * 1000
            total_response_time_ms += request_time_ms
            print("HTTP GET request number: {}\n"
                  "\tStatus code: {}\n"
                  "\tResponse time(ms): {}".format(call, r.status_code, request_time_ms))
        print("Average Response time(ms): {}\n"
              "{}\nSleeping for {} seconds\n{}".format(total_response_time_ms / num_calls,
                                                       divider, interval, divider))
        time.sleep(interval)


def usage():
    print("Usage: {} [N_of_consecutive_GET_calls] [interval] [URL]\n"
          "\tScript runs N consecutive GET calls against URL every interval secs indefinitely\n"
          "\tDisplays status code, response time, and average response time".format(sys.argv[0]))
    sys.exit(1)


def main():
    if len(sys.argv) != 4:
        usage()
    num_consecutive_calls = int(sys.argv[1])
    interval = int(sys.argv[2])
    url = sys.argv[3]
    indefinite_http_get_call(num_consecutive_calls, interval, url)


if __name__ == '__main__':
    main()
