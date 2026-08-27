def main():
    file_type = input("File name: ").strip().lower()
    extension = file_type.split(".")[-1]
    match extension:
        case "gif" | "jpeg" | "png" :
            print(f"image/{extension}")
        case "jpg" :
            print("image/jpeg")
        case "pdf" | "zip" :
            print(f"application/{extension}")
        case "txt" :
            print("text/plain")
        case _:
            print("application/octet-stream")

main()