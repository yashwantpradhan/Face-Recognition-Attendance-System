import face_recognition
import cv2
import numpy as np
import csv
import pyttsx3
import streamlit as st
import os
import time
from datetime import datetime
from twilio.rest import Client

engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices=engine.getProperty('voices')
engine.setProperty('rate', 170)
engine.setProperty('voice',voices[1].id)



account_sid = "andfncsdnklnsdlknv"
auth_token  = "ejbfjbsdjbfsjbdfj"

client = Client(account_sid, auth_token)
attendee_phone_numbers = {
    "Suraj": "+917858036501",
    "Yashwant": "+919304422684",
    "Harsh":"+917903905785",

}

video_capture=cv2.VideoCapture(0)
sample_image1=face_recognition.load_image_file("Suraj.jpeg")
sample_image1_encoding=face_recognition.face_encodings(sample_image1)[0]

sample_image2=face_recognition.load_image_file("Yash.jpg")
sample_image2_encoding=face_recognition.face_encodings(sample_image2)[0]

sample_image3=face_recognition.load_image_file("Paritosh.jpg")
sample_image3_encoding=face_recognition.face_encodings(sample_image3)[0]

sample_image4=face_recognition.load_image_file("Harsh.jpg")
sample_image4_encoding=face_recognition.face_encodings(sample_image4)[0]

sample_image5=face_recognition.load_image_file("ratan_tata.jpg")
sample_image5_encoding=face_recognition.face_encodings(sample_image5)[0]

sample_image6=face_recognition.load_image_file("Manjar.png")
sample_image6_encoding=face_recognition.face_encodings(sample_image6)[0]

known_face_encoding=[sample_image1_encoding,sample_image2_encoding,sample_image3_encoding,sample_image4_encoding,sample_image5_encoding,sample_image6_encoding]

known_face_names=["Suraj","Yashwant","Paritosh","Harsh","Ratan Tata","Manjar Alam"]


students=known_face_names.copy()
face_locations=[]
face_encodings=[]
face_names=[]
s=True

now=datetime.now()
current_date=now.strftime("%d-%b-%Y")

f=open(current_date +'.csv','w+',newline='')
Inwriter= csv.writer(f)

while True:
    _,frame=video_capture.read()
    small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame=small_frame[:,:,::-1]

    st.image(frame, channels="BGR")
    if st.button("Stop Streamlit"):
        break
    if s:
        face_locations=face_recognition.face_locations(rgb_small_frame)
        face_encodings=face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names=[]
        for face_encoding in face_encodings:
            matches=face_recognition.compare_faces(known_face_encoding,face_encoding)
            name=""
            face_distance=face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index=np.argmin(face_distance)
            if matches[best_match_index]:
                name=known_face_names[best_match_index]

            face_names.append(name)
            if name in known_face_names:
                if name in students:
                    st.success(f"{name} is recognized!")
                    print(name)
                    engine.say("Your attendance has been marked.")
                    engine.runAndWait()
                    students.remove(name)
                    current_time=now.strftime("%I:%M %p")
                    current_date=now.strftime("%d-%b-%Y")
                    Inwriter.writerow([name,current_time,current_date])

                    phone_number = attendee_phone_numbers.get(name)
                    if phone_number:
                       message = client.messages.create(
                            to=phone_number,
                            from_="+178995412878",
                            body=f"Hello {name}, your attendance has been marked at {current_time} on {current_date}.")

    cv2.imshow("attendance system",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

engine.stop()
video_capture.release()
cv2.destroyAllWindows()
f.close()





