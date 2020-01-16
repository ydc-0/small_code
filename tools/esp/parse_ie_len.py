# -*- coding: utf-8 -*-
import os
import re

fills = [[' ', '█'], ['▏', '▎', '▍', '▌', '▋', '▊', '▉']]
sampling_interval_s = 1
OUT_PUT_FILE = "/home/test/debug/result-60s.html"
HTML_HEAD = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Microsoft/vscode/extensions/markdown-language-features/media/markdown.css" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Microsoft/vscode/extensions/markdown-language-features/media/highlight.css" />
    <style type="text/css">
        p,pre {margin-left: 2em;}
    </style>
</head>
<body class="vscode-light">
<div>
<h1>Meanings</h1>
<p>
"-" -> no roots ie <br>
"█" -> ROOT has roots ie (connected with router)<br>
"#" -> NODE has roots ie <br>
"↓md" -> mesh_deint <br>
"↓s"  -> mesh start <br>
"↓ctr" -> connected to router <br>
"↓cwr" -> connected with router <br>
"↓r2n" -> root becomes node (deauth child with reason 104) <br>
"↓yld" -> root becomes node (asked yield) <br><br>
"one_root_time" -> from case start (different with the time stamp) <br>
"ie_clear_time" -> from one_root to roots ie clear <br>
</p>
<h2>Configurations</h1>
<p>
ie close time: 60 s <br>
network stable_time: 60 s <br>
one_root_time is always greater than 30s, beacuse there's 30s delay after case start. <br>
</p>
</div>
'''


MAX_TIME_S = 2000


class NodeSimulater(object):
    def __init__(self, node_name, log_file, step=1):
        self.step = step
        self.name = node_name
        self.ie_len = []
        self.last_close = 0
        self.log_file = log_file
        self.ie_clear_time = 0
        self.all_log_lines = []
        self.ssid = "None"
        self.actions = []
        self.is_root = []

    def update_open_close(self, action, type="fixed"):
        # action: 'open' & 'close'
        # type: 'fixed' & gone
        pass

    def _init_ie_length(self, time_s):
        self.ie_len = [0 for i in range(time_s//self.step)]

    def _update_ie_length(self, time, ie_len):
        index = time//self.step
        self.ie_len[index] = ie_len
        if ie_len:
            self.ie_clear_time = min(time + 5, MAX_TIME_S)

    def _read_all_log(self):
        if self.all_log_lines:
            return
        with open(self.log_file) as f:
            self.all_log_lines = f.readlines()

    def parse_ie_length(self):
        self._read_all_log()
        self._init_ie_length(MAX_TIME_S)
        pattern = re.compile(
            r'\((\d+)\) wifi: ieee80211_add_mesh_roots_ie:(\d+) \((\d+\+\d+\+\d+\+\d+)\)')
        for line in self.all_log_lines:
            match = pattern.search(line)
            if not match:
                continue
            time_stamp = int(match.group(1))//1000
            if time_stamp >= MAX_TIME_S:
                print("ignore more than {:d} s".format(MAX_TIME_S))
                break
            ie_len = int(match.group(2))
            details = match.group(3)
            self._update_ie_length(time_stamp, ie_len)

    def _get_time_stamp(self, index, previous=False):
        pattern = re.compile(r"[IEW] \((\d+)\)")
        step = -1 if previous else 1
        match = None
        while not match:
            match = pattern.search(self.all_log_lines[index])
            index += step
        return int(match.group(1))//1000

    def parse_actions(self):
        self._read_all_log()
        patterns = [
            (re.compile(r'\((\d+)\) mesh: \[DONE\]connect to router'), "ctr"),
            (re.compile(r'\((\d+)\) wifi: connected with TP-LINK_945D'), "cwr"),
            (re.compile(
                r'\((\d+)\) mesh: 330\[L:\d+\]deauth aid:\d+, mac:[\w:]+, reason:104'), "r2n"),
            (re.compile(r'\((\d+)\) mesh: 377<stop>'), "md"),
          
        ]
        for i, line in enumerate(self.all_log_lines):
            for pattern, description in patterns:
                match = pattern.search(line)
                if not match:
                    continue
                time_stamp = int(match.group(1))//1000
                if time_stamp >= MAX_TIME_S:
                    break
                self.actions.append((time_stamp, description))
            # extra
            if line.find("MESH_EVENT_ROOT_ASKED_YIELD") != -1:
                self.actions.append((self._get_time_stamp(i), "yld"))
            if line.find("MESH_EVENT_STARTED") != -1:
                self.actions.append((self._get_time_stamp(i), "s"))


        self.is_root = [0 for i in range(MAX_TIME_S//self.step)]
        for time_stamp, action in self.actions:
            if action == "cwr":
                for i in range(time_stamp, MAX_TIME_S//self.step):
                    self.is_root[i] = 1
            if action == "r2n" or action == "yld":
                for i in range(time_stamp, MAX_TIME_S//self.step):
                    self.is_root[i] = 0

    def parse_map_ssid(self):
        self._read_all_log()
        pattern = re.compile(r'wifi: mode : sta \(([\w:]+)\)')
        for line in self.all_log_lines:
            match = pattern.search(line)
            if match:
                mac = match.group(1)
                ssid = "ESPM_" + mac.replace(":", "")[-6:].upper()
                return

    def parse_map_ssid(self):
        self._read_all_log()
        pattern = re.compile(r'wifi: mode : sta \(([\w:]+)\)')
        for line in self.all_log_lines:
            match = pattern.search(line)
            if match:
                mac = match.group(1)
                ssid = "ESPM_" + mac.replace(":", "")[-6:].upper()
                return

    def get_status_character(self, time_stamp):
        if not self.ie_len[time_stamp]:
            return "-"
        elif self.is_root[time_stamp]:
            return "█"
        else:
            # return "⣿"
            return "#"


class LogParser(object):
    def __init__(self, log_path):
        self.log_path = log_path
        self.nodes = {}
        self.case_name = "CASE"
        self.initialization()

    @staticmethod
    def file_to_name(path):
        _, file_name = os.path.split(path)
        return os.path.splitext(file_name)[0]

    def initialization(self):
        self.case_name = os.path.basename(self.log_path)
        for path, dir_list, file_list in os.walk(self.log_path):
            # print(path,dir_list,file_list)
            for file_name in file_list:
                node_name = self.file_to_name(file_name)
                log_file = os.path.join(path, file_name)
                self.nodes.update(
                    {node_name: NodeSimulater(node_name, log_file)})

    def parse_open_close_time(self):
        pass

    def _init_html_file(self, html_file):
        if not os.path.exists(html_file):
            with open(html_file, "wt", encoding="utf-8") as f:
                print(HTML_HEAD, file=f)

    def print_to_html(self, html_file, details):
        self._init_html_file(html_file)
        # print to html
        ports = sorted(self.nodes.keys(), key=lambda x: int(x[3:]))
        effective_time_s = max([n.ie_clear_time for n in self.nodes.values()])
        with open(html_file, "at", encoding='utf-8') as f:
            print("<div><h1>{}</h1>".format(self.case_name), file=f)
            print("<p>{}</p>".format(details), file=f)
            print("<pre><code><code><div>", file=f)

            print("time(s) :" + "".join(["↓{:<9d}".format(i)
                                         for i in range(0, effective_time_s, 10)]), file=f)
            for port in ports:
                # print("         " + "".join(["↓{:<9d}".format(i) for i in range(0,effective_time_s,10)]), file=f)
                format_str = " " * effective_time_s
                for index, action in self.nodes[port].actions:
                    format_str = format_str[:index] + "↓" + \
                        action + format_str[index+len(action)+1:]
                print("         " + format_str, file=f)
                # format_str = "".join(["█" if i else "_" for i in self.nodes[port].ie_len[:effective_time_s]])
                format_str = "".join(
                    [self.nodes[port].get_status_character(i) for i in range(effective_time_s)])
                print("{:8s}:".format(port) + format_str, file=f)
            print("</div></code></code></pre></div>", file=f)

    def parse_ie_length(self, details="", out_file=OUT_PUT_FILE):
        for _, node in self.nodes.items():
            node.parse_ie_length()
            node.parse_map_ssid()
            node.parse_actions()
        # self.print_to_markdown(out_file)
        self.print_to_html(out_file, details)


SOURCES = [
    # ("establish: one_root_time: 200.93, ie_clear_time: 33.73 <br> destroy: one_root_time: 30.49, ie_clear_time: 197.93 ", r"/home/test/debug/tc_log/MESH_EST_6103_01_02053016"),
    # ("establish: one_root_time: 269.95, ie_clear_time: 54.56 <br> destroy: one_root_time: 30.30, ie_clear_time: 0.17 ", r"/home/test/debug/tc_log/MESH_EST_6102_01_02085713"),
    # ("one_root_time: 856.19, ie_clear_time: 27.43", r"/home/test/debug/tc_log/MESH_EST_6003_01_03155503"),
    # ("one_root_time: 660.01, ie_clear_time: 42.90", r"/home/test/debug/tc_log/MESH_EST_6004_01_01222924"),
    # ("one_root_time: 215.71, ie_clear_time: 166.13", r"/home/test/debug/tc_log/MESH_EST_6002_01_02054607"),
    ("one_root_time: 194.32, ie_clear_time: 357.40", r"/home/test/debug/60s/tc_log/MESH_EST_6001_01_29105241"),

]
for details, path in SOURCES:
    parser = LogParser(path)
    parser.parse_ie_length(details)
