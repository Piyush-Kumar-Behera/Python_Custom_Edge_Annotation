import numpy as np
import cv2
import os

image_list = os.listdir('img_bs/')
images_done = os.listdir('lbl_aj/')

for image_name in image_list:
    if image_name not in images_done:
        image_path_start = 'labels' + '/' + image_name[:-4] + '_image'
        image1 = cv2.imread(image_path_start + str(1) + image_name[-4:])
        image2 = cv2.imread(image_path_start + str(2) + image_name[-4:])
        image3 = cv2.imread(image_path_start + str(3) + image_name[-4:])
        image4 = cv2.imread(image_path_start + str(4) + image_name[-4:])

        image5 = cv2.imread(image_path_start + str(5) + image_name[-4:])
        image6 = cv2.imread(image_path_start + str(6) + image_name[-4:])
        image7 = cv2.imread(image_path_start + str(7) + image_name[-4:])
        image8 = cv2.imread(image_path_start + str(8) + image_name[-4:])

        img_path = 'img_bs/' + image_name
        actual_image = cv2.imread(img_path,1)
        y_dim, x_dim, depth = actual_image.shape
        #print("Image_Name : ", image_name)
        #print(x_dim,',',y_dim, ',', depth)

        y_dim1 = y_dim//4
        y_dim2 = y_dim//2
        y_dim3 = (y_dim * 3)//4
        y_dim4 = y_dim

        x_dim1 = x_dim//2
        x_dim2 = x_dim

        final_image = np.zeros(actual_image.shape, dtype=np.uint8)

        final_image[0:y_dim1,0:x_dim1] = image1
        final_image[y_dim1:y_dim2,0:x_dim1] = image2
        final_image[y_dim2:y_dim3,0:x_dim1] = image3
        final_image[y_dim3:y_dim4,0:x_dim1] = image4

        final_image[0:y_dim1,x_dim1:x_dim2] = image5
        final_image[y_dim1:y_dim2,x_dim1:x_dim2] = image6
        final_image[y_dim2:y_dim3,x_dim1:x_dim2] = image7
        final_image[y_dim3:y_dim4,x_dim1:x_dim2] = image8

        cv2.imwrite('lbl_aj/' + image_name,final_image)
        print("Label Saved Successfully!!")
        #print("Original Shape:", actual_image.shape)
        #print("Final Shape:", final_image.shape)
        cv2.imshow("Label",final_image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
