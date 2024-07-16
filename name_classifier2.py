import cv2
from ultralytics import YOLO

model = YOLO('yolov8m.pt')

img = cv2.imread("tv_2.jpeg")
results = model.predict(source="tv_2.jpeg", save=True)
# print(results)
results[0].save_txt("result.txt",save_conf=False)

f = open(f"result.txt", "r")
list = f.readlines();
clas_id = []
for line in list:
    clas_id.append(line[:2])

class_counts = {}
for item in clas_id:
    class_name = results[0].names[int(item)]
    if class_name in class_counts:
        class_counts[class_name] += 1
    else:
        class_counts[class_name] = 1

ans = ""
for key in class_counts:
    ans = ans + key + ":" + f"{class_counts[key]}" + " "

print(class_counts)
print(ans)

frame = results[0].plot(line_width=1)
cv2.putText(frame, ans, (20, 45), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),thickness=3)
while True:
    cv2.imshow("totalcount", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press Q on keyboard to exit the loop
        break