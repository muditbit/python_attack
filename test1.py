#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#

def stringAnagram(dictionary, query):
    # Write your code here
    result = []
    for i in range(len(query)):
        result.append(0)
    
    for i in range(len(query)):
        
        x=query[i]
        sorted_query = sorted(x)
        for j in range(len(dictionary)):
            
            y=dictionary[j]
            sorted_dict = sorted(y)
            if x==y:
                result[i]=result[i]+1
            else:
                result[i]=result[i]
    return result
    

if __name__ == '__main__':
    

    dictionary_count = int(input())

    dictionary = []

    for i in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(dictionary_item)

    query_count = int(input())

    query = []

    for i in range(query_count):
        query_item = input()
        query.append(query_item)

    result = stringAnagram(dictionary, query)

    print(result)

    fptr.close()
