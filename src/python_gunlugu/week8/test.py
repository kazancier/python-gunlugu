from datetime import datetime
from noteproject.noteProjectMain import create_note, write_note, read_note, return_now

simdi = datetime.now()
print(simdi)
simdi_ = return_now()
print(simdi_)


veri_dict = {
        "date" : "01.01.2026 10:00", 
        "subject" : "test_subject", 
        "note" : "test_note", 
        "keywords" : "test_keywords"
        }

bool_, msg = write_note(veri_dict,"test_json/")
print(bool_,msg)

"""
def create_note(date,subject,note,keywords):
    if subject != "":
        my_dict = {}
        my_dict["date"] = date
        my_dict["subject"] = subject
        my_dict["note"] = note
        my_dict["keywords"] = keywords
        return (True,my_dict)
        
    else:
        return (False,"Konu boş olduğu için not oluşturulamadı.")

import json
def write_note(veri_dict,dosya_yolu):
    try:
        with open(dosya_yolu,"w",encoding="utf-8") as dosya:
            json.dump(veri_dict,dosya,ensure_ascii=False,indent=4)

        return (True,"Kayıt başarılı")
    except Exception as e:
        return (False,f"Hata: {e}")

print(create_note("","x","y","z"))
print(create_note("2026-01-01","   ", "y","z"))

veri_dict = {
        "date" : "   ", 
        "subject" : "test_subject", 
        "note" : "test_note", 
        "keywords" : "test_keywords"
        }

print(write_note(veri_dict,"/Users/ertugrulkazanci/cld2/python-gunlugu/src/python_gunlugu/week7/noteProject/src/noteProject/notes.json"))


"""