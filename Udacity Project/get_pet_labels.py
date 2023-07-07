#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Drishti Arora
from os import listdir

def get_pet_labels(image_dir):
    filename_list = listdir(image_dir)
    pet_labels = []
    results_dic = dict()
    for index in range(0, len(filename_list), 1):
        if filename_list[index][0] != ".":
            pet_label = ''
            pet_image_filename = filename_list[index]
            word_list_pet_image_filename = pet_image_filename.lower().split('_')
            pet_name = ''
            
            for word in word_list_pet_image_filename:
                if word.isalpha():
                    pet_name += word + " "
            
            pet_name = pet_name.strip()
            print('Filename = ', pet_image_filename, '    label = ', pet_name)
            print('\n{:2d} file: {:>25}'.format(index + 1, filename_list[index]))
            number_of_items_empty_dic = len(results_dic)
    
            print('\nEmpty dictionary has {} items'.format(number_of_items_empty_dic))
            if filename_list[index] not in results_dic:
                results_dic[filename_list[index]] = [pet_name]
            else:
                print('key =' , filename_list[index],  'already exists in results_dic with value =', results_dic[filename_list[index]])
          
    print('\nPrinting key-value pairs in dictionary results_dic:')
    for key in results_dic:
          print('\nfilename = ', key, '    pet label = ', results_dic[key][0])
            
    number_of_items_full_dic = len(results_dic)
    print('\nEmpty dictionary has {} items'.format(number_of_items_full_dic))
    
    return results_dic