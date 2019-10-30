# 读取图像，解决 imread 不能读取中文路径的问题
# https://www.zhihu.com/question/67157462/answer/251754530
def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    return cv_img