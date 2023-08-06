# -*- coding=utf-8 -*- 
# github: night_handsomer
# csdn: 惜年_night
# mirror: https://pypi.tuna.tsinghua.edu.cn/simple/

###########################
# Dear:                   #
#                         #
#    欢迎批评指正(捂脸)      #
#                   Night #
###########################

import cv2

# 任意角度的旋转
def any_angle(path, angle, scale=1.0, flags=cv2.IMREAD_COLOR, size=(300, 300), flip=None):
    """
    :param path:        图片路径
    :param angle:       你想旋转的角度
    :param scale:       旋转后图片的尺寸，默认是 1.0
    :param flags:       打开方式，灰度/RGB/RGB-A, 默认是 RGB
    :param size:        改变图像尺寸(分辨率)
    :param flip:        是否镜像
    :return:
    """
    img = cv2.imread(path, flags)

    if flip is None:
        img = cv2.resize(img, size)     # 重置尺寸，需要扩展自己改吧

        (h, w) = img.shape[0:2]
        center = (h//2, w//2)

        M = cv2.getRotationMatrix2D(center, angle, scale)
        rot = cv2.warpAffine(img, M, (w, h))        # 注意这里, 恢复的时候 w, h是反过来的
    else:
        rot = cv2.flip(img, flags)

    return rot




