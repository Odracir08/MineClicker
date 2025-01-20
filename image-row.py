from PIL import Image
from random import randint

#Method for generating the image-row
def create_image_row(image_paths, output_file):
    images = [Image.open(img_path) for img_path in image_paths]
    
    total_width = sum(img.width for img in images) + 2
    max_height = max(img.height for img in images) + 2
    
    result = Image.new("RGBA", (total_width, max_height), (0, 0, 0, 255))
    
    x_offset = 1
    for img in images:
        result.paste(img, (x_offset, 1))
        x_offset += img.width
    
    result.save(output_file)
    print(f"Bild erfolgreich gespeichert als: {output_file}")


#Method for creating all the files
def generate_files():
    image_files = []

    inputFolder = ""    #Path of input folder (eg: "blocks/")
    outputFolder = ""   #Path of output folder (eg: "output-images/")
    background = ""     #The main Image you want to display (eg: "dirt")
    otherImages = [""]  #All the other images which can overlay your background (as a list)
    coverage = 0        #The percantage of getting a replace image (in percent)

    for i in range(41): #Number of imgages generated in a row
        if (randint(1, 100) < coverage):
            image_files.append(inputFolder + otherImages[randint(0, len(otherImages) - 1)] + ".png")
        else:
            image_files.append(inputFolder + background + ".png")

    output_path = outputFolder+background+"-with-"+str(coverage)+"-of-"+str(otherImages)+".png"

    create_image_row(image_files, output_path)


#Start of code
generate_files()
