from noteproject.noteProjectMain import create_note, write_note, read_note, return_now
from datetime import datetime
import json

veri_dict = {
        "date" : "01.01.2026 10:00", 
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


def test_write_note_is_directory(tmp_path): 
    dosya = tmp_path
    
    assert write_note(veri_dict,dosya)[0] == False

def test_subject_whitespace():
    assert create_note("01.01.2026","   ","test_note","test_keyword")[0] == False

def test_write_note_success(tmp_path):
    dosya = tmp_path / "note.json "
    assert write_note([veri_dict],dosya)[0] == True

def test_read_note_json(tmp_path):
    dosya =tmp_path / "note.json"
    assert read_note(dosya)[1] == []

def test_read_write_ifequals(tmp_path):
    dosya =tmp_path / "note.json"
    write_note([veri_dict],dosya)
    assert read_note(dosya)[1] == [veri_dict]

def test_return_now_check():
    format_datetime = "%d-%m-%Y %H:%M"
    str_now=return_now()
    assert datetime.strptime(str_now,format_datetime)

def test_invalid_json(tmp_path):
    dosya = tmp_path / "invalid.json"
    invalid_json_content = '{ "date" : "01.01.2026", "subject" : "özel", "note": "özel not" "keyword" : "özel, not" } '
    dosya.write_text(invalid_json_content, encoding="utf-8")
    read_note(dosya)[0] == False