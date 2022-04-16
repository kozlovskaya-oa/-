import sys


pod = input()
str_lst = list(map(str.strip, sys.stdin))
# pod = 'JU'
# str_lst = ['JUJUJU']
min_pod = 1e9 ** 10
need_str = ''

for strok in str_lst:
    if min_pod >= strok.count(pod) and strok.count(pod):
        need_str = strok
        min_pod = strok.count(pod)


print(need_str.split(pod))

print(len(max(need_str.split(pod))) + 1)

index_pod = 0
count = 0
counts = []
for let in need_str:
    print(let, pod[index_pod])
    if let != pod[index_pod]:
        count += 1
        if let != pod[0]:
            index_pod = 0
    elif not index_pod:
        index_pod += 1
        count += 1
    elif index_pod:
        index_pod = 0
        counts += [count]
        count = 1
counts += [count]
print(max(counts))