from QuickSort import QuickSort

class VladimirQuickSort(QuickSort):
    def __init__(self, list) -> None:
        super().__init__(list)
        self.n = 17 #default값 17

    def sorting(self, p, r):
        if(p<r):
            if (r-p<self.n):
                self.insertionsort(p, r)
                return 
            L, G = self.partition(p, r)
            self.sorting(p, L-1)
            self.sorting(L+1, G-1)
            self.sorting(G+1, r)

    def partition(self, low, high):
        list = self.list
        if list[low]>list[high]:
            list[low], list[high] = list[high], list[low]
        k = low+1
        l = low
        g = high
        while(k<g):
            if(list[k]>list[high]):
                g=g-1
                list[k], list[g] = list[g], list[k]
                continue
            elif(list[k]<list[low]):
                l = l+1
                list[k], list[l] = list[l], list[k]
            k=k+1
        list[l], list[low] = list[low], list[l]
        list[g], list[high] = list[high], list[g]
        return l, g
    
    def insertionsort(self, p, r):
        list = self.list
        for i in range(p+1, r):
            for j in range(p, i):
                if list[j]>list[i]:
                    break
            m = list[i]
            for k in range(i,j,-1):
                list[k] = list[k-1]
            list[j] = m            

    def nSetter(self, n):
        self.n = n