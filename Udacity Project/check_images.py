# PROGRAMMER: Drishti Arora

# Import necessary modules
from time import time
from print_functions_for_lab_checks import *
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results


def main():
    # Record the start time of the program
    st_tim = time()

    # Get the command line arguments
    inarg = get_input_args()

    # Check the validity of the command line arguments
    check_command_line_arguments(inarg)

    # Get the pet labels from the images in the specified directory
    res = get_pet_labels(inarg.dir)

    # Check if the pet image labels are created successfully
    check_creating_pet_image_labels(res)

    # Classify the images using the specified architecture
    classify_images(inarg.dir, res, inarg.arch)

    # Check if the images are classified successfully
    check_classifying_images(res)

    # Adjust the results to indicate whether the images are dogs or not
    adjust_results4_isadog(res, inarg.dogf)

    # Check if the labels are correctly classified as dogs or not
    check_classifying_labels_as_dogs(res)

    # Calculate the result statistics
    res_stt = calculates_results_stats(res)

    # Check if the result statistics are calculated correctly
    check_calculating_results(res, res_stt)

    # Print the final results
    print_results(res, res_stt, inarg.arch, True, True)

    # Record the end time of the program
    end_time = time()

    # Calculate and print the total runtime of the program
    tot_time = end_time - st_tim
    print("Total Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time % 3600)/60))+":"
          + str(int((tot_time % 3600) % 60)))


# Call the main function to run the program
if __name__ == "__main__":
    main()
