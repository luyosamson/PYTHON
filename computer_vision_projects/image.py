# import cv2
# image=cv2.imread("sam.png")
# gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# inverted=255-gray_image
# blur=cv2.GaussianBlur(inverted,(21,21),0)
# invertedblur=255-blur
# sketch=cv2.divide(gray_image,invertedblur,scale=256.0)
# cv2.imwrite("sketch_image.png",sketch)
# cv2.imshow("Image",sketch)
import cv2
import os

# Path to the image file
image_path = 'samm.jpg'

# Check if the file exists
if not os.path.isfile(image_path):
    print(f"Error: File '{image_path}' not found.")
else:
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image is loaded
    if image is None:
        print(f"Error: Unable to load the image '{image_path}'.")
    else:
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Save the grayscale image
        gray_image_path = 'gray_image.png'
        cv2.imwrite(gray_image_path, gray_image)
        print(f"Grayscale image saved to '{gray_image_path}'.")

        # Display the grayscale image
        cv2.imshow('Gray Image', gray_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
