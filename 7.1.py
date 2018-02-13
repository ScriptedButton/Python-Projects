file = open('hello.txt', 'w')
file.write("Hello, World!")

file.close()

read = open('hello.txt', 'r').read()
print(read)