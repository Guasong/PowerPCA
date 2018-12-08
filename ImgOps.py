from PIL import Image
import numpy as np
import PowerMethod

class ImageCompresser(object):
    def __init__(self, k, img, out='output.png'):
        self.img_name = img
        self.img = Image.open(img)
        self.img_ori_arr = np.array(self.img)
        self.k = k
        self.output = np.zeros(self.img_ori_arr.shape)
        self.outpath = out
        self.compressed = False

    def getOriginalArr(self):
        return self.img_ori_arr

    def getOutputArr(self):
        if not self.compressed:
            print("Run compress() first!")
            return
        self.o = Image.fromarray(self.output.astype('uint8'))
        if self.o.mode != 'RGB':
            self.o = self.o.convert('RGB')
        return np.array(self.o)

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
        print('Compressing', self.img_name, 'with k =', self.k, '...')
        for i in range(self.img_ori_arr.shape[2]-1):
            RGB = ['R','G','B']
            channel = self.img_ori_arr[...,i]
            p = PowerMethod.PowerMethod(channel, self.k)
            print(RGB[i], 'channel shape: ', channel.shape)
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
            self.compressed = True
        print('Image compressed!\n')

    def saveImage(self):
        if not self.compressed:
            print("Run compress() first!")
            return
        self.o = Image.fromarray(self.output.astype('uint8'))
        if self.o.mode != 'RGB':
            self.o = self.o.convert('RGB')
        self.o.save(self.outpath,'png')

# np.set_printoptions(precision=30)