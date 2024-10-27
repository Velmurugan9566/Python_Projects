import requests
res=requests.get('https://api.frankfurter.app/currencies')
print(res.status_code)
da=res.json()
print(da)
print(type(da))
ke=list(da.keys())
va=list(da.values())
for i in range(len(ke)):
    print(i+1," : ",ke[i],va[i])
cu1=int(input('Select Country Number you want to check: '))
cu2=int(input('select country number you want to convert:'))
n=input('Enter the amount:')
fr=ke[cu1-1]
to=ke[cu2-1]
qu=requests.get('https://api.frankfurter.app/latest?amount={}&from={}&to={}'.format(n,fr,to))
print(qu)
ans=qu.json()
li=list(map(list,ans.items()))

da=li[3][1]
print(da[to])
print(qu.status_code)
