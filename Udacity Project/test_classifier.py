# Import the classifier function
from classifier import classifier

# Define the test image path
test_image = "pet_images/Collie_03797.jpg"

# Specify the model
model = "vgg"

# Call the classifier function to get the predicted label for the test image
img_clf = classifier(test_image, model)

# Print the results
print("Results ", test_image, " ", model, ": ", img_clf)