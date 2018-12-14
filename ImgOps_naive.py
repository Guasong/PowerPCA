# This script is a PCA implementation using the naive SVD

import numpy as np
from svd import svd
from PIL import Image

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

    def compress(self):
        print('Compressing', self.img_name, 'with k =', self.k, '...')
        for i in range(self.img_ori_arr.shape[2]-1):
            RGB = ['R','G','B']
            channel = self.img_ori_arr[...,i]
            print(RGB[i], 'channel shape: ', channel.shape)
            u, s, vh = svd(channel)
            s[self.k:-1]=np.zeros(s.shape[0]-self.k-1)
            s = np.diag(s)
            print(u.shape)
            print(s.shape)
            print(vh.shape)
            # uncomment and modify the below lines if not input not square to fit svd outputs
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