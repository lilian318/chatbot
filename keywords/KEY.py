a='reduce,change,cancel order'
b='how to find,picture,search'
c='picture,image,picture search'
d='shipping fee, sea, express,price, reach,duration'
e='send to you, address, help ship, can u ship for you, send for me'
f='next,payment done,confirm payment,how is going,how far'
g='exchange rate,rate,rmb to naira,dollar rate'
h='how do I get you,how you get me,contacts,know my number,profile'
i='send me ur address, chinese address, location, send goods to'
j='christmas'
k='committee fee,committe, #3000'
l='buy from 1688,find links from 1688'
m='payment account,account, alipay,bank'
n='ghana,ghana price'
o='hi,hello,hey,how are you'






keys=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]
#---------------------------don't modify the below line--------------------------------------------
key=[]
for i in keys:
    m=i.split(",")
    a=[i.strip(" ") for i in m]
        
    s="|".join(a)
    key.append(s)
Count=len(key)