fi = open('AIRCREW.IN', 'r')
fo = open('AIRCREW.OUT', 'w')

pilot = [0]
co_pilot = [0]
result = [0]

num_pilots = int(fi.readline())
print('num pilot',num_pilots)
for i in range(num_pilots):
    t1, t2 = fi.readline().rstrip('\n').split(' ')
    pilot.append(int(t1))
    co_pilot.append(int(t2))
    result.append(10 ** 10)
print(result)

for i in range(1, num_pilots + 1):
    for j in range(int(i / 2), 0, -1):
        result[j] = min(result[j] + co_pilot[i], result[j - 1] + pilot[i])
    result[0] = result[0] + co_pilot[i]
print(result)
fo.write(str(result[int(num_pilots / 2)]))
