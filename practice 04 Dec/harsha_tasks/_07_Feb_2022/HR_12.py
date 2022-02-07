# s="aabbbccde"
s="tctesvgnclzykpmbcqixlonfidpdjbynrcpxsjmucpeyormenrjbibafpzkquminfnnbizgbpxeovefuykjrcebfnntvyamkgykcnvjqxvnprwrarpcgrjoucywgfnbnysgwzymcxyachlpsglosflsubqhvobedbtzuqmvgyvrpeclcsoeemysuyuejpjtahnrzmebztrjtzhhjtqlmhttxdnjilqsqymmhjmlzikkdzasshfktbfsaozyhaduyqcufucqxxuksnfjaiwacvlyiimfrzyxwobrfoalhmowcobbpwuqpwvlstbngxjrebfnckbcagoacmfuzvmqxefiwqkgfwgghxbulvhqiaqewdmmizjfgyymchohejdpsnnpvmtgqzxkesnrikywoolootuuikapycpxhkrplyuhzhndxckbvaynkzreybomwuemxtgmrjxbysarlsemwambppmrumivznuaqskzgpamfsjwwrjvtwyqpainuyyfmwnegjlmanqwvshvpsbpeykfwykdumdgjlkuwoxwqctihfdwvxrefggsxmjtxmpdcigjertcxwennzyamqpahytneybgmdyupusarhemazvozdqurftdvbnavynrsdzxjebjrdatbkoezdgwznplqqzakozjecyewsidawuxfpusmeusantzdglridxnwvbgwjcaofbplnwyxtmwerskdzwhgxfdqbpfhymlgwtvqeehnnhwgklxqkdjgmfxvuxwwpmnqxsaiitfehhbqdyveqfrqjjfnggmhjrgldgctnhzrrqdtbunxxcuwibqkjdickhrtbznevczqoidnfmtaveysysrgbhctwxmevuutrwyriugtuvhuxkqapfjyplczgekxisffoivofobqmipqxzunlrrtcmaivvhbfjvgywwtqubwszqwjtskyuxljhinqrhcgddejurivukcspaazjjwwloreqlreqjifwsv"
lst1=[]
for i in s:
    if i not in lst1:
        lst1.append(i)
dict2={}
for i2 in lst1:
    dict2[i2]=s.count(i2)
dict3=dict(sorted(dict2.items(),key=lambda x:x[1],reverse=True))
lst4=[]

count=0
for k,v in dict3.items():
    if v not in lst4:
        lst4.append(v)
        count+=1
        if count>=3:
            break
        else:
            continue
print(lst4)
dict5={}
dict4=dict(sorted(dict3.items(),key=lambda x:x[0],reverse=False))
for k,v in dict4.items():
    if v in lst4:
        dict5[k]=v

dict6= {}
for i6 in lst4:
    for k3,v3 in dict5.items():
        if v3==i6:
            dict6[k3]=v3
count1=0
for k4,v4 in dict6.items():
    print(k4,v4)
    count1+=1
    if count1 >= 3:
        break
    else:
        continue






