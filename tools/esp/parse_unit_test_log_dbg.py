import argparse
import os
import re
import xlwt
# import pandas as pd


UNIT_LOG_FILE = r"C:\proj\test\utest_script\dual_ttyUSB3.md"
# UNIT_RX_LOG_FILE = r"C:\proj\test\utest_script\dual_ttyUSB1-RX.md"
UNIT_RX_LOG_FILE = r""

PATTERN_ONE_CASE = re.compile(r"Running ([\s\S]+?)\.\.\.([\s\S]+?)PASS")
PATTERN_RX_CASE = re.compile(
    r"Running ([\s\S]+?)[,|(?:\.\.\.)]([\s\S]+?)LAST_END")

# PATTERN_FAIL_PERCENT = re.compile(r"fail:(\d+\(\d+.\d+%\))")
# PATTERN_COUNTS = re.compile(r"((?:enable:\d+)|(?:complete:\d+/?\d{0,10})|(?:success:\d+)|(?:rtt\(max:\d+, min:\d+\)))")
# PATTERN_COUNTS = re.compile(r"((?:enable:\d+)|(?:complete:\d+/?\d{0,10})|(?:success:\d+))")


PATTERNS = [
    ["TX ID",                re.compile(r"psdu\(id:(\d+), ssn:\d+\)")],
    ["TX SSN",               re.compile(r"psdu\(id:\d+, ssn:(\d+)\)")],
]

PATTERNS_MULTI_LINE = [
    ["DBG ID",                re.compile(r"psdum\(id:(\d+), ssn:\d+\)")],
    ["DBG SSN",               re.compile(r"psdum\(id:\d+, ssn:(\d+)\)")],
]


def write_excel_xls(xls_file, result):
    # if os.path.exists(xls_file):
    #     os.remove(xls_file)
    xlwt.XFStyle().alignment.wrap = 1
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Sheet1")
    # headers = result[0].keys()
    headers = ["Case name"]
    headers.extend([key for key, _ in PATTERNS])
    extra_headers = [key for key, _ in PATTERNS_MULTI_LINE]
    extra_col = len(headers)

    for j, title in enumerate(headers):
        sheet.write(0, j, title)
    for j, title in enumerate(extra_headers):
        sheet.write(0, j + extra_col, title)
    current_row = 1
    for _, case in enumerate(result):
        max_line = 1
        for j, key in enumerate(headers):
            try:
                sheet.write(current_row, j, float(case[key]))
            except ValueError:
                sheet.write(current_row, j, case[key])

        for j, key in enumerate(extra_headers):
            if len(case[key]) > max_line:
                max_line = len(case[key])
            for n, raw in enumerate(case[key]):
                try:
                    sheet.write(current_row + n, j + extra_col, float(raw))
                except ValueError:
                    sheet.write(current_row + n, j + extra_col, raw)

        current_row += max_line

    workbook.save(xls_file)


def parse_unit_log(log_file, rx_log_file=""):
    with open(log_file, "rb") as f:
        all_log = f.read()
        all_log = all_log.replace("Running tests matching", "----ignore---")
        all_log = re.sub(
            r"ampdu_count:\d+, psdu\(id:(\d+), ssn:(\d+)\), seqno:\d+,", "psdum(id:\g<1>, ssn:\g<2>)", all_log)
        all_log = re.sub(r"esp_test_tx_process_complete,\d+\] \(test\)aci:\d+, lost Ba/Ack, ampdu_count:\d+, seqno:\d+, psdu\(id:(\d+), ssn:(\d+)\)",
                         "psdum(id:\g<1>, ssn:\g<2>)", all_log)
        all_log = all_log.replace("WDEVRX", "WDEVRX_TX_")
    cases = PATTERN_ONE_CASE.finditer(all_log)

    if rx_log_file:
        with open(rx_log_file, "rb") as f:
            all_rx_log = f.read()
            all_rx_log = all_rx_log.replace(
                "Running tests matching", "----ignore---")
            all_rx_log = all_rx_log.replace(
                "Running RX MAC...", "Running TX MAC...")
            all_rx_log = all_rx_log.replace(
                "Running Set MAC RX", "Running Set MAC TX")
            all_rx_log = all_rx_log.replace(
                "(test)rx, Running", "LAST_END.\n (test)rx, Running")
        rx_cases = PATTERN_RX_CASE.findall(all_rx_log)
    else:
        rx_cases = []

    results = []
    for case in cases:
        name = case.group(1)
        tx_data = case.group(2)

        # Assume rx_cases is less than tx_cases
        # always uses the first match in rx_cases here
        if rx_cases and rx_cases[0][0] == name:
            rx_data = rx_cases[0][1]
            rx_cases = rx_cases[1:]
        elif rx_cases and rx_cases[1][0] == name:
            print("Try to use the second rx case, drop extra rx case {}".format(name))
            rx_data = rx_cases[1][1]
            rx_cases = rx_cases[2:]
        else:
            if rx_log_file:
                print("There's no such case in rx log, case_name:{}".format(name))
            rx_data = ""

        data = tx_data + rx_data
        parsed_case = {"Case name": name}
        for key, pattern in PATTERNS:
            matchs = pattern.findall(data)
            parsed_case.update({key: "\n".join(matchs)})
        for key, pattern in PATTERNS_MULTI_LINE:
            matchs = pattern.findall(data)
            parsed_case.update({key: matchs})
        results.append(parsed_case)

    if rx_cases:
        print("extra rx cases:")
        print(",".join([c[0] for c in rx_cases]))

    xls_file = os.path.join(os.path.dirname(log_file), "RESULT.xls")
    write_excel_xls(xls_file, results)


def main():
    log_file = ''
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("log_file")
        parser.add_argument("-r", "--rx_log_file",
                            help="utest rx log file", default="")
        args = parser.parse_args()
        log_file = args.log_file
        rx_log_file = args.rx_log_file
    except SystemExit:
        log_file = UNIT_LOG_FILE
        rx_log_file = UNIT_RX_LOG_FILE
        print("try to parse {}".format(UNIT_LOG_FILE))

    parse_unit_log(log_file, rx_log_file)


if __name__ == "__main__":
    main()
