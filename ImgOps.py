from PIL import Image
import numpy as np
import PowerMethod
import os

class ImageCompresser(object):
    def __init__(self, k, img, out='output.png'):
        self.img = Image.open(img)
        self.img_arr = np.array(self.img)
        self.k = k
        self.output = np.zeros(self.img_arr.shape)
        self.outpath = out

    def getNumpyArr(self):
        return self.img_arr

    def format(self, p):
        s = []
        u = []
        vh = []
        for i in range(len(p)):
            s.append(p[i][0])
            vh.append(p[i][1])
            u.append(p[i][2])
        s = np.array(s)
        u = np.array(u).T
        vh = np.array(vh)
        return s, u, vh

    def compress(self):
        for i in range(self.img_arr.shape[2]-1):
            channel = self.img_arr[...,i]
            p = PowerMethod.PowerMethod(channel, self.k)
            print("channel size: ",channel.shape)
            result = p.power_method()
            # u, s, vh = np.linalg.svd(channel)
            s, u, vh = self.format(result)

            # s[-216:-1]=np.zeros(215)
            s = np.diag(s)
            s = np.pad(s, ((0,u.shape[0]-s.shape[0]), (0,vh.shape[1]-s.shape[0])), 'constant')
            u = np.pad(u, ((0,0),(0,u.shape[0]-u.shape[1])), 'constant')
            vh = np.pad(vh, ((0,vh.shape[1]-vh.shape[0]),(0,0)), 'constant')
            print(u.shape)
            print(s.shape)
            print(vh.shape)
            # s_new = np.zeros((9,220))
            # s = np.vstack((s, s_new))
            self.output[...,i] = np.clip(np.matmul(np.matmul(u, s),vh), 0, 255)

    def saveImage(self):
        self.o = Image.fromarray(self.output.astype('uint8'))
        if self.o.mode != 'RGB':
            self.o = self.o.convert('RGB')
        self.o.save(self.outpath,'png')

# np.set_printoptions(precision=30)
os.chdir(os.path.dirname(__file__))

ic1 = ImageCompresser(1, 'mackey.png', 'mackey-1.png')
ic1.compress()
ic1.saveImage()

ic2 = ImageCompresser(5, 'mackey.png', 'mackey-5.png')
ic2.compress()
ic2.saveImage()

ic3 = ImageCompresser(10, 'mackey.png', 'mackey-10.png')
ic3.compress()
ic3.saveImage()

ic4 = ImageCompresser(15, 'mackey.png', 'mackey-15.png')
ic4.compress()
ic4.saveImage()