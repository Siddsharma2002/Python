import csv
string1="horse"
string2="rose"
def func(i,j,string1,string2):
    if(i<0) :
        return j+1
    if(j<0) :
        return i+1
    if(string1[i]==string2[j]):
        return func(i-1,j-1,string1,string2)
    else:
       return min(func(i-1,j,string1,string2),func(i,j-1,string1,string2),func(i-1,j-1,string1,string2)) +1
def MainFunc(string1,string2):
    len1=len(string1)
    len2=len(string2)
    x = func(len1-1,len2-1,string1,string2)
    return x
    #print(x)
ans=MainFunc(string1,string2)
y=str(ans)
with open("data5.txt", 'w') as f:
    f.write(y)

