import tensorflow as tf
import numpy as np
from messenger import message


def predict(img):
    # im=Image.open(img).resize((250,250))
    img_array = tf.keras.utils.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)

    interpreter = tf.lite.Interpreter(model_path = 'tf_lite_model.tflite')
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    interpreter.resize_tensor_input(input_details[0]['index'], (1, 250, 250,3))
    interpreter.resize_tensor_input(output_details[0]['index'], (1, 2))
    interpreter.allocate_tensors()

    interpreter.set_tensor(input_details[0]['index'], img_batch)
    interpreter.invoke()
    tflite_model_predictions = interpreter.get_tensor(output_details[0]['index'])
    # print("Prediction results:")
    if((tflite_model_predictions[0][1]  > 0.5).astype("int32")==0):
        message()
        return("Accident Detected")
    else:
        return("No Accident")

