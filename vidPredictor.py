import cv2
from predictor import predict
from PIL import Image
import tempfile

img_height = 250
img_width = 250


def vid(f):
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(f.read())

    image=[]
    label=[]
    grabbed=1
    c=1
    cap= cv2.VideoCapture(tfile.name)
    while grabbed:
        grabbed, frame = cap.read()
        if c%30==0:
            resized_frame = cv2.resize(frame, (250, 250), interpolation=cv2.INTER_AREA)
            image.append(frame)

            rgb_frame = resized_frame[:, :, ::-1]
            pil_image = Image.fromarray(rgb_frame)

            label.append(predict(pil_image))
            if(len(image)==75):
                break
        c+=1
    cap.release()
    return label, image
