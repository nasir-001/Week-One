#Authur: Nasir Lawal
#Date: 22-Nov-2019

"""
Description: Tutorial on how to use "Files and input"
"""

fw = open('sample.txt', 'w')
fw.write("Writting some stuff in my text file\n")
fw.write("I like bacon\n")
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()