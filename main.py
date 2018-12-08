import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from PIL import Image
from ImgOps import *

os.chdir(os.path.dirname(__file__))

ic1 = ImageCompresser(1, 'src_img/mackey.png', 'out_img/mackey-1.png')
ic1.compress()
# ic1.saveImage()

ic2 = ImageCompresser(5, 'src_img/mackey.png', 'out_img/mackey-5.png')
ic2.compress()
# ic2.saveImage()

ic3 = ImageCompresser(10, 'src_img/mackey.png', 'out_img/mackey-10.png')
ic3.compress()
# ic3.saveImage()

ic4 = ImageCompresser(15, 'src_img/mackey.png', 'out_img/mackey-15.png')
ic4.compress()
# ic4.saveImage()

ic5 = ImageCompresser(30, 'src_img/mackey.png', 'out_img/mackey-30.png')
ic5.compress()
# ic5.saveImage()

plt.rcParams.update({'font.size': 7})
plt.rcParams.update({'font.family': 'Arial'})

print('Plotting...')

f, axarr = plt.subplots(2,3)
axarr[0,0].imshow(ic1.getOutputArr())
axarr[0,0].set_title('k=1')
axarr[0,0].axis('off')

axarr[0,1].imshow(ic2.getOutputArr())
axarr[0,1].set_title('k=5')
axarr[0,1].axis('off')

axarr[0,2].imshow(ic3.getOutputArr())
axarr[0,2].set_title('k=10')
axarr[0,2].axis('off')

axarr[1,0].imshow(ic4.getOutputArr())
axarr[1,0].set_title('k=15')
axarr[1,0].axis('off')

axarr[1,1].imshow(ic5.getOutputArr())
axarr[1,1].set_title('k=30')
axarr[1,1].axis('off')

axarr[1,2].imshow(ic5.getOriginalArr())
axarr[1,2].set_title('uncompressed')
axarr[1,2].axis('off')

plt.savefig("out_img/mackey-2x2.png", dpi=500)
# plt.show()