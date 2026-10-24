from noteproject.noteProjectMain import create_note, write_note, read_note, return_now

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
            if(create_status == True):
                json_note=read_note("note.json")
                json_note.append(create_msg)
                write_status, write_msg =write_note(json_note,my_path)
                print(write_msg)
            else:
                print(create_msg)
        elif first_answer == "N":
            break
        else:
            input("Y/N ?")