#### FizzBuzz
```
def fizzbuzz(n):
    if n%3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)
        
print("\n".join(fizzbuzz(n) for n in xrange(1,10))
```

```
import urllib.request

u = urllib.request.urlopen('url')
data = u.read()
print(data)
```

```
from xml.etree.ElementTree import XML
doc = XML(data)

for element in doc.findall('element'):
    print(element.text)
```

### Reading command line arguments
```
import sys

if len(sys.argv) != 3:
    raise SystemExit('Usage: file.py arg1 arg2 arg3')

one = sys.arg[1]
two = sys.arg[2]
three = sys.arg[3]

print('Command options:', sys.argv)
raise SystemExit(0)
```

### Use python progaram as script
include the following line on top of the script
```
#!/usr/bin/env python3
```

### Syntax
While
```
while condition > 0:
    statement1
    statement2
```

If..else
```
    if condition == 0 and condition != -1 or condition == 1:
        statement1
    elif n % 3 == 0:
        statement
    else:
        statement
```

### Formatted output
```
name = 'IBM'
shares = 100
price = 32.2

print(name, shares, price)
output => IBM 100 32.2

print('%10s %10d %10.2f' % (name, shares, price))
output =>       IBM       100     32.20     ##Print a character 10 characters wide

print('{:>10s} {:>10d} {:>10.2f}'.format(name, shares, price))
```

### File operations
Write content to a file
```
out = open('file.txt', 'w')  ## Open a file file writing
print('{:>10s} {:>10d} {:>10.2f}'.format(name, shares, price), file=out)  ## write output to file
out.close()    ## close the file
```
Reading a file
```
f = open('file.txt', 'r') ## Open a file for reading
data = f.read()     ## Entire file data is read into the object data
```

Reading file line by line
```
f = open('file.txt', 'r') ## Open a file for reading
## reading data
for line in f:
    print(line)
f.close()
```

using with statement
```
with open('file.txt','r') as f:
    data = f.read
```

#### Text Manupulation
```
a = 'hello world'
b = "hello world"
>>> a[0]
'h'
>>> a[1]
'e'
>>> a[-1]
'd'
>>> a[0-5]
'hello'
>>> a[:5]
'hello'
>>> a[-5:]
'world'
>>> len(line)
>>> c= a + b
>>> line.strip() ## cleans up the end characters
>>> line.strip('"')
>>> line.replace('"', '-')
>>> line.split(',') ## Splits into a list
```
### Some modules
1. pdb - python debugger
2. sys - System specific paramaters and libraries
2. csv - 
