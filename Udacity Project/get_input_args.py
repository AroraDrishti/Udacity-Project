# PROGRAMMER: Drishti Arora

# Import the argparse module
import argparse

# Function to get input arguments
def get_input_args():
    # Create an ArgumentParser object
    p = argparse.ArgumentParser()
    
    # Add arguments to the parser
    p.add_argument('--dir', type=str, default='pet_images/', help='Path to pet images folder')
    p.add_argument('--arch', type=str, default='vgg', help='CNN Architecture')
    p.add_argument('--dogfile', type=str, default='dognames.txt', help='Text with dog names')
    
    # Parse the arguments and return the result
    return p.parse_args()
