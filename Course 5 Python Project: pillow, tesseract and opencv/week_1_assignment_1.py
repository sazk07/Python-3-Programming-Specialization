import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFont, ImageDraw

# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')
# build a list of 9 images which have different brightnesses
enhancer=ImageEnhance.Brightness(image)
images=[enhancer.enhance(iterable/10) for iterable in range(1,10)]
# create a contact sheet from different brightnesses
first_image=images[0]
width_times_3=first_image.width*3
manipulate_height=first_image.height*3
contact_sheet=PIL.Image.new(first_image.mode, (width_times_3,manipulate_height))
x=0
y=0
sheet_width=contact_sheet.width
for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y))
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width==sheet_width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width
# resize and display the contact sheet
half_width=contact_sheet.width/2
half_height=contact_sheet.height/2
resized=(int(half_width),int(half_height))
contact_sheet=contact_sheet.resize(resized)
display(contact_sheet)
# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')
# build a list of 9 images which have different color
images=list()
labels=list()
for i in range(3):
    for intensity in (0.1,0.5,0.9):
        source=image.split()
        mid=source[i].point(lambda x:x*int(intensity))
        source[i].paste(mid)
        mode_ = image.mode
        im=Image.merge(mode_, source)
        labels.append(f"channel {i} intensity {intensity}")
        images.append(im)
font = ImageFont.truetype("fonts/times.ttf",75)
# create a contact sheet from different color
first_image=images[0]
manipulate_height2=first_image.height*3+3*85
first_image_mode=first_image.mode
contact_sheet=PIL.Image.new(first_image_mode, (width_times_3,manipulate_height2))
x=0
y=0
draw=ImageDraw.Draw(contact_sheet)
for label,img in enumerate(images):
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y))
    add_height=first_image.height+5
    draw.text((x,y+add_height), labels[label], font=font)
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width==sheet_width:
        x=0
        y=y+first_image.height+85
    else:
        x=x+first_image.width
# resize and display the contact sheet
contact_sheet=contact_sheet.resize(resized)
display(contact_sheet)
