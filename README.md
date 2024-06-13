# Face-Verification-Using-A-Siamese-Neural-Network
This project implements a facial verification system using a Siamese Neural Network. The system is designed to verify whether two input images belong to the same person or not.

## Overview
The facial verification system utilizes deep learning techniques to compare facial features and determine the similarity between two images. It employs a Siamese Neural Network architecture, which is a popular choice for one-shot learning tasks like face verification.

The Siamese Neural Network consists of two identical subnetworks, often called "twins," which share the same weights and architecture. The twin networks process each input image separately and produce embeddings, which are vector representations of the input images in a high-dimensional feature space. The embeddings are then compared to calculate the similarity between the images.

## Features
### Face detection:
The system incorporates face detection algorithms to identify and extract facial regions from input images.

### One-shot learning:
The Siamese Neural Network enables the model to learn from a limited number of samples, making it suitable for scenarios where only a few examples are available for each person.

### BinaryCrossLossEntropy:
The network is trained using the BinaryCrossLossEntropy function, which encourages similar images to have closer embeddings and dissimilar images to have greater separation.

### Real-time verification:
The application provides a real-time verification mode that captures images from a webcam and performs facial verification on the fly.

## Requirements
Python 3.x  
TensorFlow  
Keras  
OpenCV  
Kivy  

## Usage
Install the required dependencies using pip install -r requirements.txt. Train the Siamese Neural Network by running the training script train.py. Provide the dataset containing pairs of positive and negative images for training. Once the model is trained, you can run the application using python app.py. The application will open a GUI window showing the webcam feed. Position your face within the camera view and click the "Verify" button to compare your face with the input image. The application will display the verification result.

## Credits
This project is developed by Ahmad Maaz. It is based on the principles of Siamese Neural Networks for face verification and utilizes existing open-source libraries and resources.

Contribution Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please submit a pull request or open an issue.

Enjoy the facial verification system!
