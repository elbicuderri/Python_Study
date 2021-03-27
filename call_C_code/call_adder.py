import ctypes

adder = ctypes.CDLL("adder.so")

res_int = adder.add_int(4, 5)
print(f"4 + 5 = {res_int}")

f1 = ctypes.c_float(5.5)
f2 = ctypes.c_float(2.3)

add_float = adder.add_float
add_float.restype = ctypes.c_float

print(f"5.5 + 2.3 = {add_float(f1, f2)}")