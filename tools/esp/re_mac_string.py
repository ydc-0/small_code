import re

string1 = '''
xxx
'''

string2 = '''
xxxx
'''

mac_list1 = re.findall(r"(\w\w:\w\w:\w\w:\w\w),", string1)
mac_list2 = re.findall(r"(\w\w:\w\w:\w\w:\w\w)\)", string2)

print(mac_list1, mac_list2)

for mac in mac_list2:
    if mac not in mac_list1:
        print(mac, "not in list1")
