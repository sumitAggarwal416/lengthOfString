#I, Sumit Aggarwal, student number 000793607, certify that all code submitted is
#my own work and I have not copied from any source. I also certify that I have
#not allowed anyone else to copy my work
user_input= input("Enter any string ")
string_length= len(user_input)
if string_length%2==0:
    print("The input length is even: True")
else:
    print("The input length is even: False")

print("The length is :" + str(string_length))
tag= input("Please enter h1, div or article")
midpoint= round(string_length/2)
first_half= user_input[0:midpoint]
tagged_input= '<'+tag+'>'+first_half+'</'+tag+'>'
tag_length= len(tagged_input)
spaces_needed= round((80-tag_length)/2)
x=1
for x in range(spaces_needed):
    print('\t', end='')
    x+=1

print(tagged_input)
