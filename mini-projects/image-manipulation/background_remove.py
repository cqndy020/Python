from rembg import remove

input_path ='path/to/files'
output_path = 'path/to/files'

with open(input_path, 'rb') as f:
    read_file = f.read()
    remove_bg = remove(read_file)

with open(output_path, 'wb') as x:
    x.write(remove_bg)