# PROGRAMMER: Drishti Arora

# Function to calculate result statistics
def calculates_results_stats(res_dic):
    # Create a dictionary to store result statistics
    res_stt_dic = dict()

    # Initialize the result statistics with initial values
    res_stt_dic['n_images'] = 0
    res_stt_dic['n_dogs_img'] = 0
    res_stt_dic['n_notdogs_img'] = 0
    res_stt_dic['n_match'] = 0
    res_stt_dic['n_correct_dogs'] = 0
    res_stt_dic['n_correct_notdogs'] = 0
    res_stt_dic['n_correct_breed'] = 0

    # Iterate over the keys in the results dictionary
    for key in res_dic:
        # Count the total number of images
        res_stt_dic['n_images'] = len(res_dic)

        # Check if the result is a match
        if res_dic[key][2] == 1:
            res_stt_dic['n_match'] += 1

        # Check if the image is of a dog
        if res_dic[key][3] == 1:
            res_stt_dic['n_dogs_img'] += 1

            # Check if the dog classification is correct
            if res_dic[key][4] == 1:
                res_stt_dic['n_correct_dogs'] += 1

            # Check if the dog breed classification is correct
            if res_dic[key][2] == 1:
                res_stt_dic['n_correct_breed'] += 1

        else:
            # Count the number of images that are not of dogs
            res_stt_dic['n_notdogs_img'] += 1

            # Check if the not-a-dog classification is correct
            if res_dic[key][4] == 0:
                res_stt_dic['n_correct_notdogs'] += 1

        # Calculate the percentage of correct matches
        res_stt_dic['pct_match'] = res_stt_dic['n_match'] / res_stt_dic['n_images'] * 100

        # Calculate the percentage of correct dog classifications and correct dog breed classifications
        if res_stt_dic['n_dogs_img'] > 0:
            res_stt_dic['pct_correct_dogs'] = res_stt_dic['n_correct_dogs'] / res_stt_dic['n_dogs_img'] * 100
            res_stt_dic['pct_correct_breed'] = res_stt_dic['n_correct_breed'] / res_stt_dic['n_dogs_img'] * 100
        else:
            res_stt_dic['pct_correct_dogs'] = 0
            res_stt_dic['pct_correct_breed'] = 0

        # Calculate the percentage of correct not-a-dog classifications
        if res_stt_dic['n_notdogs_img'] > 0:
            res_stt_dic['pct_correct_notdogs'] = res_stt_dic['n_correct_notdogs'] / res_stt_dic['n_notdogs_img'] * 100
        else:
            res_stt_dic['pct_correct_notdogs'] = 0

    # Return the result statistics dictionary
    return res_stt_dic
