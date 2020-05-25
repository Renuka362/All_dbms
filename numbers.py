"""
f = open('python/files_demo.txt','r')
#print(f.read())
print(f.name)
f.close()
"""
"""
with open("python/files_demo.txt",'r') as f:
    #f_contents=f.readlines()
    f_contents=f.read(10)
    print(f_contents)
    #f_contents=f.readline()
    #print(f_contents)
    #print(f.read())
    for line in f:
    print(line,end="")
       
"""
"""
with open("python/files_demo.txt",'r') as f:
    size_to_read=10
    f_contents=f.read(
        size_to_read)
    while len(f_contents) > 0:
        print(f_contents,end=",")
        f_contents=f.read(size_to_read)
"""
with open("python/files_demo.txt",'w') as f:
    f.write("Hello :)")
    f.write("Hello :)")
    f.seek(0)
    f.write('y')
    
