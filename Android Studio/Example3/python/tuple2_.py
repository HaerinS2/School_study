x = 2560
y = 1440
x, y = y, x
print(x)
print(y)
a = (123, "abc", True, 123)
print(a[1])
print(a[2:])
print(a[:2])
#a[1] = 2 # 튜플 값 수정 불가능
print(a.index("abc"))
print(a.count(123))