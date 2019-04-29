# Rail Fence
The Rail Fence transposition takes a sentence breaks it into a number of rails; which must be greater than zero. The transposition assigns each letter sequentially to a rail and then presents the text in rail order.  i.e. all letters assigned to the first rail are presented first, then the second rail etc.

```py
from transposition.railfence import RailFence

line = "the lazy brown dog fox"

rf = RailFence(number_of_rails=3)
foo = rf.encrypt(line=line)
bar = rf.decrypt(line=foo)

print(f"line: {line}")
print(f"encrypt: {foo}")
print(f"decrypt: {bar}")
```
Returns
```
line: the lazy brown dog fox
encrypt: t zbwd xhlyrnofea o go
decrypt: the lazy brown dog fox
```