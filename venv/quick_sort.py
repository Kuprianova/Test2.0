def quickSort(s):
    number = s[0]
    if len(s)<=1:
        return s
    else:
        less = [x for x in s if x<number]
        greater = [x for x in s if x>number]
        equal = [x for x in s if x==number]
        return (quickSort(less) + equal + quickSort(greater))

n=int(input())
s=list(map(int,input().split()))
s = quickSort(s)

print([x for x in s if x%2==0])

