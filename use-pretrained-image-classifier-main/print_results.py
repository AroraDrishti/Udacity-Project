#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Drishti Arora

def print_results(results_dict, results_stats_dict, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    print(f'Classifier model: {model}')

    print(f'Number of images: {results_stats_dict["n_images"]}', end=" ")
    print(f'Number of Dog Images: {results_stats_dict["n_dogs_img"]}', end=" ")
    print(f'Number of Not-a-Dog Images: {results_stats_dict["n_notdogs_img"]}')

    def get_key_name(key):
        words = ''
        for word in key:
            if word.isalpha():
                words += word + ' '
        return words.capitalize()

    for key, value in results_stats_dict.items():
        if key.startswith('p'):
            print(f'{get_key_name(key.split("_"))}: {value}')

    if print_incorrect_dogs:
        print("Misclassified Dogs:")
        for key, value in results_dict.items():
            if sum(results_dict[key][3:]) == 1:
                print(f'\tPet Image: {key} Classifier Labels: {results_dict[key][1]}')

    if print_incorrect_breed:
        print("Misclassified Breeds of Dogs:")
        for key, value in results_dict.items():
            if sum(results_dict[key][3:]) == 2 and results_dict[key][2] == 0:
                print(f'\tPet Image: {key} Classifier Labels: {results_dict[key][1]}')
