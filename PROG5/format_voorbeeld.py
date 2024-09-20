hour = 7
minute = 15
second = 32

"""
Error: int + str kan niet.

>>> print(hour+':'+minute+':'+second)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    print(hour+':'+minute+':'+second)
"""

# Normale print
print(str(hour)+':'+str(minute)+':'+str(second))
# F-string
print(f"{hour}:{minute}:{second}")
