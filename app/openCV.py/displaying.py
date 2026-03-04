import cv2

image = cv2.imread("/Users/harshraj/Desktop/bright-colours-sawed-wood-indian-holi-festival-colorful-gulal-powder-colors-happy-copy-space-142379853.jpg.webp")

if image is not None:
    cv2.imshow("Image Showing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: could not load image.")