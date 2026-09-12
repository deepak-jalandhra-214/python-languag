import os
import shutil

def organize_files(folder_path):

    # Folder ke andar saari files/folders ki list
    files = os.listdir(folder_path)

    for file in files:

        # Full path banana
        file_path = os.path.join(folder_path, file)

        # Agar ye folder hai to skip karo
        if os.path.isdir(file_path):
            continue

        # File ka extension nikalna
        extension = os.path.splitext(file)[1].lower()

        # Extension ke according folder decide karna
        if extension in [".jpg", ".jpeg", ".png", ".gif"]:
            folder_name = "Images"

        elif extension in [".mp4", ".mkv", ".avi", ".mov"]:
            folder_name = "Videos"

        elif extension in [".pdf", ".docx", ".doc", ".txt"]:
            folder_name = "Documents"

        elif extension in [".py", ".c", ".cpp", ".java", ".js"]:
            folder_name = "Programming"

        elif extension in [".mp3", ".wav"]:
            folder_name = "Music"

        elif extension in [".zip", ".rar", ".7z"]:
            folder_name = "Archives"

        else:
            folder_name = "Others"

        # Destination folder ka path
        destination_folder = os.path.join(
            folder_path,
            folder_name
        )

        # Folder nahi hai to create karo
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # File ko destination folder mein move karo
        destination_path = os.path.join(
            destination_folder,
            file
        )

        shutil.move(file_path, destination_path)

        print(f"Moved: {file} -> {folder_name}")


folder = input("Enter folder path: ")

if os.path.exists(folder) and os.path.isdir(folder):
    organize_files(folder)
    print("\nFiles organized successfully!")
else:
    print("Invalid folder path!")