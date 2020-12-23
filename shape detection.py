import cv2
import numpy as np

def nothing(x):
    pass

video = cv2.VideoCapture(0)

desiredWidth=700
desiredheight=0
cv2.namedWindow("Trackbars", cv2.WINDOW_AUTOSIZE)

cv2.createTrackbar("L-H", "Trackbars", 0, 180, nothing)
cv2.createTrackbar("L-S", "Trackbars", 145, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 143, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 180, 180, nothing)
cv2.createTrackbar("U-S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 243, 255, nothing)

cv2.resizeWindow("Trackbars", desiredWidth,desiredheight)

font = cv2.FONT_HERSHEY_COMPLEX

while True:
    ret, kare = video.read()
    hsv = cv2.cvtColor(kare, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")

    lower_red = np.array([l_h, l_s, l_v])
    upper_red = np.array([u_h, u_s, u_v])

    maske = cv2.inRange(hsv, lower_red, upper_red)
    kontur, _ = cv2.findContours(maske, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for cnt in kontur:
        alan = cv2.contourArea(cnt, )
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        if alan > 100:
            cv2.drawContours(kare, [approx], 0, (0, 255, 0), 3)
            cv2.putText(kare, "Hedef Bulundu", (0,85), font, 1, (255,0,0))
            if 5 < len(approx) < 15:
                cv2.putText(kare, "Hedef Alan", (x, y), font, 1, (255, 255, 255))
                print("Hedef Alan")
             


    cv2.imshow("Video", kare)
    cv2.imshow("Maske", maske)


    key = cv2.waitKey(1)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()