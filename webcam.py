import cv2

imgcapture = cv2.VideoCapture(0)
result = True
while(result):
    ret,frame = imgcapture.read()
    cv2.imwrite("rish.jpg", frame)
    result=False
    print("image captured.....")
imgcapture.release()
