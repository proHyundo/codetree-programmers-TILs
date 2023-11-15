n = int(input())
nums = [
    input() for _ in range(n)
]
ans = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            num1 = nums[i]
            num2 = nums[j]
            num3 = nums[k]
            loop = max(len(num1), max(len(num2), len(num3)))
            num1 = num1.zfill(loop)
            num2 = num2.zfill(loop)
            num3 = num3.zfill(loop)

            carry = 0
            for l in range(loop):
                if int(num1[l]) + int(num2[l]) + int(num3[l]) >= 10:
                    carry += 1
            if carry == 0:
                ans = max(ans, int(num1)+int(num2)+int(num3))

print(ans if ans != 0 else -1)