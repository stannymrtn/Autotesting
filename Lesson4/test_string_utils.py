from string_utils import StringUtils
import pytest 

string_utils = StringUtils()

@pytest.mark.parametrize('string,result',[('test','Test'),pytest.param('1test','1Test',marks=pytest.mark.xfail),((''),(''))])
def test_capitilize(string,result):
    string_utils = StringUtils()
    test_result = string_utils.capitilize(string)
    assert test_result == result

@pytest.mark.parametrize('string,result',[(' Test','Test'),(' ',''),('','')])
def test_trim(string,result):
    string_utils = StringUtils()
    test_result = string_utils.trim(string)
    assert test_result == result


@pytest.mark.parametrize('string,delimeter,result',[
    ("a,b,c,d", ",", ['a', 'b', 'c', 'd']),        
    ("1:2:3", ":", ['1', '2', '3']),               
    ("", ",", []),                                
    ("test", "/", ['test']),                       
    ("a,,b,,c", ",", ['a', '', 'b', '', 'c']),
    ("a,b,c,d ,e",",",['a','b','c','d ','e']), ])

def test_to_list(string, delimeter, result):
        string_utils = StringUtils()
        test_result = string_utils.to_list(string, delimeter)
        assert test_result == result

@pytest.mark.parametrize('string,value,result',[("Test","s",True),("Test", "U", False),("", "a", False),("Test", "", True),("", "", True)])
def test_contains(string,value,result):
    string_utils = StringUtils()
    test_result = string_utils.contains(string,value)
    assert test_result == result

@pytest.mark.parametrize('string,value,result',[("myValue","e","myValu"),("myValue","my","Value"),("myValue","myValue",""),("myValue","","myValue")])

def test_delete_symbol(string,value,result):
     string_utils = StringUtils()
     test_result = string_utils.delete_symbol(string,value)
     assert test_result == result

@pytest.mark.parametrize('string,value,result',[("Test","T",True),("Test","U",False),("Test","e",False),("Test","Test",True)])
def test_starts_with(string,value,result):
     string_utils = StringUtils()
     test_result = string_utils.starts_with(string,value)
     assert test_result == result

@pytest.mark.parametrize('string,value,result',[("Test","t",True),("Test","U",False),("Test","e",False),("Test","Test",True)])
def test_end_with(string,value,result):
     string_utils = StringUtils()
     test_result = string_utils.end_with(string,value)
     assert test_result == result

@pytest.mark.parametrize('string,result',[("",True),(" ",True),("Test",False),(" Test",False),("Test ",False)])
def test_is_empty(string,result):
     string_utils = StringUtils()
     test_result = string_utils.is_empty(string)
     assert test_result == result

@pytest.mark.parametrize('lst,joiner,result',[([1,2,3,4],",","1,2,3,4"),([1,2,3,4],"/","1/2/3/4"),(["my","Test"],",","my,Test"),(["my","Test"],"/","my/Test")])
def test_list_to_string(lst,joiner,result):
     string_utils = StringUtils()
     test_result = string_utils.list_to_string(lst,joiner)
     assert test_result == result


