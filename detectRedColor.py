import numpy as np
import argparse
import cv2

import anki_vector
import time
from PIL import Image



with anki_vector.Robot(enable_camera_feed=True) as robot:
    for _ in range(30):
        while not robot.camera.latest_image:
            time.sleep(1.0)
        image = robot.camera.latest_image
        #image = image.resize((184,96))
	robot.camera.latest_image.save("temp.png", 'PNG') #check syntax
    
        #screen_data = anki_vector.screen.convert_image_to_screen_data(image)
        
        #robot.screen.set_screen_with_image_data(screen_data, 0.5)
        time.sleep(0.5)

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image")
#args = vars(ap.parse_args())

# load the image
# change based on what path
image = cv2.imread('temp.png')

# define the list of boundaries
# boudnaries for red 
boundaries = [
	([17, 15, 100], [50, 56, 200])
]

#	([86, 31, 4], [220, 88, 50]), green
#	([25, 146, 190], [62, 174, 250]), blue
#	([103, 86, 65], [145, 133, 128]) yellow

# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)
