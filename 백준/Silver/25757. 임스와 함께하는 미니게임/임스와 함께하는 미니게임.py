N, G = input().split()
N = int(N)
min_people = 0
if G == 'Y':
    min_people = 1
elif G == 'F':
    min_people = 2
else:
    min_people = 3

lst = set()
for _ in range(N):
    lst.add(input())

answer = len(lst) // min_people
print(answer)
