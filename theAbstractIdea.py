# this is the abstract idea of the app

# with the help of these libraries  we can process the img and remove the background 
from rembg import remove
from PIL import Image

# the path of the img
inputPath = "D:/do_projects/Github-K0/BG-Remover/tests/inputs/a.jpg"
# the path of the output (the img with the background removed ) 
outputPath = "D:/do_projects/Github-K0/BG-Remover/tests/outputs/a.png"

# getting the img ready to oprate on it 
input = Image.open(inputPath)
# remove the img 
output = remove(input) 
# save the output in the path of the output 
output.save(outputPath)

# all of this will be edited 100% to suit the figma design and the project's idea.