def main():
    file_type = input("File name: ").strip().lower()
    extension = file_type.split(".")[-1]
    match extension:
        case "gif" | "jpg" | "jpeg" | "png" | "pdf" | "txt" | "zip":
            print(f"image/{extension}")
        case _:
            print("application/octet-stream")

main()