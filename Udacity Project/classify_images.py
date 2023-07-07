#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Drishti Arora
from classifier import classifier 

def classify_images(images_dir, results_dic, model):
    for image_file in results_dic:
        classifier_label = classifier(images_dir + image_file, model).lower().strip()

        real_label = results_dic[image_file][0]
        prediction = 1 if real_label in classifier_label else 0
        results_dic[image_file].append(classifier_label)
        results_dic[image_file].append(prediction)
    
    return None