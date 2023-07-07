#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Drishti Arora
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    print('\nModel used: {}'.format(model))
    print('\nNumber of Images: {} \nNumber of Dog Images: {} \nNumber of "Not-a" Dog Images: {}'.format(results_stats_dic['n_images'], results_stats_dic['n_dogs_img'], results_stats_dic['n_notdogs_img']))
    
    for key in results_stats_dic:
        if key[0] == 'p':
            print('{}: {}'.format(key, results_stats_dic[key]))
            
    if print_incorrect_dogs == True and (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']):
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print('\nMISCLASSIFIED DOGS: \n Pet Image Label?: {} \n Classifier Label?: {}'.format(results_dic[key][0], results_dic[key][1]))
                
    if print_incorrect_breed == True and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        for key in results_dic:   
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print('\nMISCLASSIFIED BREEDS: \n Pet Image Label?: {} \n Classifier Label?: {}'.format(results_dic[key][0], results_dic[key][1]))