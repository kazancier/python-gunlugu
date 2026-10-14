
def create_note(date,subject,note,keywords):
    if subject != "":
        my_dict = {}
        my_dict["date"] = date
        my_dict["subject"] = subject
        my_dict["note"] = note
        my_dict["keywords"] = keywords
        return my_dict
        
    else:
        return (False,"Not oluşturulamadı")

