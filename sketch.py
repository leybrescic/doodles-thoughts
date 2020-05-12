import cv2


def dodge(image, mask):
    return cv2.divide(image, 255 - mask, scale=256)

cam = cv2.VideoCapture(0)
cv2.namedWindow("Webcam to sketch")
while True:
    ret, frame = cam.read()
    cv2.imshow("Webcam to sketch", frame)
    if not ret:
        break
    k = cv2.waitKey(1)
    if k%256 == 32:
        img_name = "picture.jpg"
        cv2.imwrite(img_name, frame)
        break

cam.release()

img = cv2.imread('picture.jpg', 1)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_invert = cv2.bitwise_not(img_gray)
img_blur = cv2.blur(img_invert, (10, 10))

final_img = dodge(img_gray, img_blur)

cv2.imshow('Webcam to sketch', final_img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('sketch.png', final_img)
    cv2.destroyAllWindows()