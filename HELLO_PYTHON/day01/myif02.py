a = True
b = False

if a and b:
    print("참")
else:
    print("거짓")
    
print("거짓말")

print("--------------------------")

if a or b:
    print("참")
else:
    print("거짓")
    print("거짓말1")
    
print("거짓말1")

print("---------------------------")

if a or b:
    print("참")
else:
    pass
print("거짓")
#    print("거짓말") <-이건 오류남.
print("거짓말")

