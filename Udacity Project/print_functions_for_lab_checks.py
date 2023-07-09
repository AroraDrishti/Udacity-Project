# PROGRAMMER: Drishti Arora

# Function to check command line arguments
def check_command_line_arguments(inarg):
    if inarg is None:
        print("Not Check CLI Args as get_input_args not defined")
    else:
        print("CLI Args: dir =", inarg.dir, " arch =",
              inarg.arch, "\n dogf =", inarg.dogf)

# Function to check creating pet image labels


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

# Function to check classifying images


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

# Function to check classifying labels as dogs


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
                print("\n{:>30}: \nReal: {:>26}   Classifier: {:>30}  \nPetLabelDog: {:1d}  ClassLabelDog: {:1d}".format(key,
                      res_dic[key][0], res_dic[key][1], res_dic[key][3], res_dic[key][4]))

        print("No of img ", n_mat + n_notmat, "no of match ",
              n_mat, "no of no match ", n_notmat)

# Function to check calculating results


def check_calculating_results(res_dic, res_stt_dic):
    if res_stt_dic is None:
        print("Not Check Results Dict as calculates_results_stats not defined ")
    else:
        n_images = len(res_dic)
        n_pet_dog = 0
        n_class_cdog = 0
        n_class_cnotd = 0
        n_mat_breed = 0

        for key in res_dic:
            if res_dic[key][2] == 1:
                if res_dic[key][3] == 1:
                    n_pet_dog += 1
                    if res_dic[key][4] == 1:
                        n_class_cdog += 1
                        n_mat_breed += 1
                else:
                    if res_dic[key][4] == 0:
                        n_class_cnotd += 1
            else:
                if res_dic[key][3] == 1:
                    n_pet_dog += 1
                    if res_dic[key][4] == 1:
                        n_class_cdog += 1
                else:
                    if res_dic[key][4] == 0:
                        n_class_cnotd += 1

        n_pet_notd = n_images - n_pet_dog
        pct_corr_dog = (n_class_cdog / n_pet_dog)*100
        pct_corr_notdog = (n_class_cnotd / n_pet_notd)*100
        pct_corr_breed = (n_mat_breed / n_pet_dog)*100

        print("Stt calculates_results_stats():")
        print("img: {:3d}  n dog img {:3d} n notdog img: {:3d} nPct Corr dog: {:5.1f} Pct Corr NOTdog: {:5.1f}  Pct Corr Breed: {:5.1f}".format(
              res_stt_dic['n_images'], res_stt_dic['n_dogs_img'],
              res_stt_dic['n_notdogs_img'], res_stt_dic['pct_correct_dogs'],
              res_stt_dic['pct_correct_notdogs'],
              res_stt_dic['pct_correct_breed']))
        print("n img {:2d}  n dog img {:2d}  n notdog img {:2d} Pct Corr dog: {:5.1f} Pct Corr NOTdog: {:5.1f}  Pct Corr Breed: {:5.1f}".format(
              n_images, n_pet_dog, n_pet_notd, pct_corr_dog, pct_corr_notdog, pct_corr_breed))
