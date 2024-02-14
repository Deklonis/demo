#сортировка пузырьком

def f(arr):
    for i in range(len(arr)-1):
        fl = True
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                fl = False
        if fl:
            break

#сортировка выбором
def f(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

#сортировка вставками
def f(arr):
    for i in range(len(arr)):
        cr = arr[i]
        pos = i
        while pos > 0 and arr[pos-1] > cr:
            arr[pos] = arr[pos-1]
            pos -= 1
        arr[pos] = cr