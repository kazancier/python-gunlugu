from datetime import datetime
from noteproject.noteProjectMain import create_note, write_note, read_note, return_now

date_ = return_now()
create_status, create_msg = create_note(date_,"","özel not","özel, not" )
my_list = create_msg
msg_ = write_note(my_list,"week9/note.json")
print(msg_)