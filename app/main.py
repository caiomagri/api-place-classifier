from keras.layers import Activation
from keras.models import load_model, Model

from app.classifier import Classifier

from fastapi import FastAPI, File, UploadFile

app = FastAPI()
model = load_model('app/src/model/best_model.h5')
output = model.output
activation = Activation('softmax', name='activation_add')(output)
keras_model = Model(model.input, activation)
keras_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


@app.post("/predict")
def predict(file: UploadFile):
    file_data = file.file.read()
    classifier = Classifier(keras_model)
    predictions = classifier.predictions(file_data)
    classification = classifier.get_predict_classification(predictions)
    description = classifier.get_predicted_description(classification)
    return {"classification": classification, "description": description, "predictions": predictions.tolist()}
