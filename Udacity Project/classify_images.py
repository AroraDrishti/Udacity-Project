# Import the classifier function
from classifier import classifier

# Function to classify images
def classify_images(images_dir, res_dic, mod):
    # Iterate over the image filenames in the results dictionary
    for imgf in res_dic:
        # Call the classifier function to get the predicted label for the image
        clf_label = classifier(images_dir + imgf, mod).lower().strip()

        # Get the real label and prediction for the image
        real_label = res_dic[imgf][0]
        prediction = 1 if clf_label == real_label else 0

        # Append the predicted label and prediction to the results dictionary
        res_dic[imgf].append(clf_label)
        res_dic[imgf].append(prediction)

    return None