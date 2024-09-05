import sys
from collections import deque

string = input()
N = int(input())
left = deque(string)
right = deque()

for _ in range(N):
    command = sys.stdin.readline().strip()
    
    if command == 'L' and left:
        right.appendleft(left.pop())
    elif command == 'D' and right:
        left.append(right.popleft())
    elif command == 'B' and left:
        left.pop()
    elif command.startswith('P'):
        left.append(command[2])

print(''.join(left + right))