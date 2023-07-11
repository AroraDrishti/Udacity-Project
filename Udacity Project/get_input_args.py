import argparse

def get_input_args():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser()

    # Add arguments to the parser
    parser.add_argument('--dir', type=str, default='pet_images/', help='Path to pet images folder')
    parser.add_argument('--arch', type=str, default='vgg', help='CNN Architecture')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='Text with dog names')

    # Parse the arguments and return the result
    args = parser.parse_args()

    return args