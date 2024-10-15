import os


file_list= [] 
dir_list= []  
main_dir = 'path/to/directory'

def ls_files(repertoire):
    for racine, repertoires, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            add_to(os.path.join(racine, fichier), file_list)
        add_to(racine, dir_list)

def add_to(file, ls: []): 
    ls.append(file)

def move_to(file, dir): 
    dir_path = os.path.join(main_dir, dir)
    print(dir_path)
    if os.path.exists(file) and os.path.exists(dir_path):
        try:
            destination = os.path.join(dir_path, os.path.basename(file))
            os.replace(file, destination)
            print(f"Moved {file} to {destination}")
        except PermissionError as e : 
             print(f"Permission error: {str(e)}. Check your permissions.")
        except Exception as e : 
            print(f"Error moving {file}: {str(e)}")
        else : 
            print(f"File or directory does not exist: {file}, {dir}")
    else : 
        print("rien")

def create_dir_if_not_exists(dir_name): 
    dir_path = os.path.join(main_dir, dir_name)
    if not os.path.exists(dir_path):
        try:
            os.mkdir(dir_path)
            print(f"Directory '{dir_name}' created successfully.")
        except FileExistsError:
            print(f"Directory '{dir_name}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{dir_name}'.")
        except Exception as e:
            print(f"An error occurred: {e}")

def organize(): 
    create_dir_if_not_exists("Documents")
    create_dir_if_not_exists("Pdfs")
    create_dir_if_not_exists("Presentations")
    create_dir_if_not_exists("Text_files")
    create_dir_if_not_exists("Others")
    
    for i in range(len(file_list_name)): 
        ext= file_list_name[i].split('.')[-1]
        match ext: 
            case "pdf": 
                move_to(file_list[i], "Pdfs")
            case "txt": 
                move_to(file_list[i], "Text_files")
            case "pptx": 
                move_to(file_list[i], "Presentations")
            case "docx": 
                move_to(file_list[i], "Documents")
            case _:                     
                move_to(file_list[i], "Others")


if __name__ == "__main__":

    ls_files(main_dir)
    dir_list_name = [dir.split('\\')[-1] for dir in dir_list if dir != main_dir]
    file_list_name= [dir.split('\\')[-1] for dir in file_list] 
    print(dir_list)
    organize()