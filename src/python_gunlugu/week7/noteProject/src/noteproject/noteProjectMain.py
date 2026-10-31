
import json
from datetime import datetime


  
def create_note(date,subject,note,keywords):
    if subject.strip() != "":
        my_dict = {}
        my_dict["date"] = date
        my_dict["subject"] = subject
        my_dict["note"] = note
        my_dict["keywords"] = keywords
        return (True,my_dict)
        
    else:
        return (False,"Konu boş olduğu için not oluşturulamadı.")


def write_note(veri_dict,dosya_yolu):
    try:
        with open(dosya_yolu,"w",encoding="utf-8") as dosya:
            json.dump(veri_dict,dosya,ensure_ascii=False,indent=4)   
        return True,"Dosya başarıyla yazıldı." 
    except FileNotFoundError:
        return False,"Dosya yolu bulunamadı."
    except IsADirectoryError:
        return False,"Bu bir klasör."

def read_note(dosya_yolu):
    try:
        with open(dosya_yolu,"r",encoding="utf-8") as dosya:
            veri = json.load(dosya)
        return True,veri
    except (FileNotFoundError):
        return False, []
    except(json.JSONDecodeError):
        return False, "Dosya bozuk."
        


def return_now():
    now_ = datetime.now()
    format_datetime = "%d-%m-%Y %H:%M"
    str_now_ = now_.strftime(format_datetime)
    return str_now_
