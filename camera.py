import cv2
from simple_facerec import SimpleFacerec

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

class Video(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret,frame=self.video.read()
        frame = cv2.resize(frame, (1920,1080))
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
          y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

          cv2.putText(frame, name,(x1, y1 - 20), cv2.FONT_HERSHEY_DUPLEX, 3, (0, 0, 200), 5)
          cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 10)

          cv2.line(frame, (x1,y1) , (x1+30 , y1) , (255,0,255), 20) #Top Left
          cv2.line(frame, (x1,y1) , (x1 , y1+30) , (255,0,255), 20) #Top Left

          cv2.line(frame, (x2,y1) , (x2-30 , y1) , (255,0,255), 20) #Top Right
          cv2.line(frame, (x2,y1) , (x2 , y1+30) , (255,0,255), 20) #Top Right

          cv2.line(frame, (x1,y2) , (x1+30 , y2) , (255,0,255), 20) #Bottom Left
          cv2.line(frame, (x1,y2) , (x1 , y2-30) , (255,0,255), 20) #Bottom Left

          cv2.line(frame, (x2,y2) , (x2-30 , y2) , (255,0,255), 20) #Bottom Right
          cv2.line(frame, (x2,y2) , (x2 , y2-30) , (255,0,255), 20) #Bottom Right
        ret,jpg=cv2.imencode('.jpg',frame)
        return jpg.tobytes()

