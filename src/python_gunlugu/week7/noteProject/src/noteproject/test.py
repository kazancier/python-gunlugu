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



print(create_note("","x","y","z"))
print(create_note("2026-01-01","   ", "y","z"))