""" Render function """
from lib import draw_border
import cv2

def render_to_frame(frame, data):
    """ Render """
    for item in data:
        car = item['vehicle']
        plate = item['license_plate']
        # plate_text = item['license_plate_text']
        draw_border(frame, (int(car[0]), int(car[1])), (int(car[2]), int(car[3])), (0, 0, 255), 5,
        	            line_length_x=50, line_length_y=50)
        
        w = 0
        d = 0
        license_plate_crop = frame[int(plate[1] + d):int(plate[3] - w), int(plate[0] + d):int(plate[2] - w)]
        license_crop = cv2.resize(license_plate_crop, (int((plate[2] - plate[0]) * 100 / (plate[3] - plate[1])), 100))
        H, W, _ = license_crop.shape
        try:
        	frame[int(car[1]) - H - 5:int(car[1]) - 5,
                      int((car[2] + car[0] - W) / 2):int((car[2] + car[0] + W) / 2), :] = license_crop
        except:
            pass
        
        draw_border(frame, (int(plate[0]), int(plate[1])), (int(plate[2]), int(plate[3])), (0, 255, 0), 2,
        	            line_length_x=10, line_length_y=10)
        # print(plate_text)

