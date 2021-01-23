heap = []


def heapify():
    child = len(heap) - 1
    parent = (child - 1) // 2
    while heap[child] > heap[parent]:
        heap[parent], heap[child] = heap[child], heap[parent]
        if parent == 0:
            break
        child, parent = parent, (parent - 1) // 2


def insert(data):
    heap.append(data)
    if len(heap) == 1:
        return
    # heapify the array after appending element to last
    heapify()


data_array = [41, 39, 33, 18, 27, 12, 55]
for d in data_array:
    insert(d)

print('original array')
print(data_array)
print('Heapify array is')
print(heap)
