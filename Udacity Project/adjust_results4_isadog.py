#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                            
# PROGRAMMER: Drishti Arora
def adjust_results4_isadog(results_dic, dogfile):
    dognames_dic = dict()
    with open(dogfile, "r") as file:
        line = file.readline()
        while line != "":
            line = line.rstrip("\n")
            if line not in dognames_dic:
                dognames_dic[line] = 1
            line = file.readline()
    for key in results_dic:
        if results_dic[key][0] in dognames_dic:
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((1, 1))
            else:
                results_dic[key].extend((1, 0))
        else:
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((0, 1))
            else:
                results_dic[key].extend((0, 0))
                print(results_dic[key])            