import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file) # Splits the path and the extenstion. Ex: if you have maya.png, it will split maya and .png in two

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)#append is used to add the data to the list
        
print(len(images))
count = len(images)

frame=cv2.imread(images[0])# Imread reads all the images in the file
height,width,channels=frame.shape
size=(width,height)

out=cv2.VideoWriter("project.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 5, size)# VideoWriter_fourcc is a video creator

for i in range ( count-1,0,-1):
    frame=cv2.imread(images[i])
    out.write(frame)

out.release()
print("Done!")
