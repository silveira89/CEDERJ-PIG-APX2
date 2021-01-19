import sys
import random

class sorter:

    @staticmethod
    def randomList(k):
        lista = []
        if (k <= 0):
            lista = [9,3,4,10,100,-5,2,1,4,0,-12]
            return lista
        else:
            i = 0
            while(i < k):
                number = random.randint(10,300)
                lista.append(number)
                i += 1
            return lista

    def __init__(self, debug = False):
        self.debug = debug

    def sort(self, x):
        a = []
        for i in range(len(x)):
            pos = self.binarySearch(a, len(a)-1, x[i])
            a.insert(pos, x[i])
        return a

    def binarySearch(self, arr, larr, x):
        first = 0
        last = larr
        midpoint = 0
        while first <= last:
            midpoint = (first + last) // 2
            if arr[midpoint] == x:
                return midpoint
            elif x < arr[midpoint]:
                last = midpoint - 1
            elif x > arr[midpoint]:
                first = midpoint + 1
        if first > last:
            midpoint = first
        else:
            midpoint = last
        return midpoint

def main():
    s = sorter()
    lista1 = sorter.randomList(0)
    lista2 = s.sort(lista1)
    print("original list = %s" % lista1)
    print("sorted list = %s" % lista2)

    n = lista1[len(lista1)//2]
    b = s.binarySearch(lista2, len(lista2), n)
    print("pos({}) -> sorted list[{}] and found = {}".format(n, b, lista2[b] == n))

    n = 6
    b = s.binarySearch(lista2, len(lista2), n)
    print("pos({}) -> sorted list[{}] and found = {}".format(n, b, b < len(lista2) and lista2[b] == n))

if __name__ == "__main__":
     sys.exit(main())