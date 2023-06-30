from PIL import Image, ImageFilter

input_path = "path/to/files"
output_path = "path/to/files"

open_file = Image.open(input_path)
blurring = open_file.filter(ImageFilter.BLUR)

#if you want to adject blurring level, you can use with changing the radius
#radius_level = 10
#blurring = open_file.filter(ImageFilter.GaussianBlur(radius_level))

with open(output_path, 'wb') as f:
    blurring.save(f)