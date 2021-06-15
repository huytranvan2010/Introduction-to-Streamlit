from tensorflow.keras.models import load_model
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

classifier = load_model('DogCat.h5')
image = load_img('dog.jpg', target_size=(64, 64))
image = img_to_array(image) / 255.
image = np.expand_dims(image, axis=0)

pred = classifier.predict(image)[0][0]

if pred > 0.5:
    print("This is a dog")
else:
    print("This is a cat")