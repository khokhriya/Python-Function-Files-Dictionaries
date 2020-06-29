<h1> Alternative File Reading Methods</h1>
# write,read(n),readline(n),readlines(n)


# 1. Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.
file_scol=open("school_prompt2.txt", "r") # open file in read mode
content=file_scol.read() # assign content of file to content variable
print(content) #print the content
num_char=len(content) # Getting the no of characters in content
print(num_char)  # Printing Counts


# 2. Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.
file_travl=open("travel_plans2.txt","r")   # open file in read mode
content=file_travl.readlines()   # assign content of file to content variable
num_lines=len(content)   # Getting the no of lines in content
print(num_lines) # Printing Counts

# 3.Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.
file_emotion=open("emotion_words2.txt","r")
first_forty=file_emotion.read(40)
print(first_forty)