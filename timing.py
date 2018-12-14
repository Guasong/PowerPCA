# This scripts automate timing tests for us

import os
import numpy as np
from datetime import datetime
from svd import svd
from PowerMethod import PowerMethod
import ImgOps as img_pm
import ImgOps_naive as img_naive

os.chdir(os.path.dirname(__file__))

##### A Simple Test

A = [[ 0.041,0.815,0.245,0.054,0.249,0.534,0.753,0.307,0.877,0.429],
 [ 0.918,0.846,0.249,0.262,0.133,0.32, 0.446,0.122,0.164,0.711],
 [ 0.139,0.701,0.726,0.094,0.036,0.695,0.325,0.29, 0.373,0.692],
 [ 0.644,0.067,0.032,0.896,0.047,0.55, 0.062,0.568,0.204,0.275],
 [ 0.631,0.412,0.232,0.415,0.335,0.508,0.393,0.549,0.076,0.698]]

# power method
time_pm = []
for i in range(10):
    T = PowerMethod(A, 5)
    startTime = datetime.now()
    T.power_method()
    time = datetime.now() - startTime
    time_pm.append(time)
# naive svd
time_naive = []
for i in range(10):
    startTime = datetime.now()
    svd(A)
    time = datetime.now() - startTime
    time_naive.append(time)


##### Test on PCA of Images

# power method
pca_time_pm = []
for i in range(10):
    startTime = datetime.now()
    ic1 = img_pm.ImageCompresser(1, 'src_img/mackey.png', 'out_img/mackey-1.png')
    ic1.compress()
    time = datetime.now() - startTime
    pca_time_pm.append(time)

# naive svd
pca_time_naive = []
for i in range(10):
    startTime = datetime.now()
    ic1 = img_naive.ImageCompresser(1, 'src_img/mackey.png', 'out_img/mackey-1.png')
    ic1.compress()
    time = datetime.now() - startTime
    pca_time_naive.append(time)


print('#####RESULTS#####')
print('SIMPLE TEST')
print('power method:', np.mean(time_pm))
print('naive svd:', np.mean(time_naive))
print('PCA ON IMAGES')
print('power method:', np.mean(pca_time_pm))
print('naive:', np.mean(pca_time_naive))
