from .noteProjectMain import create_note 

def test_subject_empty():
    assert create_note("01.01.2026","","test_note","test,keyword")[0] == False

