def print_results(res_dic, res_stt_dic, mod, print_inc_dogs=False, print_inc_breed=False):

    # Print the model used
    print('\nModel used: {}'.format(mod))

    # Print the number of images, dog images, and not dog images
    print('No. of Images: {} No. of Dog Images: {} No. of not Dog Images: {}'.format(
        res_stt_dic['n_images'], res_stt_dic['n_dogs_img'], res_stt_dic['n_notdogs_img']))

    # Print the result statistics
    for key in res_stt_dic:
        if key[0] == 'p':
            print('{}: {}'.format(key, res_stt_dic[key]))

    # Print misclassified dogs if requested and there are misclassified dogs
    if print_inc_dogs == True and (
            res_stt_dic['n_correct_dogs'] + res_stt_dic['n_correct_notdogs'] != res_stt_dic['n_images']):
        for key in res_dic:
            if sum(res_dic[key][3:]) == 1:
                print('MISCLASSIFIED DOGS: {} \n CLF Label?: {}'.format(res_dic[key][0], res_dic[key][1]))

    # Print misclassified breeds if requested and there are misclassified breeds
    if print_inc_breed == True and (
            res_stt_dic['n_correct_dogs'] != res_stt_dic['n_correct_breed']):
        for key in res_dic:
            if sum(res_dic[key][3:]) == 2 and res_dic[key][2] == 0:
                print('MISCLASSIFIED BREEDS: {} \n CLF Label?: {}'.format(res_dic[key][0], res_dic[key][1]))
