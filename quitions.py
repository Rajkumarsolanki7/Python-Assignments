x = "aaaaaaaaaaaakkkkkkkkkkkkdddddddddd"
counta = 0
countk = 0
countd = 0
for i in x:
    if i == "a":
        counta+=1
for j in x:
    if j == "k":
        countk+=1
for m in x:
    if m == "d":
        countd+=1

sum = counta,countd,countk

if counta > countd and counta > countk:
    print("a")

elif countd>counta and countd>countk:
    print("d")
else:
    print("k")

        



