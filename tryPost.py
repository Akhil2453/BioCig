import requests

num = input("Enter the phone number: ")
param = {'action': 'saveUserData', 'MOB': num, 'MCID': '002000244', 'BTNO': '10'}
print(param)
r = requests.post("http://clickcash.in/apisave/apiDataSavever2.php", data=param)
print(r.status_code)
print("content: ", r.content)
print("\nbody: ", r.text)
