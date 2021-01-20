import cv2
from random import randrange
print('**********Welcome to Face Detector App*********\n-------Modules-------\n1) Photo\n2) Webcam\n3) Video\n')
option = input('Please Select from above: ')

# load some pre-trained data on face frontal from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")



if option == '1':
    # Choose an image to detect faces in
    img = cv2.imread('Shah_Rukh_Khan.jpg')
    # img = cv2.imread('006.png')
    # Must convert to grayscale
    grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(img, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 2)

    print(face_coordinates)

    # Display the images with the faces
    cv2.imshow('Face Detector', img)
    cv2.waitKey()

elif option == '2':
    # To capture video from webcam.
    webcam = cv2.VideoCapture(0)

    # Iterate forever over frames
    while True:
        # read the current frame
        successful_frame_read, frame = webcam.read()
        # must convert to grayscale
        grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect Faces
        face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

        # Draw rectangles around the faces
        for (x, y, w, h) in face_coordinates:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 2)

        # Display the frames  with the faces
        cv2.imshow('Face Detector App', frame)
        key = cv2.waitKey(1)

        # stop if S key is pressed
        if key == 83 or key == 115:
            break

        # release the video-capture object
        webcam.release()


elif option == '3':
    # To capture video from our system.
    video = cv2.VideoCapture('Funny Meme.mkv')

    # Iterate forever over frames
    while True:
        # read the current frame
        successful_frame_read, frame = video.read()
        # must convert to grayscale
        grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect Faces
        face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

        # Draw rectangles around the faces
        for (x, y, w, h) in face_coordinates:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 2)

        # Display the frames  with the faces
        cv2.imshow('Face Detector App', frame)
        key = cv2.waitKey(1)

else:
    print('invalid option')