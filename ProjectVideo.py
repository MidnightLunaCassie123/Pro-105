import os
import cv2

path="PRO-C105-Project-Images-main"

images=[]


for file in os.listdir(path):
    name, ext = os.path.splitext(file) 

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append()

        count = len(images) 

        frame=cv2.imread(images[0])

        width,height,Channels=frame.shape

        size=(width,height)

        out=cv2.VideoWriter("ProVid.avi", cv2.VideoWriter_fourcc(*"DIVX"), 0.8, size)

        for i in range (0,count-1):
            frame=cv2.imread(images[i])
            out.write(frame)

        print("Done")
