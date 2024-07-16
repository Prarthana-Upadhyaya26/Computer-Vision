import cv2
from ultralytics import YOLO

model = YOLO('runs/detect/train4/weights/best.pt')

# Open the video
cap = cv2.VideoCapture("{video_path to be entered here}")

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('{video_path where we want to save the predicted video}', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        # Create a copy of the original frame to modify
        detection_frame = frame.copy()

        # Perform inference on the modified frame
        results = model.predict(detection_frame, imgsz=640, conf=0.3)
        processed_frame = results[0].plot(line_width=0)

        # Retrieve the bounding boxes from the results
        bounding_boxes = results[0].boxes

        # Write the processed frame to the output video
        out.write(processed_frame)

        #  running this code on a local machine to view the real-time processing results
        cv2.imshow('Real-time Analysis', processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press Q on keyboard to exit the loop
            break
    else:
        break

cap.release()
out.release()
