from tflite_model_maker import image_classifier
from tflite_model_maker.image_classifier import DataLoader

data = DataLoader.from_folder('cars/')

model = image_classifier.create(data, epochs=50)

loss, accuracy = model.evaluate(data=data)

model.export(export_dir='./car_labeler/app/src/main/assets/custom_models')
