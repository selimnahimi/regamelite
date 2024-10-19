import os

def list_cpp_files(directory):
    cpp_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.cpp', '.c')):
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                cpp_files.append(relative_path)
    return cpp_files

if __name__ == "__main__":
    directory = '.'  # Change this to the directory you want to search
    cpp_files = list_cpp_files(directory)
    for cpp_file in cpp_files:
        print("SRCS+=./" + cpp_file)