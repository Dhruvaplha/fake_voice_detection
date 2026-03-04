import cv2

image = cv2.imread("/Users/harshraj/Desktop/bright-colours-sawed-wood-indian-holi-festival-colorful-gulal-powder-colors-happy-copy-space-142379853.jpg.webp")

if image is not None:
    h,w,c = image.shape
    print(f"Height: {h}, Width: {w}, Channels: {c}")
else:
    print("Error: could not load image.")