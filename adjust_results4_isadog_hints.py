def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """           
    # Creates dognames dictionary for quick matching to results_dic labels from
    # real answer & classifier's answer
    dognames_dic = dict()

    # Reads in dognames from file, 1 name per line & automatically closes file
    with open(dogfile, "r") as infile:
        # Reads in dognames from first line in file
        line = infile.readline()

        # Processes each line in file until reaching EOF (end-of-file) by 
        # processing line and adding dognames to dognames_dic with while loop
        while line != "":
            # Process line by striping newline from line
            line = line.rstrip('\n')

            # Adds dogname(line) to dognames_dic if it doesn't already exist 
            # in the dognames_dic dictionary
            if line not in dognames_dic:
                dognames_dic[line] = 1

            # Reads in next line in file to be processed with while loop
            # if this line isn't empty (EOF)
            line = infile.readline()

    # Add whether pet labels & classifier labels are dogs by appending
    # two items to the end of the value(List) in results_dic.
    # List Index 3 = whether(1) or not(0) Pet Image Label is a dog AND 
    # List Index 4 = whether(1) or not(0) Classifier Label is a dog
    # Iterate through results_dic, if labels are found in dognames_dic,
    # then append (1, 1) to indicate both labels are dogs.
    # Otherwise, append (0, 0) or (1, 0) or (0, 1) based on the label conditions.
    for key in results_dic:
        # Pet Image Label IS a Dog (found in dognames_dic)
        if results_dic[key][0] in dognames_dic:
            # Classifier Label IS image of Dog (found in dognames_dic)
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((1, 1))
            # Classifier Label IS NOT image of Dog (not in dognames_dic)
            else:
                results_dic[key].extend((1, 0))
        # Pet Image Label IS NOT a Dog image (not found in dognames_dic)
        else:
            # Classifier Label IS image of Dog (found in dognames_dic)
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((0, 1))
            # Classifier Label IS NOT image of Dog (not in dognames_dic)
            else:
                results_dic[key].extend((0, 0))