from noteproject.noteProjectMain import create_note 
from noteproject.noteProjectMain import write_note 

def test_subject_empty():
    assert create_note("01.01.2026","","test_note","test_keyword")[0] == False

def test_subject_exists():
    assert create_note("01.01.2026","test_subject","test_note","test_keyword")[0] == True

def test_write_note_directory_missed(tmp_path): 
    dosya = tmp_path / "yok" / " "
    veri_dict = {
        "date" : "01.01.2026", 
        "subject" : "test_subject", 
        "note" : "test_note", 
        "keywords" : "test_keywords"
        }
    assert write_note(veri_dict,dosya)[0] == False
    
def test_subject_whitespace():
    assert create_note("01.01.2026","   ","test_note","test_keyword")[0] == False
