# Description  
An implementation of PCA using Power Method in computing SVD  

# Paper   
The paper detailing the approaches and analysis used in this project can be found at: https://github.com/johnzhang1999/PowerPCA/blob/master/docs/21_241_Final_Paper__Power_Method_for_SVD%20FINAL%20-%20Yiwen%20Zhang%2C%20John%20Zhang.pdf   

# Code Structure  
.  
├── ImgOps.py //implementation of PCA using `power_method()` in `PowerMethod.py`  
├── ImgOps_naive.py //implementation of PCA using the naive `svd()` in `svd.py`  
├── PowerMethod.py //our implementation of the required `power_method()` can be found in this OOP encapsulation.  
├── README.md //this file  
├── main.py //generating PCA compressed images using `ImgOps.py`  
├── out_img //PCA image output directory  
│   ├── mackey-1.png  
│   ├── mackey-10.png  
│   ├── mackey-15.png  
│   ├── mackey-2x3.png  
│   └── mackey-5.png  
├── src_img //PCA image input directory  
│   ├── jacobo.png  
│   ├── mackey.png  
│   └── scs.png  
├── svd.py //implementation of naive SVD  
└── timing.py //generating timing statistics  

# Author   
John Zhang, Yiwen Zhang  
21-241 Matrices and Linear Transformations  
Carnegie Mellon University 

