#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Drishti Arora
import argparse

def get_input_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--dir', type = str, default = 'pet_images/', help = 'path to the folder of pet images')
    parser.add_argument('--arch', type = str, default = 'vgg', help = 'CNN Model Architecture')
    parser.add_argument('--dogfile', type = str, default = 'dognames.txt', help = 'Text File with Dog Names')
    return parser.parse_args()
