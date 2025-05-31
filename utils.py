def txt_to_list(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        lines = [line for line in lines if line]
    return lines