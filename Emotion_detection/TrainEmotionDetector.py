
# import required packages
import cv2
from keras.models import Sequential#keras use tenserflow in backend
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator

# Initialize image data generator with rescaling
train_data_gen = ImageDataGenerator(rescale=1./255)#use to preprose the image for training prupose 
validation_data_gen = ImageDataGenerator(rescale=1./255)#use for the testing purpose 

# Preprocess all test images
#flow from directory is very important tool to keras use to flow from the directory and collect data for process
#pass the path of train directory to fetch the image 
train_generator = train_data_gen.flow_from_directory(
        'data/train',
        target_size=(48, 48),#resize it to 48 by 48
        batch_size=64,
        color_mode="grayscale",
        class_mode='categorical')

# Preprocess all train images
validation_generator = validation_data_gen.flow_from_directory(
        'data/test',
        target_size=(48, 48),
        batch_size=64,
        color_mode="grayscale",
        class_mode='categorical')

# create model structure
emotion_model = Sequential()

emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))#creating the layers of convolution 2d layer
emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))#relu is rectifide linear unit 
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))#use to prevent over fitting ,0.25 means 25% of input unit will be randomly set to zero  

emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))

emotion_model.add(Flatten())#use to flatten the input data from multi dimensional to tensor into a one dimension 
emotion_model.add(Dense(1024, activation='relu'))
emotion_model.add(Dropout(0.5))
emotion_model.add(Dense(7, activation='softmax'))#here 7 is the total no of catagory use in this model

cv2.ocl.setUseOpenCL(False)

emotion_model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.0001, decay=1e-6), metrics=['accuracy'])
#Adam is a popular optimization algorithm. It adapts the learning rates of each parameter individually, providing adaptive learning rates.
#lr=0.0001 sets the initial learning rate to 0.0001.
# Train the neural network/model
emotion_model_info = emotion_model.fit_generator(
        train_generator,
        steps_per_epoch=28709 // 64,#total no of image divided by 64
        epochs=50,
        validation_data=validation_generator,
        validation_steps=7178 // 64)

# save model structure in jason file
model_json = emotion_model.to_json()
with open("emotion_model.json", "w") as json_file:
    json_file.write(model_json)

# save trained model weight in .h5 file
emotion_model.save_weights('emotion_model.h5')

