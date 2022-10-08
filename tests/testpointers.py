from pointers import c_malloc as malloc 
from pointers import to_ptr


name = "Unity"
pname = to_ptr(name)
name = "Current"
tname = pname.dereference()

print(name)
print(pname)
print(tname)

