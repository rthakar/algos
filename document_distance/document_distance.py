import sys
import math

def main():
    if len(sys.argv) != 3:
        print "Usage: docdist1.py filename_1 filename_2"
    else:
        filename_1 = sys.argv[1]
        filename_2 = sys.argv[2]
        sorted_word_list_1 = word_frequencies_for_file(filename_1)
        sorted_word_list_2 = word_frequencies_for_file(filename_2)
        distance = vector_angle(sorted_word_list_1,sorted_word_list_2)
        print "The distance between the documents is: %0.6f (radians)"%distance

def word_frequencies_for_file(filename):
    lines_list = read_file(filename)
    word_list = line_list_2_word_list(lines_list)#O(n)
    word_frequency_vector = get_word_frequency_vector(word_list)#O(n)
    #print "Frequency vector: "+str(word_frequency_vector)
    return word_frequency_vector

def read_file(filename):
    with open(filename) as f:
        content = f.readlines()
    #print "opened "+filename+" and contents are:\n"+str(content)  
    return content

def line_list_2_word_list(lines_list):#O(n)
    words = []
    for line in lines_list: #Num_lines O(n)
        word = []
        #print "Processing line: "+line
        for char in line: #Num_chars_line
            
            if char.isalnum():#O(1)
                word.append(char)#O(1)
            else:
                if len(word) != 0:#O(1)
                    words.append("".join(word))#O(1)
                    #print "Adding word: "+ words[-1]
                    word = []
            
                
        if len(word) != 0:#O(1)
            words.append("".join(word))#O(1)
            #print "Adding word: "+ words[-1]
    return words

def get_word_frequency_vector(word_list):
    freq_vector = {}
    for word in word_list:#n
        if freq_vector.has_key(word):#O(1)
            freq_vector[word] +=1
        else:#O(1)
            freq_vector[word] = 1
        #print "frequency of "+word+" is "+str(freq_vector[word])
    return freq_vector

def vector_angle(L1, L2):#O(mlg(m)+nlg(n))
    numerator = inner_product(L1, L2);#O(mlog(m))
    denominator = math.sqrt(inner_product(L1, L1) * inner_product(L2, L2))
    return (numerator/denominator)

def inner_product(L1, L2):
    prod = 0
    for key, value in L1.iteritems(): #O(mlog(m))
        if L2.has_key(key):
            prod += value*L2[key]#O(1)
            
            #print "Word " + key +" in L1:"+str(value) + " L2: "+str(L2[key])+ " brings DP to "+str(prod)

    #print "Returning "+str(prod)
    return prod


            
main()
