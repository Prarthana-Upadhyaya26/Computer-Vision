# Computer-Vision(Inventory-Management-System)
 This project utilizes computer vision to enhance inventory management systems. It includes models for object detection and scripts for various counting and classification tasks.

## Demo application 
url - "https://computer-vision-l2ha3mqffde2nen9hqf6bz.streamlit.app/".
To get an idea of what the project is about, check it out, something intresting is awaiting you. 

## Models

1. *predefined yolov8m.pt*: A YOLO model with 78 classes. This model can detect a wide range of objects including, but not limited to, people, vehicles, animals, and everyday items.
2. *train2/best.pt*: Trained on 2D carton images.
3. *train3/best.pt*: Trained on 3D carton images.
4. *train4/best.pt*: Trained on images of Arnav, Customer 1, Customer 2, and the user. Note: This model has limited accuracy due to a smaller dataset.

## Scripts

1. *customer.py*: Uses model 4 to detect customers' names.
2. *basketcount.py*: Counts the number of items a lady puts in a bag from a video.
3. *count.py*: Counts items on a conveyor belt. Vertices points can be adjusted to specify detection locations.
4. *on_off_shelf.py*: Counts items on and off a shelf.
5. *train.py*: Script used to train all the models.
6. *name.py*: Counts and names each item on the screen for static images.
7. *name_classifier.py*: Similar to name.py, but works for videos instead of static images.

## Requirements

- Python 3.x
- Streamlit
- SQLite3
- Pandas
- qrcode
- BytesIO
- pyzbar
- os
- OpenCV

## Use Cases

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/inventory-management-system.git
   cd inventory-management-system
2. Demo app
      to get an idea of the entire proh=ject in a quick glance
   url - "https://computer-vision-l2ha3mqffde2nen9hqf6bz.streamlit.app/"
3. using trained models 
      While working on our project we were surprised to find out something as common as a box is not included in the 80 classes of yolov8. Detection of boxes both 2D and 3D could have endless applications in the industry. You can diretly use our pre-trained models.
      1. *train2/best.pt*: Trained on 2D carton images.
      2. *train3/best.pt*: Trained on 3D carton images.
      
      model = torch.hub.load('ultralytics/yolov5', 'custom', path='path/to/train2/best.pt')
4. collabrations
      Feel free to submit issues or pull requests. We welcome contributions to improve the system.
