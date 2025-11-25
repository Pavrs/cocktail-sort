import random,time
start = time.time()
y=100000
items = [random.randint(0,10000) for x in range(y)]
def cocktailSort(items):
    n = len(items)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):

        swapped = False
        for i in range (start, end):
            if (items[i] > items[i+1]) :
                items[i], items[i+1]= items[i+1], items[i]
                swapped=True

        if (swapped==False):
            break
        swapped = False

        end = end-1

        for i in range(end-1, start-1,-1):
            if (items[i] > items[i+1]):
                items[i], items[i+1] = items[i+1], items[i]
                swapped = True
        start = start+1

a = [5, 1, 4, 2, 8, 0, 2]
cocktailSort(items)
print("Sorted array is:")



end=time.time()
speed= round(end-start,5)
print(f'Time taken: {speed}')

