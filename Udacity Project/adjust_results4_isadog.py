def adjust_results4_isadog(res_dic, dogf):
    # Create a dictionary to store dog names
    dgname_dic = {}

    # Open the dogfile and read its contents
    with open(dogf, "r") as file:
        for line in file:
            l = line.rstrip("\n")

            # Add the dog name to the dictionary
            if l not in dgname_dic:
                dgname_dic[l] = 1

    # Iterate over the keys in the results dictionary
    for key in res_dic:
        # Check if the first element of the result is a dog name
        k0 = key[0]
        if k0 in dgname_dic:
            # Check if the second element of the result is a dog name
            k1 = key[1]
            if k1 in dgname_dic:
                # Extend the result with 1 for both elements (both are dogs)
                res_dic[key].extend((1, 1))
            else:
                # Extend the result with 1 for the first element and 0 for the second element
                res_dic[key].extend((1, 0))
        else:
            # Check if the second element of the result is a dog name
            if k1 in dgname_dic:
                # Extend the result with 0 for the first element and 1 for the second element
                res_dic[key].extend((0, 1))
            else:
                # Extend the result with 0 for both elements (neither is a dog)
                res_dic[key].extend((0, 0))

    # Print the updated result
    for key in res_dic:
        print(res_dic[key])
