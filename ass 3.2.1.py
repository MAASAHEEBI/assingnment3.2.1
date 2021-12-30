'''Write a Python program to reverse a string.

Sample String : "1234abcd"
Expected Output : "dcba4321"'''



def rev():
    s=input('Enter a string: ')
    return (s[-1::-1])
print(rev())
