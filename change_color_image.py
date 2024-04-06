import cv2

def change_color(image_path, new_color):
    # Load the image
    image = cv2.imread("/Users/sudipto/Downloads/image.jpeg")

    # Convert the image to the desired color
    new_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the original and new image
    cv2.imshow("Original Image", image)
    cv2.imshow("New Image", new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Path to the image file
image_path = "/path/to/your/image.jpg"

# Color conversion code (e.g., cv2.COLOR_BGR2GRAY for grayscale)
new_color = cv2.COLOR_BGR2GRAY

# Call the function to change the color of the image
change_color(image_path, new_color)