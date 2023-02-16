import numpy as np
import cv2 as cv
import random


class Img_pro_utils(object):

    @staticmethod
    def to_gray_normal(self, img: np.ndarray):
        if len(img.shape) == 3:
            img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # 如果已经映射到0，1则不需要再映射了
        # 灰度值映射到[0, 1]
        if np.max(img) > 1:
            img = img / 255
        return img

    @staticmethod
    # 多段线性变换
    def imLinearAdjust_n(self, src: np.ndarray, points: list, ks: list):
        """多段线性变化

        Args:
            src (np.ndarray): 输入图片
            points (list): 区间点集不包括0，1
            ks (list): 斜率集

        Returns:
            dst: 输出图片
        """
        src = self.to_gray_normal(self, src)
        if (len(points) != len(ks) - 1):
            print("points和ks的长度不对应")
            return
        elif len(points) <= 0 or len(ks) <= 1:
            print("points和ks的长度错误")
            return

        src[(0 <= src) & (src < points[0])] = ks[0] * \
            src[(0 <= src) & (src < points[0])]
        dy = ks[0] * points[0]
        for i in range(1, len(ks)):
            src[(points[i - 1] <= src) & (src < points[i])] = ks[i] * \
                src[(points[i - 1] <= src) & (src < points[i])] + dy
            dy = dy + ks[i] * (points[i] - points[i - 1])
        src[(points[len(ks) - 2] <= src) & (src <= 1)] = ks[len(ks) - 1] * \
            src[(points[len(ks) - 2] <= src) & (src <= 1)] + dy
        dst = src
        return dst

    @staticmethod
    def imLinearAdjust(self, src: np.ndarray, k, b):
        """线性变化"""
        src = self.to_gray_normal(self, src)
        temp = src * k + b
        temp[temp > 1] = 1
        return self.to_gray_255(self, temp)

    @staticmethod
    def to_gray_255(self, src):
        """将灰度值映射到[0, 255]

        Args:
            src (np.ndarray): 输入图片

        Returns:
            np.ndarray: 输出图片
        """
        src = src * 255
        print(type(src[0][0]))
        # 将浮点数转换为整数
        src = src.astype(np.uint8)
        print(type(src[0][0]))
        return src

    @staticmethod
    def imLogAdjust(self, src, lamb, base):
        """对数变化

        Args:
            src (np.ndarray): 输入图片
            lamb (float): lambda倍数
            base (float): 对数底
        Returns:
            np.ndarray: 输出图片
        """
        src = self.to_gray_normal(self, src)
        temp = lamb * np.log(src + 1) / np.log(base)
        return self.to_gray_255(self, temp)

    @staticmethod
    def imPowerAdjust(self, src: np.ndarray, lamb: float, power: float):
        """指数变换

        Args:
            src (np.ndarray): 源图像
            lamb (float): lambda倍数
            power (float): 指数

        Returns:
            np.ndarray: 输出图像
        """
        src = self.to_gray_normal(self, src)
        temp = lamb * np.power(src, power)
        return self.to_gray_255(self, temp)

    @staticmethod
    def imHistEqual(self, src: np.ndarray):
        """直方图均衡化

        Args:
            src (np.ndarray): 源图像

        Returns:
            np.ndarray: 输出图像
        """
        # src = self.to_gray_normal(self, src) # 直方图均衡化不需要归一化
        # print(type(src[0][0]))
        # 由于只支持uint8类型，因此需要在此判断图片类型是灰度还是彩图
        if (src.ndim == 3):
            src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        # 如果图片已经归一化，需要先映射到255
        if (np.dtype != np.uint8):
            src = self.to_gray_255(self, src)
        temp = cv.equalizeHist(src)
        return self.to_gray_255(self, temp)

    @staticmethod
    def imLUT(self, src: np.ndarray, lut: np.ndarray):
        """灰度变换

        Args:
            src (np.ndarray): 源图像
            lut (np.ndarray): 灰度变换表

        Returns:
            np.ndarray: 输出图像
        """
        # 由于只支持uint8类型，因此需要在此判断图片类型是灰度还是彩图
        if (src.ndim == 3):
            src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        # 如果图片已经归一化，需要先映射到255
        if (np.dtype != np.uint8):
            src = self.to_gray_255(self, src)
        src = self.to_gray_normal(self, src)
        temp = cv.LUT(src, lut)
        return self.to_gray_255(self, temp)

    @staticmethod
    def imfilter(self, src: np.ndarray, kernel: np.ndarray):
        temp = cv.filter2D(src, -1, kernel)
        return temp

    @staticmethod
    def imSmoothing(self, src: np.ndarray):
        """平滑滤波

        Args:
            src (np.ndarray): 源图像
            kernel (np.ndarray): 滤波核

        Returns:
            np.ndarray: 输出图像
        """
        # temp = cv.blur(src, kernel)
        # 中值滤波核
        kernel = np.ones((5, 5), np.float32) / 25
        temp = Img_pro_utils.imfilter(self, src, kernel)
        return temp

    @staticmethod
    def imSharpen(self, src: np.ndarray):
        """锐化滤波

        Args:
            src (np.ndarray): 源图像
            kernel (np.ndarray): 滤波核

        Returns:
            np.ndarray: 输出图像
        """
        # 基于拉普拉斯算子的图像锐化
        kernel = np.array(([0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]), dtype="float32")
        temp = Img_pro_utils.imfilter(self, src, kernel)
        print(np.shape(temp))
        return temp

    @staticmethod
    def imFimg(self, src: np.ndarray):
        src = self.to_gray_normal(self, src)
        f = np.fft.fft2(src)
        fshift = np.fft.fftshift(f)
        fshift_img = np.log(np.abs(fshift))
        # 将fshift_img映射到0-1
        fshift_img = (fshift_img - np.min(fshift_img)) / \
            (np.max(fshift_img) - np.min(fshift_img))
        fshift_img = self.to_gray_255(self, fshift_img)
        print(np.shape(fshift_img))
        return fshift_img

    @staticmethod
    def filter(self, img, D0, N=2, type='lp', filter='butterworth'):
        '''
        频域滤波器
        Args:
            img: 灰度图片
            D0: 截止频率
            N: butterworth的阶数(默认使用二阶)
            type: lp-低通 hp-高通
            filter:butterworth、ideal、Gaussian即巴特沃斯、理想、高斯滤波器
        Returns:
            imgback：滤波后的图像
        '''
        img = self.to_gray_normal(self, img)
        img = self.to_gray_255(self, img)
        # 离散傅里叶变换
        dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
        # 中心化
        dtf_shift = np.fft.fftshift(dft)

        rows, cols = img.shape
        crow, ccol = int(rows / 2), int(cols / 2)  # 计算频谱中心
        mask = np.zeros((rows, cols, 2))  # 生成rows行cols列的二维矩阵

        for i in range(rows):
            for j in range(cols):
                D = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)  # 计算D(u,v)
                if (filter.lower() == 'butterworth'):  # 巴特沃斯滤波器
                    if (type == 'lp'):
                        mask[i, j] = 1 / (1 + (D / D0) ** (2 * N))
                    elif (type == 'hp'):
                        mask[i, j] = 1 / (1 + (D0 / D) ** (2 * N))
                    else:
                        assert ('type error')
                elif (filter.lower() == 'ideal'):  # 理想滤波器
                    if (type == 'lp'):
                        if (D <= D0):
                            mask[i, j] = 1
                    elif (type == 'hp'):
                        if (D > D0):
                            mask[i, j] = 1
                    else:
                        assert ('type error')
                elif (filter.lower() == 'gaussian'):  # 高斯滤波器
                    if (type == 'lp'):
                        mask[i, j] = np.exp(-(D * D) / (2 * D0 * D0))
                    elif (type == 'hp'):
                        mask[i, j] = (1 - np.exp(-(D * D) / (2 * D0 * D0)))
                    else:
                        assert ('type error')

        fshift = dtf_shift * mask

        f_ishift = np.fft.ifftshift(fshift)
        img_back = cv.idft(f_ishift)
        img_back = cv.magnitude(
            img_back[:, :, 0], img_back[:, :, 1])  # 计算像素梯度的绝对值
        img_back = np.abs(img_back)
        img_back = (img_back - np.amin(img_back)) / (np.amax(img_back) - np.amin(img_back))
        img_back = self.to_gray_255(self, img_back)
        return img_back

    @staticmethod
    def sp_noise(self, noise_img, n):
        '''
        添加椒盐噪声
        n的值表示加入噪声的量
        return: img_noise
        '''
        height, width = noise_img.shape[0], noise_img.shape[1]#获取高度宽度像素值
        num = int(height * width * n) #一个准备加入多少噪声小点
        for i in range(num):
            w = random.randint(0, width - 1)
            h = random.randint(0, height - 1)
            if random.randint(0, 1) == 0:
                noise_img[h, w] = 0
            else:
                noise_img[h, w] = 255
        return noise_img
    
    @staticmethod
    def gaussian_noise(self, img, mean, sigma):
        '''
        此函数用将产生的高斯噪声加到图片上
        传入:
            img   :  原图
            mean  :  均值
            sigma :  标准差
        返回:
            gaussian_out : 噪声处理后的图片
        '''
        img = self.to_gray_normal(self, img)
        # 产生高斯 noise
        noise = np.random.normal(mean, sigma, img.shape)
        # 将噪声和图片叠加
        gaussian_out = img + noise
        # 将超过 1 的置 1，低于 0 的置 0
        gaussian_out = np.clip(gaussian_out, 0, 1)
        gaussian_out = self.to_gray_255(self, gaussian_out)
        return gaussian_out# 这里也会返回噪声，注意返回值

    @staticmethod
    def random_noise(self, image,noise_num):
        '''
        添加随机噪点（实际上就是随机在图像上将像素点的灰度值变为255即白色）
        param image: 需要加噪的图片
        param noise_num: 添加的噪音点数目
        return: img_noise
        '''
        # 参数image：，noise_num：
        img_noise = image
        # cv2.imshow("src", img)
        rows, cols, chn = img_noise.shape
        # 加噪声
        for i in range(noise_num):
            x = np.random.randint(0, rows)#随机生成指定范围的整数
            y = np.random.randint(0, cols)
            img_noise[x, y, :] = 255
        return img_noise

    @staticmethod
    def imEdge(self, src, type):
        '''
        采用roberts算子，prewitt算子，sobel算子，LOG算子对图像进行边缘提取。
        '''
        kernel = None
        if type == "roberts":
            kernel = np.array([[-1, 0], [0, 1]])
        elif type == "prewitt":
            kernel = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
        elif type == "sobel":
            kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        elif type == "log":
            kernel = np.array([[0,1,0], [1, -4, 1], [0, 1, 0]])
        temp = cv.filter2D(src, -1, kernel)
        return temp
    
    @staticmethod
    def morphology(self, src, type, ksize):
        '''
        二值图像的形态学处理，至少包括膨胀、腐蚀、开、闭操作。
        '''
        # src = self.to_gray_normal(self, src)
        # src = self.to_gray_255(self, src)
        temp = None
        if type == 'dilate':
            temp = cv.dilate(src, np.ones((ksize, ksize), np.uint8))
        elif type == 'erode':
            temp = cv.erode(src, np.ones((ksize, ksize), np.uint8))
        elif type == 'open':
            temp = cv.morphologyEx(src, cv.MORPH_OPEN, np.ones((ksize, ksize), np.uint8))
        elif type == 'close':
            temp = cv.morphologyEx(src, cv.MORPH_CLOSE, np.ones((ksize, ksize), np.uint8))
        return temp

    @staticmethod
    def segment(self, src):
        '''
        读入一幅为图像（只含有单一目标），应用所学的知识分割出前景目标和背景图像（分割前景和背景）。
        '''
        src = self.to_gray_normal(self, src)
        src = self.to_gray_255(self, src)
        # 使用otsu算法进行二值化
        ret, binary = cv.threshold(src, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        return binary

    @staticmethod
    def matting(self, src: np.ndarray, mask: np.ndarray):
        """抠图，根据二值化的mask抠图

        Args:
            src (np.ndarray): 输入的图像，要求为三通道，并且在函数结束后会被修改
            mask (np.ndarray): 掩模，要求为单通道，且为二值化图像

        Returns:
            src: 抠图后的图像 
        """
        bgr_ls: list() = list(cv.split(src))
        for i in range(3):
          bgr_ls[i] = cv.bitwise_and(bgr_ls[i], mask)
        cv.merge(bgr_ls, src)
        return src


            




if __name__ == "__main__":
    # 测试代码
    img = cv.imread("./data/lapsrn_butterfly.jpg")
    print(type(img[0][0]))

    # img = Img_pro_utils.to_gray_normal(Img_pro_utils, img)
    # # 输出img元素中的最大值和最小值
    # print(np.max(img), np.min(img))
    # cv.imshow("test", img)
    # if cv.waitKey(0) == ord("q"):
    #     cv.destroyAllWindows()

    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

    # 将 a 数组中所有在 0 到 3 之间的元素平方
    a[(0 <= a) & (a <= 3)] = a[(0 <= a) & (a <= 3)]**2
    print(a)

    # # temp = Img_pro_utils.imLinearAdjust_n(Img_pro_utils, img, [0.2, 0.5, 0.8], [0.5, 1, 0.5, 0.2])
    # temp = Img_pro_utils.imLinearAdjust(Img_pro_utils, img, 0.5, 0.2)
    # cv.imshow("temp", temp)
    # if cv.waitKey(0) == ord("q"):
    #     cv.destroyAllWindows()

    # temp = Img_pro_utils.imLogAdjust(Img_pro_utils, img, 0.5, 2)
    # cv.imshow("temp", temp)
    # if cv.waitKey(0) == ord("q"):
    #     cv.destroyAllWindows()

    src = Img_pro_utils.imPowerAdjust(Img_pro_utils, img, 0.5, 2)
    cv.imshow("temp", src)
    print(np.shape(src))
    if cv.waitKey(0) == ord("q"):
        cv.destroyAllWindows()
        # 判断是否为数字

    # print("------------------imHistEqual------------------")
    # temp = Img_pro_utils.imHistEqual(Img_pro_utils, img)
    # cv.imshow("temp", temp)
    # if cv.waitKey(0) == ord("q"):
    #     cv.destroyAllWindows()

    # # print("------------------imLUT------------------")
    # # # 指定一个映射lut
    # # # 这是一个平均分布
    # # temp = Img_pro_utils.imLUT(Img_pro_utils, img, lut)
    # # cv.imshow("temp", temp)
    # # if cv.waitKey(0) == ord("q"):
    # #     cv.destroyAllWindows()

    # print("------------------imSmoothing------------------")
    # temp = Img_pro_utils.imSmoothing(Img_pro_utils, img)
    # cv.imshow("temp", temp)
    # if cv.waitKey(0) == ord("q"):
    #     cv.destroyAllWindows()

    # print("------------------imSharpen------------------")
    # temp = Img_pro_utils.imSharpen(Img_pro_utils, img)
    # cv.imshow("temp", temp)
    # if cv.waitKey(0) == ord("q"):
    #     cv.destroyAllWindows()

    # print("------------------imFimg------------------")
    # temp = Img_pro_utils.imFimg(Img_pro_utils, img)
    # print(type(temp[0][0]))
    # cv.imshow("temp", temp)
    # if cv.waitKey(0) == ord("q"):
    #     cv.destroyAllWindows()

    # print("------------------filter------------------")
    # temp = Img_pro_utils.filter(Img_pro_utils, img, 20)
    # cv.imshow("temp", temp)
    # print(temp)
    # if cv.waitKey(0) == ord("q"):
    #     cv.destroyAllWindows()

    # print("------------------sp_noise------------------")
    # temp = Img_pro_utils.sp_noise(Img_pro_utils, img, 0.1)
    # cv.imshow("temp", temp)
    # if cv.waitKey(0) == ord("q"):
    #     cv.destroyAllWindows()
    
    # print("------------------gaussian_noise------------------")
    # temp = Img_pro_utils.gaussian_noise(Img_pro_utils, img, 0, 0.1)
    # cv.imshow("temp", temp)
    # if cv.waitKey(0) == ord("q"):
    #     cv.destroyAllWindows()

    # print("------------------random_noise------------------")
    # temp = Img_pro_utils.random_noise(Img_pro_utils, img, 1)
    # cv.imshow("temp", temp)
    # if cv.waitKey(0) == ord("q"):
    #     cv.destroyAllWindows()
    
    
    # print("------------------imEdge------------------")
    # temp = Img_pro_utils.imEdge(Img_pro_utils, img, "sobel")
    # cv.imshow("temp", temp)
    # if cv.waitKey(0) == ord("q"):
    #     cv.destroyAllWindows()

    print("------------------morphology------------------")
    # 产生二值化图像
    mask = Img_pro_utils.segment(Img_pro_utils, img)
    # temp = Img_pro_utils.morphology(Img_pro_utils, temp, "dilate", ksize=3)
    Img_pro_utils.matting(Img_pro_utils, img, mask)
    cv.imshow("temp", img)
    if cv.waitKey(0) == ord("q"):
        cv.destroyAllWindows()
    
    

    
    
