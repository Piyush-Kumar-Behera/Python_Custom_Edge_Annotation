import numpy as np
import cv2
import os

image_list = os.listdir('img_bs/')

for image_name in image_list:
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


    image1 = actual_image[0:y_dim1,0:x_dim1]
    image2 = actual_image[y_dim1:y_dim2,0:x_dim1]
    image3 = actual_image[y_dim2:y_dim3,0:x_dim1]
    image4 = actual_image[y_dim3:y_dim4,0:x_dim1]

    image5 = actual_image[0:y_dim1,x_dim1:x_dim2]
    image6 = actual_image[y_dim1:y_dim2,x_dim1:x_dim2]
    image7 = actual_image[y_dim2:y_dim3,x_dim1:x_dim2]
    image8 = actual_image[y_dim3:y_dim4,x_dim1:x_dim2]


    def save_image(loc,image_name,image,index):
        image_path = loc + '/' + image_name[:-4] + '_image' + str(index) + image_name[-4:]
        cv2.imwrite(image_path, image)


    save_image('images',image_name,image1,1)
    save_image('images',image_name,image2,2)
    save_image('images',image_name,image3,3)
    save_image('images',image_name,image4,4)
    save_image('images',image_name,image5,5)
    save_image('images',image_name,image6,6)
    save_image('images',image_name,image7,7)
    save_image('images',image_name,image8,8)

    print('Split Successful!')
