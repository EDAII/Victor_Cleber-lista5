
class Interval:

    def __init__(self, title, start, finish):
        self.title = title
        self.start = start
        self.finish = finish
    
    def __repr__(self):
        return str((self.title, self.start, self.finish))


def insertion_sort(nums):
    for i in range(1, len(nums)):
        aux = nums[i]
        j = i-1
        while j>=0 and aux.finish < nums[j].finish:
            nums[j+1] = nums[j]
            j=j-1
        nums[j+1] = aux
    return nums

    
def interval_scheduling(V):
    V = insertion_sort(V)
    A = []
    finish = 0
    for i in V:
        if finish <= i.start:
            print(i.start, i.finish)
            finish = i.finish
            A.append(i)
    return A

if __name__ == '__main__':
    I = []
    I.append(Interval("Summer School" , 1, 5))
    I.append(Interval("Semester 1" , 1, 3))
    I.append(Interval("Semester 2" , 4, 6))
    print(I)
    O = interval_scheduling(I)
    print(O)