import os

class Interval:

    def __init__(self, title, start, finish):
        self.title = title
        self.start = start
        self.finish = finish
    
    def __repr__(self):
        return str((self.title, self.start, self.finish))


def count_sort(nums, max_value):
    output = [0 for i in range(len(nums))]
    count = [0 for i in range(max_value+1)]

    for i in nums:
        count[i.finish] += 1

    for i in range(max_value+1):
        count[i] += count[i-1]

    for i in range(len(nums)-1, -1, -1):
        output[count[nums[i].finish]-1] = nums[i]
        count[nums[i].finish] -= 1

    return output

def insertion_sort(nums):
    for i in range(1, len(nums)):
        aux = nums[i]
        j = i-1
        while j>=0 and aux.finish < nums[j].finish:
            nums[j+1] = nums[j]
            j=j-1
        nums[j+1] = aux
    return nums

    
def interval_scheduling(V, max):
    V = count_sort(V, max)
    A = []
    finish = 0
    for i in V:
        if finish <= i.start:
            finish = i.finish
            A.append(i)
    return A

if __name__ == '__main__':
    max = 7
    I = []
    I.append(Interval("Summer School" , 1, 5))
    I.append(Interval("Semester 1" , 1, 3))
    I.append(Interval("Semester 2" , 4, 6))
    print(I)
    I = interval_scheduling(I, 7)
    print(I)

    while(1):
        print('=========================================')
        print("Choose an option:\n1: Input a task\n2: Interval scheduling\n3: Print\n0: exit")
        ans = int(input())
        if ans == 1:
            print('Choose a name: ')
            name = input()
            print('Choose a start')
            start = int(input())
            print('Choose a finish')
            finish = int(input())
            if finish > max:
                max = finish + 1
            I.append(Interval(name, start, finish))

        if ans == 2:
            I = interval_scheduling(I, max)

        if ans == 3:
            print(I)

        if ans == 0:
            break
            
        print('=========================================')
        ans = input()
        os.system('cls' if os.name == 'nt' else 'clear')