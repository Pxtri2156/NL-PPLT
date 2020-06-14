with open('BOX.INP') as f:
    content=f.readlines()
content = [x.strip() for x in content]

a=[]
j = 0
for i in content:
    a.append(i.split(" "))

    print(a[j])
    # Chuyển đổi thành int
    a[j][0] = int(a[j][0])
    a[j][1] = int(a[j][1])
    # Sắp xếp lại chiều trong mỗi cặp chiều dài
    if a[j][0] > a[j][1]:
        temp = a[j][0]
        print (temp)
        a[j][0] = a[j][1]
        a[j][1] = temp
    #a[j].append(1)
    j += 1


# Ham so sanh 2 cap do dai
def SoSanh2Cap(a,b):
    if a[0] == b[0] or  a[1] == b[1] or a[1] == b[0] or a[0] == b[1]:
        return True
        #print("True")
    else:
        #print("False")
        return False
    #print(a)

# Ham sap xep lai cac cap chieu dai
def Sap_Xep_2(a):
    l = len(a)
    i = 1
    while (i<l):
        j = i
        while(j<l):
            if a[i-1] == a[j]:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
                i += 1
                break
            if j == l-1:
                return False
            j += 1
        i +=1


def Check_Hinh_Chu_Nhat(a):
    if SoSanh2Cap(a[0],a[2]) and SoSanh2Cap(a[0],a[4]) and SoSanh2Cap(a[2],a[4]):
        return True
    else:
        return False


print("Mang ban dau",a)
t = Sap_Xep_2(a)
print("Mang sau bien doi",a)
out=open("BOX.OUT",'w')
if Check_Hinh_Chu_Nhat(a) and t :
    print("YES")
    out.write('YES')
else:
    print("NO")
    out.write('NO')
out.close()



