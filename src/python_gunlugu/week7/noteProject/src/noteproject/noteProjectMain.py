
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


def write_note(veri_dict, dosya_yolu):
  try:
    with open(dosya_yolu, "w", encoding="utf-8") as dosya:
      json.dump(veri_dict, dosya, ensure_ascii=False, indent=4)
    return True, "Veri başarıyla JSON dosyasına yazıldı."
  except Exception as e:
    return False, f"Hata: {str(e)}"