import cv2
import datetime

rstp = "rtsp://admin:samit123@10.3.48.201:554/cam/realmonitor?channel=13&subtype=0"
video = cv2.VideoCapture(rstp)
if (video.isOpened() == False):  
    print("Error reading video file") 
  
# We need to set resolutions. 
# so, convert them from float to integer. 
frame_width = int(video.get(3)) 
frame_height = int(video.get(4)) 
   
size = (frame_width, frame_height) 
tanggal = datetime.datetime.now()
date_time = tanggal.strftime("%H-%M-%S")
print(date_time)
# Below VideoWriter object will create 
# a frame of above defined The output  
# is stored in 'filename.avi' file. 
result = cv2.VideoWriter(f'cctv_{date_time}.mp4',  
                         cv2.VideoWriter_fourcc(*'MJPG'), 
                         10, size)
if not video.isOpened():
 print("Cannot open camera")
 exit()
while True:
    ret, frame = video.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    result.write(frame) 
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
video.release()
result.release() 
cv2.destroyAllWindows()