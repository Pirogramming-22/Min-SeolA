### 리스트 ### 
lottery=[3,42,12,19,30,10]

lottery.sort() # 오름차순
lottery.reverse() 
print(lottery)

### 딕셔너리 ###
participant={"name":"Ola", "country":"Poland", "favorite_numbers":[7,13]}
participant['favorite_language']="Python"
print(participant)

if 5>2:
    print("5 is indeed greater than 2")
else:
    print("5 is not greater than 2")

name="Sonja"
if name=="Ola":
    print("Hey Ola!")
elif name=="Sonja":
    print("Hey Sonja!")
else:
    print("Hey Anonymous!")

volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')
