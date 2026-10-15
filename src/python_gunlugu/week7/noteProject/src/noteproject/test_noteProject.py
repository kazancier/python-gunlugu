from .noteProjectMain import create_note 

def test_subject_empty():
    assert create_note("01.01.2026","","test_note","test_keyword")[0] == False

def test_subject_exists():
    assert create_note("01.01.2026","test_subject","test_note","test_keyword")[0] == True

