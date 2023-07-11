import os

def get_pet_labels(image_dir):

    # Get the list of filenames in the image directory
    fname_lst = os.listdir(image_dir)

    # Initialize variables
    pet_lbl = []
    res_dic = {}

    # Iterate over the filenames
    for index in range(0, len(fname_lst), 1):
        # Check if the filename is not hidden
        if fname_lst[index][0] != ".":
            pet_lbl = ""
            pet_img_fname = fname_lst[index]
            word_list_pet_img_fname = pet_img_fname.lower().split("_")
            pet_name = ""

            # Extract the pet name from the filename
            for word in word_list_pet_img_fname:
                if word.isalpha():
                    pet_name += word + " "

            pet_name = pet_name.strip()

            # Print filename and pet label
            print("Filename = ", pet_img_fname, "    label = ", pet_name)
            print(f"\n{index + 1:3d} file: {fname_lst[index]:>25}")

            # Count the number of items in the empty dictionary
            no_of_items_empty_dic = len(res_dic)
            print("Empty dictionary {} items".format(no_of_items_empty_dic))

            # Add the pet name to the dictionary with the filename as the key
            if fname_lst[index] not in res_dic:
                res_dic[fname_lst[index]] = [pet_name]
            else:
                print("key = ", fname_lst[index], " already exists in results_dic with value = ", res_dic[fname_lst[index]])

    # Print key-value pairs in the results dictionary
    print("key-value pairs in results_dic:")
    for key in res_dic:
        print("filename = ", key, "    pet label = ", res_dic[key][0])

    # Count the number of items in the full dictionary
    no_of_items_full_dic = len(res_dic)
    print("Empty dictionary {} items".format(no_of_items_full_dic))

    # Return the results dictionary
    return res_dic