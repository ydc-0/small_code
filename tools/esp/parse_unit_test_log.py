import argparse
import os
import re
import xlwt
# import pandas as pd



UNIT_LOG_FILE="E:/test.md"

PATTERN_ONE_CASE = re.compile(r"unity: Running ([\s\S]+?)\.\.\.([\s\S]+?)PASS")
PATTERN_THROUGHPUT = re.compile(r"(\d+.\d+) Mbps")
# PATTERN_FAIL_PERCENT = re.compile(r"fail:(\d+\(\d+.\d+%\))")
PATTERN_FAIL_COUNT = re.compile(r"fail:(\d+)\(\d+.\d+%\)")
PATTERN_FAIL_PERCENT = re.compile(r"fail:\d+\((\d+.\d+%)\)")

PATTERN_LOST = re.compile(r"lost:(\d+)")
# PATTERN_COUNTS = re.compile(r"((?:enable:\d+)|(?:complete:\d+/?\d{0,10})|(?:success:\d+)|(?:rtt\(max:\d+, min:\d+\)))")
PATTERN_COUNTS = re.compile(r"((?:enable:\d+)|(?:complete:\d+/?\d{0,10})|(?:success:\d+))")
PATTERN_RTT = re.compile(r"(rtt\(max:\d+, min:\d+\))")
PATTERN_FAIL_COUNTS = re.compile(r"\(test\)\[\d+\]\[\d+\]\[\d+\]([\s\S]+?[ ]{0,3}\d+/[ ]{0,3}\d+\([ ]{0,3}\d+.\d+%\))")


def write_excel_xls(xls_file, result):
    # if os.path.exists(xls_file):
    #     os.remove(xls_file)
    xlwt.XFStyle().alignment.wrap = 1
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Sheet1")
    # headers = result[0].keys()
    headers = ["Case name", "Throughput", "Fail count", "Fail percent", "Lost", "Fail comment", "Counts",  "RTT"]
    for j, title in enumerate(headers):
        sheet.write(0, j, title)
    for i, line in enumerate(result):
        for j, key in enumerate(headers):
            try:
                sheet.write(i+1, j, float(line[key]))
            except ValueError:
                sheet.write(i+1, j, line[key])
    workbook.save(xls_file)

def parse_unit_log(log_file):
    with open(log_file, "rb") as f:
        all_log = f.read()
    cases = PATTERN_ONE_CASE.finditer(all_log)
    results = []
    for case in cases:
        name = case.group(1)
        data = case.group(2)
        throughput = PATTERN_THROUGHPUT.findall(data)
        # fail_percent = PATTERN_FAIL_PERCENT.findall(data)
        fail_count = PATTERN_FAIL_COUNT.findall(data)
        fail_percent = PATTERN_FAIL_PERCENT.findall(data)
        
        counts = PATTERN_COUNTS.findall(data)
        fail_counts = PATTERN_FAIL_COUNTS.findall(data)
        rtt = PATTERN_RTT.findall(data)
        lost = PATTERN_LOST.findall(data)

        parsed_case = {
            "Case name": name, 
            "Throughput": "\n".join(throughput),
            # "Fail percent": "\n".join(fail_percent),
            "Fail count": "\n".join(fail_count),
            "Fail percent": "\n".join(fail_percent),
            "Lost": "\n".join(lost),
            "Counts": "\n".join(counts),
            "RTT": "\n".join(rtt),
            "Fail comment": "\n".join(fail_counts)
            }
        results.append(parsed_case)

    xls_file = os.path.join(os.path.dirname(log_file),"RESULT.xls")
    write_excel_xls(xls_file, results)

    

def main():
    log_file = ''
    try: 
        parser = argparse.ArgumentParser()
        parser.add_argument("log_file")
        args = parser.parse_args()
        log_file = args.log_file
    except SystemExit:
        log_file = UNIT_LOG_FILE

    parse_unit_log(log_file)

if __name__ == "__main__":
    main()