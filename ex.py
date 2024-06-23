#1st one
st="Print only statements that start with s in this sentence"
string=st.split()
for word in string:
    if word[0]=="s":
        print(word)
        
#2nd one
for i in range(0,11):
    if i%2 ==0:
        print(i, end=" ")
print()

#4th one - use a list comprehension to create a list of all numbers between 1 to 50 which are divisible by 3
ans=[num for num in range(1,51) if num%3==0]
print(ans)


#5th one - go through the string below and if the length of the word is even then print even

sen="print every word in this sentence that has an even number of letters"
word=sen.split()
even=[]
for each in word:
    if len(each)%2==0:
        even.append(each)
print(even)

#6th one - that prints integers from 1 to 100 .but for multiples of 3 "Fizz". instead of number . for multiples of 5 "Buzz" for both 3 and 5 then "FizzBuzz"

answer=["FizzBuzz" if x%3==0 and x%5==0 else "Fizz" if x%3==0 else "Buzz" if x%5==0 else x for x in range(1,101)] 
print(answer)

sen1="create a list of the first letters of every word in the string"
list=[]
words=sen1.split()
for word in words:
    list.append(word[0])
print(list)

