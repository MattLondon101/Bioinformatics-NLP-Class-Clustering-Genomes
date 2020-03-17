# function to convert a DNA sequence string to a numpy array
# converts to lower case, changes any non 'acgt' characters to 'n'
def string_to_array(my_string):
    my_string=my_string.lower()
    my_string=re.sub('[^acgt]','z',my_string)
    my_array=np.array(list(my_string))
    return my_array

