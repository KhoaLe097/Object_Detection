import cv2
import numpy as np

cap = cv2.VideoCapture('workplace.mp4')

    ###Create list_name for identìication
list_name = []
file_path = 'coco.names'
with open(file_path,'rt') as f:
    list_name = f.read().rstrip('\n').split('\n')
# a=0
# for name in list_name:
#     print(a,name)
#     a+=1

    ###Import trained model

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightPath = 'frozen_inference_graph.pb'
net = cv2.dnn_DetectionModel(weightPath,configPath)
net.setInputSize(300,300)
net.setInputScale(1/255)
net.setInputMean((127,127,127))
net.setInputSwapRB(True)



while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(0,0), fx = 0.2, fy = 0.2)

    ###Apply model
    IDs, confs, boxes = net.detect(frame, confThreshold=0.6)
    # print(type(IDs), type(confs), type(boxes))
    if len(IDs) != 0:
        for ID,conf,box in zip(IDs.flatten(),confs.flatten(),boxes):
            cv2.rectangle(frame,box,color=(255,0,0), thickness=1)
            cv2.putText(frame,list_name[ID-1], (box[0]+10,box[1]-10), cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,150,0),2)
            # treat_conf = int(conf*100)
            cv2.putText(frame,str(int(conf*100))+'% confidence', (box[0]+0, box[1]-30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    else:
        cv2.putText(frame, 'Not detect', (100,100), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 0, 0), 2)
    cv2.imshow("workplace",frame)
    if cv2.waitKey(1) == ord("c"):
        break
cap.release()
cv2.destroyAllWindows()
