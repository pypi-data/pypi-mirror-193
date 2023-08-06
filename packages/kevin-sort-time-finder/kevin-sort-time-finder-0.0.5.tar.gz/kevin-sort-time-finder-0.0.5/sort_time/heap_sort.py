from heapq import heappop, heappush  
   
def heapsort(list1):  
    heap = []  
    for ele in list1:  
        heappush(heap, ele)  

    sort = []  

    # the elements are lift in the heap  
    while heap:  
        sort.append(heappop(heap))  

    return sort  
