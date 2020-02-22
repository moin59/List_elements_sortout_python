# author: Moin Uddin
# 18 February 2020
# Bremen

def listsort(array):

    for p in range(len(array)):
        _ = p

        for q in range(len(array)-1):
            
            while(array[q] > array[q+1]):
                
                for i, j in zip(range(len(array)-1), range(1,len(array))):

                    if array[i] > array[j]:
                        array[i], array[j] = array[j], array[i]
                    elif array[i] == array[j]:
                        array[i], array[j] = array[i], array[j]
                        exit
                break

    return array
