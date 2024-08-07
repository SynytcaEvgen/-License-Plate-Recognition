import cv2
from ultralytics import YOLO
import numpy as np
from lib import get_car_with_plate, read_license_plate
from render import render_to_frame
import math

# Load the video file
video_path = './video_examples/car_4.mp4'
cap = cv2.VideoCapture(video_path)
model = YOLO("yolov8n.pt")
license_plate_detector = YOLO('./train_model/models/licens_plate_model.pt')

# Check if the video was successfully opened
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()
     
WIDTH = 1380
HEIGHT = 730

vehicles = [2, 3, 5, 7] #type of vehicle car, truch, bus ...

# Read and display the video frames
while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    
    yoloDetect = model.predict(frame)
    detect_vehicles = []
    to_render_data = []
    for bbox in yoloDetect[0].boxes:
        class_id = int(bbox.cls)
        if int(class_id) in vehicles:
            xyxy = bbox.numpy().xyxy.astype(np.int_).flatten()
            detect_vehicles.append(xyxy)
    
    license_plates = license_plate_detector.predict(frame)
    for license_plate in license_plates[0].boxes:
        lp_box = license_plate.numpy().xyxy.astype(np.int_).flatten()
        
        car_with_plate = get_car_with_plate(lp_box, detect_vehicles)

        if len(car_with_plate['vehicle']) != 0:
            # license_plate_crop = frame[int(lp_box[1]):int(lp_box[3]), int(lp_box[0]):int(lp_box[2])]
            # # process license plate
            # license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
            # _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV)
            # # read license plate number
            # license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_thresh)
            # if license_plate_text is not None:
            #     car_with_plate['license_plate_text'] = license_plate_text
            to_render_data.append(car_with_plate)
    
    render_to_frame(frame, to_render_data)

    # Display the frame
    cv2.imshow('Licens plate recognizer', frame)

    # Press 'q' to quit the video playback
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
