def add_min_mul_div_mod(a,b):
    return a+b,a-b,a*b,a/b,a%b

sum,min,mul,div,mod = add_min_mul_div_mod(4,2)
sum = add_min_mul_div_mod(4,2)

print("sum" , sum)
print("min" , min)
print("mul" , mul)
print("div" , div)
print("mod" , mod)

print("----------------------------")

print("sum",sum)
print("sum",sum[0])
print("sum",sum[1])
print("sum",sum[2])
print("sum",sum[3])
print("sum",sum[4])