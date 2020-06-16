#luu y cac file G.txt khong duoc chua DAU CACH giua cac bieu thuc
# Dau mui ten quy dinh la  "->"
# Chuoi nhap vao cung ko duoc chua DAU CACH 
# Day la code uu tien REDUCE

grammar = {}
#Nhap quy luat
temp = []
f = open("/content/sample_data/G.txt")
for line in f.readlines():
  #print(line)
  a = line.strip("\n").split("->")
  temp.append(a)
#print("temp",temp)
T = temp[-1][0]

# Gan lai grammar tu duoi len
for i in range(len(temp)-1,-1,-1):
  grammar[temp[i][1]] = temp [i][0]
print(grammar)

inp_str = input("Nhap bieu thu can phan tich cu phap:")
result = ""
action = []
print("result\tstring\taction")
for i in range(len(inp_str)):
  #print("i",i)
  #print(inp_str[i])
  result = result + inp_str[i]
  print("{result}\t{inp_str}\tshift ".format(result = result,inp_str = inp_str[i+1:]))
  #inp_str = inp_str[i+1:]
  for j in range(i,-1,-1):
    action = len(temp)
    for key in grammar.keys(): #duyet nguoc
      if result[j:] == key:
        result = result[:j] + grammar[key]
        print("{result}\t{inp_str}\t{action} ".format(result = result,inp_str = inp_str[i+1:],action = action))
      action -=1
fw = open("/content/sample_data/input.txt","w+")
if result == T:
  fw.write("Accepted")
else:
  fw.write("Fail")
f.close()
fw.close()

