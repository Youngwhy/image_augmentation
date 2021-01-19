import cv2 as cv
import numpy as np
import math
import random
import os
from glob import glob

def imagebatch(folderpath):
    img_list = glob(folderpath+'/*.jpg')
    dataset_size = len(img_list)
    batch_image = []
    for n, path in enumerate(img_list[:dataset_size]):
        image = cv.imread(path)
        batch_image.append(image)
    return batch_image


def AffineTransform(imagearray, deg=0, scale=1, x_trans=0, y_trans=0, x_shear=0, y_shear=0):
    # -----h,w 값 할당 및 center 설정-----
    (h, w) = img.shape[:2]
    # -----Translation & shear transformation-----

    T_trans = np.float32([
        [1, 0, x_trans],
        [0, 1, y_trans],
        [0, 0, 1]])
    T_shear = np.float32([
        [1, x_shear, 0],
        [y_shear, 1, 0],
        [0, 0, 1]])

    T = T_trans @ T_shear
    T = np.delete(T, 2, axis=0)
    #     tns = cv.warpAffine(img, T, (w, h))
    tns = cv.warpAffine(img, T, (img.shape[1], img.shape[0]))

    #     cv.imshow("mid", tns)
    #     cv.waitKey(0)
    #     cv.destroyAllWindows()

    #     -----rotation & scale transformation-----
    #     (h, w) = tns.shape[:2]
    (cX, cY) = (tns.shape[1] / 2, tns.shape[0] / 2)

    T_rot = cv.getRotationMatrix2D((cX, cY), deg, scale)  # (center, angle, scale)
    rotated = cv.warpAffine(tns, T_rot, (tns.shape[1], tns.shape[0]))
    print(rotated.shape)
    return rotated


def RandomAffine(imagearray):
    # -----h,w 값 할당 및 center 설정-----
    (h, w) = imagearray.shape[:2]

    x_trans = random.randint(0, 0.3 * w)
    y_trans = random.randint(0, 0.3 * h)
    x_shear = random.uniform(0, 0.3)
    y_shear = random.uniform(0, 0.3)
    deg = random.randint(-30, 30)
    scale = random.uniform(0.5, 1.5)

    # -----Translation & shear transformation-----
    T_trans = np.float32([
        [1, 0, x_trans],
        [0, 1, y_trans],
        [0, 0, 1]])
    T_shear = np.float32([
        [1, x_shear, 0],
        [y_shear, 1, 0],
        [0, 0, 1]])

    T = T_trans @ T_shear
    T = np.delete(T, 2, axis=0)
    #     tns = cv.warpAffine(img, T, (w, h))
    tns = cv.warpAffine(imagearray, T, (imagearray.shape[1], imagearray.shape[0]))

    #     -----rotation & scale transformation-----

    (cX, cY) = (tns.shape[1] / 2, tns.shape[0] / 2)

    T_rot = cv.getRotationMatrix2D((cX, cY), deg, scale)  # (center, angle, scale)
    rotated = cv.warpAffine(tns, T_rot, (tns.shape[1], tns.shape[0]))
    return rotated

def RandomBrCtBl(imagearray):
    alpha = random.uniform(0.1,3)
    beta  = random.randint(1,100)
    kernel_size = random.randrange(1,31,2)
    img_BrCt = cv.convertScaleAbs(imagearray, -1 ,alpha, beta)
    Bl = cv.GaussianBlur(img_BrCt,(kernel_size,kernel_size),0)
    return Bl

def Randomautoaug(targetfolderpath,augmentedfolder):
    batch_image = imagebatch(folderpath)
    batch_image = np.array(batch_image)
    if not os.path.exists(augmentedfolder):
        os.makedirs(augmentedfolder)


    for i in range(0,batch_image.shape[0]):
        img = batch_image[i]
        bc = RandomBrCtBl(img)
        ra = RandomAffine(bc)
        cv.imwrite(augmentedfolder+str(i)+'_aug.jpg',ra)