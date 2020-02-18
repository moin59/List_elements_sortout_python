# author: Moin Uddin
# 18 February 2020
# Bremen

a_list = [18, 9, 200, 8, 10, 2, 3, 6, 9, 100, 3, 11, 500, 5, 4, 7, 1]

def list_sortout(array):

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

sorted_list = list_sortout(a_list)
print("New:",sorted_list,"\n")