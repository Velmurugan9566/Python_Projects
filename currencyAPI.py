
import requests
res=requests.get('https://api.frankfurter.app/currencies')
re=res.status_code
if re:
    print('\n<..Country List..>')
da=res.json() #Retrieve country list from api 
ke=list(da.keys())
va=list(da.values())
for i in range(len(ke)):
    print(i+1," : ",ke[i],va[i])
cu1=int(input('Select Country Number you want to check: '))
cu2=int(input('Select country number you want to convert: '))
n=input('Enter the amount: ')
fr=ke[cu1-1]
to=ke[cu2-1]
qu=requests.get('https://api.frankfurter.app/latest?amount={}&from={}&to={}'.format(n,fr,to))
ans=qu.json()

values=list(ans.values()) #Retrieve result from dict format get only values

print('\n\t....Result....')
print('Conversion from...> ',va[cu1-1],' To ',va[cu2-1])
print('Date of rate: ',values[2])
answer=list(values[3].values()) #list conversion from dict

print(va[cu1-1],' : ',n,' ----> ',va[cu2-1],' : ',answer[0])
