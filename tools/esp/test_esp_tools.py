from parse_ie_len import LogParser

def test_file2name():
    assert(LogParser.file_to_name("a.ext") == "a")
    assert(LogParser.file_to_name("C:/a.ext") == "a")
    assert(LogParser.file_to_name("test/a") == "a")
    assert(LogParser.file_to_name(r"test\a.ext") == "a")
