arr = ["홍길동","전우치","이순신"]

#자료구조 = stack queue list map array set

# push pop

arr.append("유관순")
#맨 끝에 붙임. = append
print(arr)
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])

arr.insert(0,"차범근")

print(arr)
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

arr.insert(3,"강감찬")
#해당 배열에 추가되고, 나머지는 뒷순으로 밀어낸다.

print(arr)
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])
print(arr[5])

print("--------------------------------------------------------")

arr.insert(len(arr),"강감찬")
print(arr)

print("--------------------------------------------------------")

arr.pop(0)
print(arr)

print("--------------------------------------------------------")

arr.remove("이순신")
print(arr)


