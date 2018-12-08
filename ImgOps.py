from PIL import Image
import numpy as np
import PowerMethod
import os

class ImageCompresser(object):
    def __init__(self, img, k):
        self.img = Image.open(img)
        self.img_arr = np.array(self.img)
        self.k = k
        self.output = np.zeros((229,220,4))

    def getNumpyArr(self):
        return self.img_arr

    def format(self, p):
        s = []
        u = []
        vh = []
        for i in range(len(p)):
            s.append(p[i][0])
            u.append(p[i][1])
            vh.append(p[i][2])
        s = np.array([[i] for i in s])
        u = np.array(u).T
        vh = np.array(vh)
        return s, u, vh

    def compress(self):
        for i in range(self.img_arr.shape[2]):
            channel = self.img_arr[...,i]
            p = PowerMethod.PowerMethod(channel, self.k)
            print("channel size: ",channel.shape)
            result = p.power_method()
            u, s, vh = np.linalg.svd(channel)
            # s, u, vh = self.format(result)
            print(u.shape)
            print(s.shape)
            print(vh.shape)

            s[-216:-1]=np.zeros(215)
 
            s = np.diag(s)
            s_new = np.zeros((9,220))
            s = np.vstack((s, s_new))
            self.output[...,i] = np.matmul(np.matmul(u, s),vh)

    def saveImage(self):
        self.o = Image.fromarray(self.output.astype('uint8'))
        if self.o.mode != 'RGB':
            self.o = self.o.convert('RGB')
        self.o.save('output.png','png')


os.chdir(os.path.dirname(__file__))
ic = ImageCompresser("jacobo.png", 2)
ic.compress()
ic.saveImage()