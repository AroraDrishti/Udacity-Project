def check_command_line_arguments(inarg):
    if inarg is None:
        print("Not Check CLI Args as get_input_args not defined")
    else:
        print("CLI Args: dir =", inarg.dir, " arch =",
              inarg.arch, "\n dogf =", inarg.dogf)

def check_creating_pet_image_labels(res_dic):
    if res_dic is None:
        print("Not Check CLI Args as get_pet_labels not defined")
    else:
        stp_pt = len(res_dic)
        if stp_pt > 10:
            stp_pt = 10
        print("Pet Img Label Dict ", len(res_dic),
              "key-value pairs \n", stp_pt)

        n = 0
        for key in res_dic:
            if n < stp_pt:
                print("{:3d} key: {:>30}  label: {:>26}".format(
                    n+1, key, res_dic[key][0]))
                n += 1
            else:
                break

def check_classifying_images(res_dic):
    if res_dic is None:
        print("Not Check CLI Args as classify_images not defined")
    elif len(res_dic[next(iter(res_dic))]) < 2:
        print("Not Check Results Dict as classify_images not defined")
    else:
        n_mat = 0
        n_notmat = 0
        for key in res_dic:
            if res_dic[key][2] == 1:
                n_mat += 1
                print("{:>30}: Real: {:>26}   clf: {:>30}".format(
                    key, res_dic[key][0], res_dic[key][1]))

        print("NO MAT:")
        for key in res_dic:
            if res_dic[key][2] == 0:
                n_notmat += 1
                print("{:>30}: Real: {:>26}   clf: {:>30}".format(
                    key, res_dic[key][0], res_dic[key][1]))

        print("No of img ", n_mat + n_notmat, "# of matches ",
              n_mat, "No of not match ", n_notmat)

def check_classifying_labels_as_dogs(res_dic):
    if res_dic is None:
        print("Not Check Results Dict as adjust_results4_isadog not defined")
    elif len(res_dic[next(iter(res_dic))]) < 4:
        print("Not Check Results Dict as adjust_results4_isadog not defined")
    else:
        n_mat = 0
        n_notmat = 0
        print("match ")
        for key in res_dic:
            if res_dic[key][2] == 1:
                n_mat += 1
                print("{:>30}: Real: {:>26}   clf: {:>30}  PetLblDog: {:1d}  ClassLblDog: {:1d}".format(
                    key, res_dic[key][0], res_dic[key][1], res_dic[key][3], res_dic[key][4]))

        print("no match")
        for key in res_dic:
            if res_dic[key][2] == 0:
                n_notmat += 1
                print(
                    "\n{:>30}: \nReal: {:>26}   Classifier: {:>30}  \nPetLabelDog: {:1d}  ClassLabelDog: {:1d}".format(
                        key, res_dic[key][0], res_dic[key][1], res_dic[key][3],
                        res_dic[key][4]))

        print("No of img ", n_mat + n_notmat, "no of match ",
              n_mat, "no of no match ", n_notmat)      