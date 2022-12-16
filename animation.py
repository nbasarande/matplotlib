import glob
from PIL import Image

frames=[]
path= '*.png'
imgs=glob.glob(path)
print(imgs)
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)
frames[0].save('animation.gif',
               save_all=True, append_images=frames[1:], optimize=False, duration=1000, loop=0)