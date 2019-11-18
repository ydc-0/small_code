# -*- coding: utf-8 -*-
import re
import os
from xml.dom import minidom
import argparse

HTML_HEADER_FORMAT = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <style type="text/css">
    table.result{
        font-family: arial;
        font-size: 16px;
        border-spacing: 0;
        border: 1px solid black;
        border-collapse: collapse;
        width: 90%;
        margin-left: 5%;
        margin-right: 5%;
        margin-top: 0.5%;
        text-align: left;
    }
    tr.testcase, td {
        padding: 12px;
        border: 2px solid black;
    }
    th {
        padding: 12px;
        border: 2px solid black;
    }
    td.testsuite {
        color: grey;
        border: 1px solid black;
    }
    div.message {
      text-align: center;
    }
    div.job {
      margin-left: 5%;
      font-size: 20px;
      margin-top: 4%;
    }
    </style>
    <title>Unit Test Report</title>
</head>
<body>
    <div class="message">
        <h2>All Unit Test Results :</h2>
    </div>
'''

HTML_CASE_FILE_FORMAT = '''
    <div class="job">
        From PATH : <b> {}  &nbsp;&nbsp; <a href="{}">Open Xml File</a></b>
    </div>
'''

HTML_TEST_SUITE_FORMAT = '''
    <table class="result">
      <tr><td class="testsuite" colspan="4">test suite: {}</td></tr>
      <tr class="caseheader">
        <th class="name">Case name</th>
        <th class="time">Time (s)</th>
        <th class="result">Result</th>
        <th class="message">Comment</th>
      </tr>
'''

HTML_SINGLE_CASE_FORMAT = '''
      <tr class="testcase" bgcolor="{}">
        <td class="name">{}</td>
        <td class="time">{}</td>
        <td class="result">{}</td>
        <td class="message">{}</td>
      </tr>
'''


RESULT_FILE_NAME = "XUNIT_RESULT.xml"

def get_performance_from_file(case_name, log_path):
    return ""

def parse_unit_report(result_path):

    out_html_file = os.path.join(result_path, "test.html")
    with open(out_html_file, "w+") as f:
        f.write(HTML_HEADER_FORMAT)

    for root, _, files in os.walk(result_path):
        if RESULT_FILE_NAME not in files:
            continue
        result_file = os.path.join(root, RESULT_FILE_NAME)
        with open(out_html_file, "a+") as f:
            job = os.path.relpath(root, result_path)
            relpath = os.path.relpath(result_file, result_path)
            f.write(HTML_CASE_FILE_FORMAT.format(job, relpath))
        
        # open xml file
        DOMTree = minidom.parse(result_file)
        testsuites = DOMTree.documentElement.getElementsByTagName('testsuite')
        
        for testsuite in testsuites:
            if testsuite.nodeName != "testsuite":
                continue
            attrs = {str(k): str(v) for k, v in testsuite.attributes.items()}
            with open(out_html_file, "a+") as f:
                f.write(HTML_TEST_SUITE_FORMAT.format(str(attrs)))

            # parse cases
            for case in testsuite.childNodes:
                if case.nodeName != "testcase":
                    continue

                # name = case.getAttribute("name").encode('utf-8')
                name = str(case.getAttribute("name"))
                # remove config from case name
                # name = re.sub(r'\[\w+\]', '', str(name), count=1)
                time = str(case.getAttribute("time"))
                result = "Pass"
                message = ""
                # message = get_performance_from_file(name, root)
                if case.hasAttribute("log"):
                    message = case.getAttribute("log")
                # failed and skipped cases
                for info in case.childNodes:
                    if info.nodeName == "failure":
                        result = "Fail"
                        message = str(info.getAttribute("message"))
                        break
                    if info.nodeName == "error":
                        result = "Error"
                        message = str(info.getAttribute("message"))
                        break
                    if info.nodeName == "skipped":
                        result = "Skip"
                        message = str(info.getAttribute("message"))
                        break

                print(result, time, name, message)

                RESULT_COLOR = {
                    'Pass': '#f0fff0', # -> light green
                    'Fail': '#ff7d7d', # -> light red
                    'Skip': '#a0a0a0', # -> light gray
                    'Error': 'red',    # -> red
                    }
                color = RESULT_COLOR[result]
                with open(out_html_file, "a+") as f:
                    f.write(HTML_SINGLE_CASE_FORMAT.format(color, name, time, result, message))
            
            with open(out_html_file, "a+") as f:
                f.write('    </table>\n')


def main():
    result_path = ''
    try: 
        parser = argparse.ArgumentParser()
        parser.add_argument("result_path")
        args = parser.parse_args()
        result_path = args.result_path
    except SystemExit:
        idf_path = os.getenv('IDF_PATH')
        if idf_path:
            result_path = os.path.join(idf_path, "TEST_LOGS")
            print("No input path, using default: {}".format(result_path))
        else:
            exit()

    parse_unit_report(result_path)

if __name__ == "__main__":
    main()