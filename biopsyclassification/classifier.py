import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from keras.preprocessing import image
import numpy as np

class HistClassifier:
    def __init__(self, model_path):
        self.model = Sequential([
            Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Conv2D(128, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Flatten(),
            Dense(128, activation='relu'),
            Dense(5, activation='softmax')
        ])
        self.model.load_weights(model_path)
        self.model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
        self.class_labels = ["доброкачественная опухоль", "хромофобный ПКР", "светлоклеточный ПКР", "онкоцитома", "папиллярный ПКР"] 
   
    def classify(self, img_path):  
        img = image.load_img(img_path, target_size=(256, 256))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255
        prediction = self.model.predict(img_array)

        # Get the predicted class label based on the model's output
        predicted_class_index = tf.argmax(prediction, axis=1).numpy()[0]
        predicted_class = self.class_labels[predicted_class_index]

        scores_of_prediction = [prediction[i] for i in range(len(prediction))]

     
        classes_hist = ["доброкачественная опухоль", "хромофобный ПКР", "светлоклеточный ПКР", "онкоцитома", "папиллярный ПКР"]
        for score_of_prediction, class_hist in zip(scores_of_prediction[0], classes_hist):
            print(
                "Предсказание модели: %s с точностью %.5f !"
                % (class_hist, (100 * score_of_prediction))
            )
           
        return predicted_class