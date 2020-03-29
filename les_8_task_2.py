# Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter
from heapq import heappush, heappop, heapify


def huffman_code(string):
    heap = []
    for ch, occur in Counter(string).items():
        heap.append([occur, [ch, ""]])

    heapify(heap)

    while len(heap) > 1:
        L = heappop(heap)
        R = heappop(heap)

        for path in L[1:]:
            path[1] = '0' + path[1]
        for path in R[1:]:
            path[1] = '1' + path[1]

        count = [L[0] + R[0]]
        heappush(heap, count + L[1:] + R[1:])

    return heappop(heap)[1:]

def main():
    string = input("Введите строку: ")
    code = dict(huffman_code(string))
    result = " ".join(code[p] for p in string)
    print("Результат кодирования по алгоритму Хаффмана:\n", result)

main()
