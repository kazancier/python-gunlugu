from noteproject.noteProjectMain import create_note, write_note, read_note, return_now,return_now_for
from pathlib import Path

def main() -> None:

    my_path="note.json"
    while True: 
        first_answer = input("Not eklemek ister misin? \n Y/N ? ")
        json_note =[]
        if first_answer == "Y":
            subject_ = input("subject: ")
            note_ = input("note: ")
            keywords_ = input("keywords: ")
            date_ = return_now()
            create_status, create_msg = create_note(date_,subject_,note_,keywords_)
            if(create_status):
                read_status=read_note("note.json")[0]
                json_note=read_note("note.json")[1]
                if read_status:             
                    json_note.append(create_msg)
                    write_status, write_msg =write_note(json_note,my_path)
                    print(write_msg)
                else:
                    if json_note == []:
                        json_note.append(create_msg)
                        write_status, write_msg =write_note(json_note,my_path)
                        print(write_msg)
                    else:
                        json_note = []
                        json_note.append(create_msg)
                        new_name ="note"+return_now_for()+".json"
                        my_path = Path("note.json")
                        my_path.rename(new_name)
                        write_status, write_msg =write_note(json_note,my_path)
                        print(write_msg)
                        print(json_note)


            else:
                print(create_msg)
        elif first_answer == "N":
            break
        else:
            input("Y/N ?")