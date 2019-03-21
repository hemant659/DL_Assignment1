from cv2 import VideoWriter, VideoWriter_fourcc
import glob
import os
import random
import numpy as np
import scipy.misc
from PIL import Image, ImageDraw
import sys
#path = '/home/user/Downloads/sem_6/CS_671_DL/Assignment_1/images/'
print(len(sys.argv))
count_arg=0;
for x in sys.argv:
	print(x,count_arg)
	count_arg +=1
if len(sys.argv) != 2 :
    print("Usage: python question_1_cla.py path/")
    sys.exit (1)
path = str(sys.argv[1])

def draw_line(line_length , line_width , angle_index , color_no , save_file_path):#1 1 9 0
    
    color =[0,0,0]
    line_thickness = 0
    distance = 0
    
    if(color_no==0):
        color[0]=255
    else:
        color[2]=255
        
    if(line_width==0):
        line_thickness = 1
    else:
        line_thickness = 3
    
    if(line_length==0):
        distance = 7
    else:
         distance = 15   
    
    angle = angle_index * 15
    line_id = 0;
    
    start_point = [0,0]
    end_point = [0,0]
    
    i=0
    while(i<10000):
        
        start_point[0]=random.randint(0,28);
        start_point[1]=random.randint(0,28);
        
        end_point[0]=start_point[0]+((distance*pow(2,0.5))/pow(1+pow(np.tan(np.deg2rad(angle)),2),0.5))
        end_point[1]=start_point[1]+(((distance*pow(2,0.5))*np.tan(np.deg2rad(angle)))/pow(1+pow(np.tan(np.deg2rad(angle)),2),0.5))
        
        
        if(((end_point[0]<28)and(end_point[1]<28))and((end_point[0]>=0)and(end_point[1]>=0))):
            im = Image.new('RGB', (28, 28), (0, 0, 0))#drawing the black background
            draw = ImageDraw.Draw(im)
            draw.line((start_point[0],start_point[1],end_point[0],end_point[1]),fill=(color[0],color[1],color[2]),width=line_thickness)
            
            save_file = save_file_path + str(line_length)+'_'+str(line_width)+'_'+str(angle_index)+'_'+str(color_no)+'_'+str(line_id)+'.jpg'
            im.save(save_file)
            line_id += 1
            if(line_id>=1000):
                break

        i+=1

class_number=0
for length in range(2):                                     
    for width in range(2):
        for angle_number in range(12):
            for color_number in range(2):
                class_number += 1
                directory_name = path+'class_'+str(class_number)+'/'
                os.makedirs(directory_name)
                draw_line(length,width,angle_number,color_number,directory_name)
                
#Vedio attributes
width = 28*3
height = 28*3
FPS = 2
seconds = 480

fourcc = VideoWriter_fourcc(*'MP42')
video = VideoWriter(path+'video_from_frames.avi', fourcc, float(FPS), (width, height))


for class_number_dirctory in range(1,class_number + 1):
    directory_name = path+'class_'+str(class_number_dirctory)+'/'
    arr = random.sample(range(1000),90) 
    os.makedirs(directory_name+'frames/')
    for frame_number in range(10):
        image_1 = Image.open((glob.glob(directory_name+'*_'+str(arr[frame_number*9 + 0])+'.jpg'))[0])
        image_2 = Image.open((glob.glob(directory_name+'*_'+str(arr[frame_number*9 + 1])+'.jpg'))[0])
        image_3 = Image.open((glob.glob(directory_name+'*_'+str(arr[frame_number*9 + 2])+'.jpg'))[0])
        
        image_4 = Image.open((glob.glob(directory_name+'*_'+str(arr[frame_number*9 + 3])+'.jpg'))[0])
        image_5 = Image.open((glob.glob(directory_name+'*_'+str(arr[frame_number*9 + 4])+'.jpg'))[0])
        image_6 = Image.open((glob.glob(directory_name+'*_'+str(arr[frame_number*9 + 5])+'.jpg'))[0])
        
        image_7 = Image.open((glob.glob(directory_name+'*_'+str(arr[frame_number*9 + 6])+'.jpg'))[0])
        image_8 = Image.open((glob.glob(directory_name+'*_'+str(arr[frame_number*9 + 7])+'.jpg'))[0])
        image_9 = Image.open((glob.glob(directory_name+'*_'+str(arr[frame_number*9 + 8])+'.jpg'))[0])
        
        frame_array = np.concatenate((np.concatenate((np.array(image_1),np.array(image_2),np.array(image_3)),axis=1),np.concatenate((np.array(image_4),np.array(image_5),np.array(image_6)),axis=1),np.concatenate((np.array(image_7),np.array(image_8),np.array(image_9)),axis=1)),axis=0)
        frame_image = Image.fromarray(frame_array,mode='RGB')
        #os.makedirs(directory_name+'frames/')
        frame_image.save(directory_name+'frames/'+str(frame_number)+'.jpg')
        video.write(frame_array)
video.release()
