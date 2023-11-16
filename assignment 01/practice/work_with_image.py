import cv2
import cvzone
img = cv2.imread("imgs/9f0526c4-2ca4-42ed-9e2a-50337870cdc3 - Copy.jpg")
h, w, _ = img.shape
img_r = cv2.resize(img, (int(w*(1/2)), int(h*(1/2))))
print(img_r.shape)


# cutting face
face = img_r[140:265, 130:265]
print(face.shape)
cv2.imwrite("imgs/face.jpg", face)
cv2.imshow(None, face)


# draw rectangle
cv2.rectangle(img_r, (145,120), (255,265), (255, 0, 0), 10)
cv2.imshow(None, img_r)
cv2.imwrite("imgs/rectangle.jpg", img_r)


# change face
face2 = cv2.imread("imgs/glass.png", cv2.IMREAD_UNCHANGED)
face2 = cv2.resize(face2, (135, 125))
face = img_r[140:265, 130:265]
img_r[140:265, 130:265] = cvzone.overlayPNG(face, face2)
cv2.imwrite("imgs/face2.jpg", img_r)
cv2.imshow(None, img_r)
cv2.waitKey(0)
