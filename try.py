import cv2

img = cv2.imread("C:/Users/MASTER/Pictures/Camera Roll/WIN_20191105_23_05_58_Pro.jpg", cv2.IMREAD_UNCHANGED)

print('Original Dimensions : ',img.shape)
 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blured = cv2.GaussianBlur(gray, (5, 5), 0)
blured = cv2.erode(blured, None, iterations=2)
blured = cv2.dilate(blured, None, iterations=2)
high_thresh, thresh_im = cv2.threshold(blured, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
high_thresh2=high_thresh*0.5
low_thresh = 0.1*high_thresh
edged=~img

edged=cv2.Canny(edged,200,20)
model_image =edged
model_image = cv2.resize(model_image,dsize=(200,200),interpolation=cv2.INTER_CUBIC)
 
print('Resized Dimensions : ',model_image.shape)
 
cv2.imshow("Resized image", model_image)
cv2.waitKey(0)
cv2.destroyAllWindows()