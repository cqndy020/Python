import os
from PIL import Image

#to check the current directory
#print(os.getcwd())

#to change the directory
#os.chdir("/path/to/files/")

input_path = '/path/to/filenames/'
output_path = '/path/to/filenames/'

for files in os.listdir(input_path):
    #skip files if files don't have 'jpg' and 'png' format
    if not files.endswith(('.jpg', '.png')):
        pass
    else:
        image_path = os.path.join(input_path, files)
        #open the images and convert to 'RGB' if needed
        image = Image.open(image_path).convert('RGB')
        img_name, ext = os.path.splitext(files)
        output_images = img_name + '.jpeg'
        saving_path = os.path.join(output_path, output_images)
        image.save(saving_path, 'JPEG')
        
        print("Image file converted successfully.")
