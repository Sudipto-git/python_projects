import cv2

# Load the images
background = cv2.imread('/Users/sudipto/Downloads/image.jpeg')
foreground = cv2.imread('/Users/sudipto/Downloads/tiger.jpeg')

# Resize the foreground image to match the background image
foreground = cv2.resize(foreground, (background.shape[1], background.shape[0]))

# Define the region of interest (ROI) where the foreground image will be placed
x = 100  # X-coordinate of the top-left corner of the ROI
y = 100  # Y-coordinate of the top-left corner of the ROI
h, w = foreground.shape[:2]  # Height and width of the foreground image
roi = background[y:y+h, x:x+w]

# Create a mask of the foreground image
foreground_gray = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(foreground_gray, 10, 255, cv2.THRESH_BINARY)

# Invert the mask
mask_inv = cv2.bitwise_not(mask)

# Apply the mask to the ROI
background_roi = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Apply the foreground image to the ROI
foreground_roi = cv2.bitwise_and(foreground, foreground, mask=mask)

# Combine the background ROI and the foreground ROI
result_roi = cv2.add(background_roi, foreground_roi)

# Update the background image with the combined ROI
background[y:y+h, x:x+w] = result_roi

# Display the result
cv2.imshow('Result', background)
cv2.waitKey(0)
cv2.destroyAllWindows()