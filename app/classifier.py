import io
from PIL import Image

import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array

from app.const import TARGET_SIZE, PREDICTED_CLASS_DICT


class Classifier:
    def __init__(self, model):
        self.model = model

    def predictions(self, file_data: bytes) -> np.ndarray:
        img = Image.open(io.BytesIO(file_data))
        img = img.convert('RGB')
        img = img.resize(TARGET_SIZE, Image.NEAREST)

        input_arr = img_to_array(img)
        input_arr = np.array([input_arr])
        input_arr = input_arr.astype('float32') / 255.

        return self.model.predict(input_arr)

    def get_predict_classification(self, predictions: np.ndarray) -> int:
        predicted_class = np.argmax(predictions, axis=-1)

        return int(predicted_class)

    def get_predicted_description(self, predicted_class: int) -> str:
        return PREDICTED_CLASS_DICT[predicted_class]
