# MineClicker
MineClicker is a game on Scratch I made. Here is the link to the project: https://scratch.mit.edu/projects/779674338/

I wrote a little python program to generate the layers for me. Maybe you need it too so thats why i decided to publish it in GitHub.

# How to use the program
For the program to work you will need the python biblithek "Pillow". Its a biblithek which can create images from your code.

If yo jsut want to generate image-rows, you can ignore the upper method. It is the one which uses Pillow.

In the second method, you can find a few variables: "inputFolder", "outputFolder", "background", "otherImages" and "coverage". They are used to give the program the information on where to put the images and what images are they made of.

# "iputFolder"
Set "inputFolder" to the folder where your start images are located at, in my case the minecraft textures. Remember to put a "/" at the end (eg: inputFolder/) or leave blank when the images are in the same folder as the program.

# "outputFolder"
Same rules as for the "inputFolder". This is the folder the image rows will be put in after generating.

# "background"
The "background" variable contains the name of the main image you want to display. Do not include the ending (eg: ".png"). The program automaticly adds it.

# "otherImages"
This is a list of all the other images which can replace the background for a certin possibility. All images in the list have the same possibility to appear. Do not include the ending of the image in here as well. Formate the list like a standart python list (eg: ["dirt", "stone"]).

# "coverage"
This is the percantage of a image in "otherImages" to replace the background. Enter a number between 0 and 100. 0 means that you dont want to replace any images.
