import matplotlib.pyplot as plt
from PIL import Image

img=Image.open("D:\\Neural networks-code\\lena.tiff") #打开彩色图像
img_r,img_g,img_b=img.split() #将彩色图像分离为RGB三个颜色通道
plt.figure(figsize=(10,10))

#R通道
plt.subplot(221)
plt.axis("off")
img_small=img_r.resize((50,50)) #图像缩小为50*50
plt.imshow(img_small,cmap="gray")
plt.title("R-缩放",fontsize=14)

#G通道
plt.subplot(222)
img_flr=img_g.transpose(Image.FLIP_LEFT_RIGHT) #图像水平镜像
img_r270=img_flr.transpose(Image.ROTATE_270) #图像顺时针旋转90度
plt.imshow(img_r270,cmap="gray") 
plt.title("G-镜像+旋转",fontsize=14)

#B通道
plt.subplot(223)
plt.axis("off")
img_region=img_b.crop((0,0,150,150))
plt.imshow(img_region,cmap="gray")
plt.title("B-裁剪",fontsize=14)

#通道合并
plt.subplot(224)
plt.axis("off")
img_rgb=Image.merge("RGB",[img_r,img_g,img_b])
plt.imshow(img_rgb)
plt.title("RGB",fontsize=14)

img_rgb.save("test.png")  #保存图片为png格式

plt.suptitle("图像基本操作",fontsize=20,color="blue")

plt.show()

