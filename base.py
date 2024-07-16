
import numpy as np
import cv2
from ultralytics import YOLO

# for 2D images
model1 = YOLO('runs/detect/train3/weights/best.pt')

# for 3D images
model2 = YOLO('runs/detect/train2/weights/best.pt')

# for  pretrained yolo model
model = YOLO('yolov8m.pt')

# Define the vertices for the quadrilaterals  for  2D convoyerbelt
vertices1 = np.array([(500, 10), (200, 10), (200, 350), (500, 350)], dtype=np.int32)
x1, x2, y1, y2 = 50, 350, 200, 500

# Define vertices for the quadrilaterals for 3D slat convoy belt
vertices1 = np.array([(500, 10), (200, 10), (200, 250), (500, 350)], dtype=np.int32)
x1, x2, y1, y2 = 50, 350, 200, 500

#Define vertices for shelf video
vertices1 = np.array([(200, 0), (0, 0), (0, 350), (200, 350)], dtype=np.int32)
vertices2 = np.array([(300, 0), (220, 0), (220, 350), (300, 350)], dtype=np.int32)
x1 = 300
lane_threshold = 210

# Define the positions for the text annotations on the image
text_position_left_lane = (10, 20)
text_position_right_lane = (450, 50)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 0, 255)  # White color for text
background_color = (0, 0, 255)  # Red background for text

# Open the video
cap = cv2.VideoCapture(" { video path } ")

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('{ path where you want to store  the video in mp4 format}', fourcc, 20.0,
                      (int(cap.get(3)), int(cap.get(4))))

# count for the numebrs
number_of_items = 0
item = 0

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        # Create a copy of the original frame to modify
        detection_frame = frame.copy()

        # Black out the regions outside the specified vertical range
        detection_frame[:x1, :] = 0  # Black out from top to x1
        detection_frame[x2:, :] = 0  # Black out from x2 to the bottom of the frame
        detection_frame[:, :y1] = 0  # Black out from x2 to the bottom of the frame
        detection_frame[:, y2:] = 0  # Black out from x2 to the bottom of the frame

        # Perform inference on the modified frame
        results = model.predict(detection_frame, imgsz=640, conf=0.3)
        processed_frame = results[0].plot(line_width=1)

        # Restore the original top and bottom parts of the frame
        processed_frame[:x1, :] = frame[:x1, :].copy()
        processed_frame[x2:, :] = frame[x2:, :].copy()
        processed_frame[:, :y1] = frame[:, :y1].copy()
        processed_frame[:, y2:] = frame[:, y2:].copy()
        cv2.polylines(processed_frame, [vertices1], isClosed=True, color=(0, 255, 0), thickness=2)
        cv2.polylines(processed_frame, [vertices2], isClosed=True, color=(255, 0, 0), thickness=2)

        # Retrieve the bounding boxes from the results
        bounding_boxes = results[0].boxes

        # for counting change the number in the denominator to get correct answer for each detection
        for box in bounding_boxes.xyxy:
            number_of_items += 1
        item = number_of_items / 20

        #counting for on shelf off shelf video
        onshelf=0
        offshelf=0
        for box in bounding_boxes.xyxy:
            # Check if the vehicle is in the left lane based on the x-coordinate of the bounding box
            if box[0] < lane_threshold:
                onshelf += 1
            else:
                offshelf += 1
        # Add the vehicle count text on top of the rectangle for the left lane
        cv2.putText(processed_frame, f'number of items passed {int(item)}', text_position_left_lane,
                    font, font_scale, font_color, 2, cv2.LINE_AA)
        cv2.putText(processed_frame, f'items picked: {2}', text_position_right_lane,
                    font, font_scale, font_color, 2, cv2.LINE_AA)
        # Write the processed frame to the output video
        out.write(processed_frame)\

        cv2.imshow('Real-time Analysis', processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press Q on keyboard to exit the loop
            break
    else:
        break
cap.release()
out.release()