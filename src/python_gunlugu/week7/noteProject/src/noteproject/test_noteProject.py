from noteproject.noteProjectMain import create_note, write_note, read_note


veri_dict = {
        "date" : "01.01.2026", 
        "subject" : "test_subject", 
        "note" : "test_note", 
        "keywords" : "test_keywords"
        }

def test_subject_empty():
    assert create_note("01.01.2026","","test_note","test_keyword")[0] == False

def test_subject_exists():
    assert create_note("01.01.2026","test_subject","test_note","test_keyword")[0] == True

def test_write_note_directory_missed(tmp_path): 
    dosya = tmp_path / "yok" / " "
    
    assert write_note(veri_dict,dosya)[0] == False
    
def test_subject_whitespace():
    assert create_note("01.01.2026","   ","test_note","test_keyword")[0] == False

def test_write_note_success(tmp_path):
    dosya = tmp_path / "note.json "
    assert write_note(veri_dict,dosya)[0] == True

def test_read_note_json(tmp_path):
    dosya =tmp_path / "note.json"
    assert read_note(dosya) == "[]"