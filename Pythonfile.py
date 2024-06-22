file_path=r"C:\Users\suhai\OneDrive\Desktop\Wiley Edge\python\June 22\textfile"
with open (file_path,'r') as file1:
    file_content=file1.read()



andcount=0
iscount=0
word=file_content.split()
for w in word:
    if w == "and":
       andcount+=1
    if w=="is" or w=="Is":
        iscount+=1
    

print("And has Occured {} times in the File".format(andcount))
print("is has Occured {} times in the File".format(iscount))
