# PROGRAMMER: Drishti Arora

# Function to adjust results based on whether the images are of dogs or not
def adjust_results4_isadog(res_dic, dogf):
    # Create a dictionary to store dog names
    dgname_dic = dict()

    # Open the dogfile and read its contents
    with open(dogf, "r") as file:
        l = file.readline()

        # Read each line until the end of the file
        while l != "":
            l = l.rstrip("\n")

            # Add the dog name to the dictionary
            if l not in dgname_dic:
                dgname_dic[l] = 1

            # Read the next line
            l = file.readline()

    # Iterate over the keys in the results dictionary
    for key in res_dic:
        # Check if the first element of the result is a dog name
        if res_dic[key][0] in dgname_dic:
            # Check if the second element of the result is a dog name
            if res_dic[key][1] in dgname_dic:
                # Extend the result with 1 for both elements (both are dogs)
                res_dic[key].extend((1, 1))
            else:
                # Extend the result with 1 for the first element and 0 for the second element
                res_dic[key].extend((1, 0))
        else:
            # Check if the second element of the result is a dog name
            if res_dic[key][1] in dgname_dic:
                # Extend the result with 0 for the first element and 1 for the second element
                res_dic[key].extend((0, 1))
            else:
                # Extend the result with 0 for both elements (neither is a dog)
                res_dic[key].extend((0, 0))

        # Print the updated result
        print(res_dic[key])
