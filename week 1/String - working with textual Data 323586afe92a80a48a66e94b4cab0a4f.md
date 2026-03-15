# String - working with textual Data

```python
message = ‘Hello World’

new_message = message.replace("World","Universe")

print(message[0]) # W
```

```python
print(message[:5]) # World  - Slicing
message.find('World') ## 6 - it returns the index from where it starts
message.count('l')   ## 3 there are 3 l in the string Hello World 
```

```python
greeting = 'Hello'
name = 'Michael'

message = greeting + name    #HelloMichael  - so when we cconcatenate it leaves no space

message = greeting + ", " + name

print(message)    # Hello, Michael
```

So instead of using this we can use a formatted string to print it hassle free

```python
message = '{}, {}. Welcome!'.format(greeting, name) 

# this will replace the curley braces with the actual value so the output will be like
Hello, Michael. Welcome!
```

this may be vary based on the version of python we use

```python
message = f'{greetings}, {name}. Welcome!' 
# this is also a formatted string , we directly write the variable in place of the placeholders
```

a little trick to see what are the different methods that are available for that specific variable

```python
greeting = "Hello"
name = "Michael"

print(dir(name))
# it'll show us all of the attributes and methods that we have access to
```