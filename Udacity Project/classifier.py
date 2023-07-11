import ast
from PIL import Image
import torchvision.transforms as transforms
from torch.autograd import Variable
import torchvision.models as mod
from torch import __version__

# Load the pretrained models
resnet18 = mod.resnet18(pretrained=True)
alexnet = mod.alexnet(pretrained=True)
vgg16 = mod.vgg16(pretrained=True)

# Store the models in a dictionary
models = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# Load the class labels dictionary from the file
with open('imagenet1000_clsid_to_human.txt') as im_class_f:
    im_class_dict = ast.literal_eval(im_class_f.read())

def classifier(img_path, model_name):
    # Open the image using PIL
    img_pil = Image.open(img_path)

    # Define the image preprocessing steps
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    # Preprocess the image
    image_tensor = preprocess(img_pil)

    # Add a batch dimension to the image tensor
    image_tensor.unsqueeze_(0)

    # Get the specified model
    model = models[model_name]
    model.eval()

    # Perform the forward pass to get the model output
    output = model(image_tensor)

    # Get the predicted index
    pred_idx = output.data.numpy().argmax()

    # Return the predicted class label
    return im_class_dict[pred_idx]
