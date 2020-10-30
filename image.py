from wand.image import Image
from wand.display import display
import uuid

default_left = 70
default_top = 190

def generate_image(left=70, top=190):
    myuuid = str(uuid.uuid4())
    with Image(filename='assets/level.png') as level_img:
        with Image(filename='assets/run1.gif') as run_img:
            level_img.composite(run_img, left, top)
            level_img.format = 'jpeg'
            level_img.save(filename='assets/generated/' + myuuid + '.png')
    return myuuid

def move_token(direction):
    myuuid = ''
    if direction == 'right':
        myuuid = generate_image(default_left + 16)
    return myuuid
