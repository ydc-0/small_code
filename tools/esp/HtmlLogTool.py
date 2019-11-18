# -*- coding: utf-8 -*-
import re
import os
import sys
import shutil
import argparse

HTML_LOG_FILE = "ESP32.MESH_EST_6001_29200959_001.html"
# HTML_LOG_FILE = ""
OUT_FOLDER = None


def parse_html_to_single_log(args):
    html_file = args.html_file
    out_folder = args.out_folder
    append = args.append
    formats = args.format

    html_file = os.path.abspath(html_file)
    if not os.path.exists(html_file) or not os.path.isfile(html_file):
        print("file: %s not exists" % html_file)
        sys.exit(1)

    if not out_folder:
        out_folder, _ = os.path.splitext(html_file)
    if not append and os.path.exists(out_folder):
        shutil.rmtree(out_folder)
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)

    pattern = r'''
    <tr[\S\s]+?>                     # start, example: <tr class="DUT1" id="1">
    <td>(\d+)(?:</td>)?              # index : <td>1</td> or <td>1
    <td>([\S\s]+?)(?:</td>)?         # time
    <td>(\w+?)(?:</td>)?             # port name
    <td><pre>([\S\s]*?)              # data
    </pre></td></tr>                 # the end
    '''
    regex = re.compile(pattern, re.VERBOSE)
    all_log_string = ""
    with open(html_file, "rb") as f:
        all_log_string = f.read().decode("utf8", "ignore")

    matchs = regex.finditer(all_log_string)
    for match in matchs:
        # index = int(match.group(1))
        time_str = match.group(2)
        port_name = match.group(3)
        data = match.group(4)
        data = data.replace(r"&lt;", r"<").replace(
            "&gt;", ">").replace("&amp;", "&").replace("&quot;", "\"")
        log_file_name = os.path.join(out_folder, "%s.log" % port_name)
        # appending to the object file
        with open(log_file_name, "ab+") as f:
            if formats == "data_only":
                write_string = "%s" % data
            else:
                write_string = "[%s]\r\n%s\r\n" % (time_str, data)
            f.write(write_string.encode('utf-8'))


def main():
    if HTML_LOG_FILE:
        args = argparse.Namespace(
            html_file=HTML_LOG_FILE, out_folder=OUT_FOLDER, append=None, format="time_data")
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument("html_file")
        parser.add_argument("-o", "--out_folder",
                            help="folder for the log output", default="")
        parser.add_argument("-t", "--format",
                            choices=["time_data", "data_only"], default="time_data")
        parser.add_argument("-a", "--append",
                            help='append new data if the file already exists', action="store_true")

        args = parser.parse_args()

    parse_html_to_single_log(args)


if __name__ == '__main__':
    main()
