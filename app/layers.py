# Custom L1 Distance Layer module
# needed to load the custom model

#Importing dependencies
import tensorflow as tf
from keras.layers import Layer
from tensorflow.keras.layers import Layer 

# Custom L1 Distance Layer from jupyter
class L1Dist(Layer):
    def __init__(self, **kwargs):
        super().__init__()
    
    # similarity calculation
    def call(self, input_embedding, validation_embedding):
        return tf.math.abs(input_embedding - validation_embedding)
