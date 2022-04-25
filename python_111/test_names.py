from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name("Anna", "Harrison") == "Harrison; Anna"
    assert make_full_name("William", "Harrison") == "Harrison; William"
    assert make_full_name("George", "Washington") == "Washington; George"
    assert make_full_name("Martha", "Washington") == "Washington; Martha"
 
def test_extract_family_name():
    assert extract_family_name("Harrison; Anna") == "Harrison"
    assert extract_family_name("Harrison; William") == "Harrison"
    assert extract_family_name("Washington; George") == "Washington"
    assert extract_family_name("Washington; Martha") == "Washington"

def test_extract_given_name():
    assert extract_given_name("Harrison; Anna") == "Anna"
    assert extract_given_name("Harrison; William") == "William"
    assert extract_given_name("Harrison; George") == "George"
    assert extract_given_name("Harrison; Martha") == "Martha"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
