import cv2

image = cv2.imread("/Users/harshraj/Desktop/bright-colours-sawed-wood-indian-holi-festival-colorful-gulal-powder-colors-happy-copy-space-142379853.jpg.webp")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: could not load image.")