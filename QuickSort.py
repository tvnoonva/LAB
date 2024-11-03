class QuickSort():
    def __init__(self, list) -> None:
        self.list = list

    def sorting(self, p, r):
        if p<r:
            q = self.partition(p, r)
            self.sorting(p, q-1)
            self.sorting(q+1, r)

    def partition(self, p, r):
        list = self.list
        x = list[r]
        i = p-1
        j = p
        while(j<r):
            if list[j]>x:
                j=j+1
            else:
                i=i+1
                list[i], list[j] = list[j], list[i]
                j=j+1
        list[i+1], list[r]=list[r],list[i+1]
        return i+1


