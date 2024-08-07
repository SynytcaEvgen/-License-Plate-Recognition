""" Render function """
from lib import draw_border

def render_to_frame(frame, data):
    """ Render """
    for item in data:
        car = item['vehicle']
        plate = item['license_plate']
        # plate_text = item['license_plate_text']
        draw_border(frame, (int(car[0]), int(car[1])), (int(car[2]), int(car[3])), (0, 0, 255), 5,
        	            line_length_x=50, line_length_y=50)
        draw_border(frame, (int(plate[0]), int(plate[1])), (int(plate[2]), int(plate[3])), (0, 255, 0), 2,
        	            line_length_x=10, line_length_y=10)
        
        # print(plate_text)
