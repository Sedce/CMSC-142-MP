
# coding: utf-8

# In[ ]:


import random
import math

def selection_sort(collection):
    comparisons = 0;
    length = len(collection)
    for i in range(length):
        least = i
        for k in range(i + 1, length):
            comparisons += 1
            if collection[k] < collection[least]:
                least = k
        collection[least], collection[i] = (
            collection[i], collection[least]
        )
    return  comparisons, collection

# In[ ]:


def insertion_sort(data, gap):
    #count = 0
    swaps = 0;
    #totalswaps = 0;
    totalcomp = 0;
    for index in range(gap, len(data)):
        count = 0;
        #swaps = 0;
        while 0 < index and data[index] < data[index - gap]:
            count += 1
            data[index], data[
                index - gap] = data[index - gap], data[index]
            swaps += 1
            index -= gap
        count += 1;
        totalcomp += count;
        #totalswaps += swaps;
        #print ('Swaps: ', swaps)

    #print ("Total Comp: ", totalcomp)
    #return totalcomp, swaps, data
    #print('Total Swaps -->', totalswaps)
    return totalcomp, swaps, data


# In[ ]:


def bubble_sort(data):
    count = 0
    while True:
        swapped = False
        for i in range(1, len(data)):
            count += 1
            if data[i-1] > data[i]:
                data[i-1], data[i] = data[i], data[i-1]
                swapped = True
        if not swapped:
            break
    return count, data


# In[ ]:





# In[ ]:


def get_Unsortedness(data):
    counter = 0;
    comparisons = 0;
    i = 0
    for index in range(1, len(data)):
        counter+=1
        comparisons += 1
        #print (index)
        while 0 < index and data[index] < data[index - 1]:
            counter += 1
            index -= 1
            #comparisons += 1
    
    comparisons += 1
    return comparisons, counter


# In[ ]:


def shell_sort_v2(array):
    count = 0;
    gap = len(array) // 2
    commulative_comp = 0;
    while gap > 0:
        #print ("Shell sort: ", array)
        # do the insertion sort
        #for i in range(gap, len(array)):
        #    count = 0;
        #    val = array[i]
        #    j = i
        #    while j >= gap and array[j - gap] > val:
        #        count += 1;
        #        array[j] = array[j - gap]
        #        j -= gap
        #        count += 1
        #    array[j] = val
        #    count += 1
            #numcomp += count
        result = insertion_sort(array, gap)
        commulative_comp += result[0]
        #print("Gap", gap ,"Comparisons: ", commulative_comp)
        gap //= 2
        
    #return numcomp, array
    #print ("Total Comparisons: ", commulative_comp)
    return commulative_comp,array


# In[ ]:


# Marcin Ciura's gap sequence
def shell_sort_v1(collection):
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    count = 0
    total_comparisons = 0
    for gap in gaps:
        i = gap
        swaps = 0;
        #while i < len(collection):
        #    temp = collection[i]
        #    j = i
        #    while j >= gap and collection[j - gap] > temp:
        #        swaps += 1
        #        collection[j] = collection[j - gap]
        #        j -= gap
        #    collection[j] = temp
        #    i += 1
        result = insertion_sort(collection, gap)
        total_comparisons = result[0]
        #print("Shell Sort: ", collection)
        #print ("Gap: ", gap, " ",result[0])
        #print (swaps)
        #print (collection)
    #print ("Total Comparisons: ", total_comparisons)
    return total_comparisons, collection


# In[ ]:


DEFAULT_BUCKET_SIZE = 5

def bucketSort(myList, bucketSize=DEFAULT_BUCKET_SIZE):
    if(len(myList) == 0):
        print('You don\'t have any elements in array!')

    minValue = myList[0]
    maxValue = myList[0]

    # For finding minimum and maximum values
    for i in range(0, len(myList)):
        if myList[i] < minValue:
            minValue = myList[i]
        elif myList[i] > maxValue:
            maxValue = myList[i]

    # Initialize buckets
    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    # For putting values in buckets
    for i in range(0, len(myList)):
        buckets[math.floor((myList[i] - minValue) / bucketSize)].append(myList[i])
        

    # Sort buckets and place back into input array
    sortedArray = []
    for i in range(0, len(buckets)):
        insertion_sort(buckets[i],1)
        for j in range(0, len(buckets[i])):
            sortedArray.append(buckets[i][j])


    print("Number of buckets %s", len(buckets))
    for i in range(0, len(buckets)):
         if buckets[i]:
                 print("Buckets ", len(buckets[i]), "First: ", buckets[i][0])
        
    return sortedArray, buckets

