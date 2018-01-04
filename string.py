para_str = """this is a long string that is made up of
several lines with TAB ( \t ) and NEWLINEs [ \n ] is displayed.
"""
print (para_str)

print ('C:\\nowhere')    # outputs C:\nowhere
print (r'C:\\nowhere')

#Built-In String Methods
str = "Find the substring and comapare with other string, if matches generate new string "
print (len(str))
print (max (str))   # max alphabetical character from the string str
print(str.capitalize())
print (str.upper())
#str.center(width[, fillchar])
print(str.center(100, '*')) # width of output string, fillchar is char to be appended
#str.count(sub, start = 0,end = len(string))
print(str.count('string',0,len(str)))
print(str.isalnum())
print(str.isdigit())
print(str.islower())
#str.replace(old, new[, max])
print(str.replace('string', 'number', 1))
print(str.split(' ', 2)) # slipt for two instance of delimiter
print(str.split(' '))
