print('>_< ' * 5)  # >_< >_< >_< >_< >_<
x = 50
print("_" * x)

# example 2
print(len('abcdefghijklmnopqrstuvwxyz'))
26

# Example 3
s = str(2 ** 100)
print(s)
print(len(s))
1267650600228229401496703205376
31

# Example 5
s = 'abcdefg'
print(s[1])     #b
print(s[-1])    #g
print(s[1:3])   #bc
print(s[1:-1])  #bcdef
print(s[:3])    #abc
print(s[2:])    #cdefg
print(s[:-1])   #abcdef
print(s[::2])   #aceg
print(s[1::2])  #bdf
print(s[::-1])  #gfedcba

# Example 7
s = 'Hello'
print(s.find('e'))
print(s.find('ll'))
print(s.find('L'))
1
2
-1

# Example 8
s = 'abracadabra'
print(s.find('b'))
print(s.rfind('b'))
1
8

# Example 9
s = 'my name is bond, james bond, okay?'
print(s.find('bond'))
print(s.find('bond', 12))
11
23


# Example 12
print('Abracadabra'.count('a'))    # 4
print(('aaaaaaaaaa').count('aa'))  # 5
