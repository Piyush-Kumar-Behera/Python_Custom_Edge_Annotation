import numpy as np
import cv2
import os

color_bgr = (0,255,255)
img_name = 'image.png'
img_path = 'images/' + img_name

label_flag = False
label_img_flag = False

labels_list = os.listdir('labels/')
labels_img_list = os.listdir('on_img_labels/')

#print(labels_list)
#print(labels_img_list)

if ('lb_' + img_name) in labels_list:
    label_flag = True

if ('lb_img_' + img_name) in labels_img_list:
    label_img_flag = True

label_path = 'labels/' + 'lb_' + img_name
label_img_path = 'on_img_labels/' + 'lb_img_' + img_name

image = cv2.imread(img_path,1)


if label_flag == True:
    lbl = cv2.imread(label_path)
else:
    lbl = np.zeros(image.shape,dtype = np.uint8)

if label_img_flag == True:
    lbl_img = cv2.imread(label_img_path)
else:
    lbl_img = image


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points_in_continuity) == 0 or lbl_break_flag[-1] == True:
            lbl_break_flag.append(False)
            cv2.circle(lbl_img, (x,y), 2, color_bgr, -1)
            cv2.circle(lbl, (x,y), 2, (255,255,255), -1)
            points_in_continuity.append((x,y))
            #print(points_in_continuity)
        else:
            cv2.line(lbl_img, points_in_continuity[-1], (x,y), color_bgr, 4)
            cv2.line(lbl, points_in_continuity[-1], (x,y), (255,255,255), 4)
            points_in_continuity.append((x,y))
            #print(points_in_continuity)

    if event == cv2.EVENT_RBUTTONDOWN or event == cv2.EVENT_MBUTTONDOWN:
        lbl_break_flag.append(True)
        points_in_continuity.append((-1,-1))

    cv2.imshow('Label_Window',lbl_img)
    cv2.imshow('Label',lbl)


cv2.imshow('Label_Window',lbl_img)
cv2.imshow('Label',lbl)

points_in_continuity = []
lbl_break_flag = []
lbl_break_flag.append(False)
cv2.setMouseCallback('Label_Window',click_event)
#cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Enter 1 to save annotation")
print("Enter 2 to undo")
print("Enter 0 to exit without saving annotation")

num = int(input())

def save_image(loc,image_name,image):
    image_path = loc + '/' + image_name
    cv2.imwrite(image_path, image)

if num == 1:
    save_image("on_img_labels",img_name,lbl_img)
    save_image("labels",img_name,lbl)
    print('Images saved successfully in respective folders!')

elif num == 2:
    lbl_img_undo = cv2.imread(img_path,1)
    lbl_undo = np.zeros(image.shape,dtype = np.uint8)
    discon_flag = True
    print("How many steps to undo? ")
    undo_steps = int(input())
    for i in range(len(points_in_continuity) - undo_steps):
        if points_in_continuity[i] == (-1,-1):
            discon_flag = True
            continue
        if discon_flag:
            cv2.circle(lbl_img_undo, points_in_continuity[i], 2, color_bgr, -1)
            cv2.circle(lbl_undo, points_in_continuity[i], 2, (255,255,255), -1)
            discon_flag = False
        else:
            cv2.line(lbl_img_undo, points_in_continuity[i-1], points_in_continuity[i], color_bgr, 4)
            cv2.line(lbl_undo, points_in_continuity[i-1], points_in_continuity[i], (255,255,255), 4)
    print("Successfully undone!! Undone images are shown...")
    cv2.imshow('Label_Window',lbl_img_undo)
    cv2.imshow('Label',lbl_undo)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    save_image("on_img_labels",img_name,lbl_img_undo)
    save_image("labels",img_name,lbl_undo)

    print("Images(Undone) saved successfully in respective folders!")

elif num == 0:
    print("Files not saved!!")
