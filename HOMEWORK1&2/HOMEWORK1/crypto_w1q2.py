import string
import re
cipherlist = []
testkeys = []
for i in range(0x00,0xff):
    testkeys.append(i)
#加入所有可能密钥
potentialchars = test_chars = string.ascii_letters + string.digits + ',' + '.' + ' '
re__ = '[A-Za-z0-9,. ]'
def findindexkey(arr):
    global testchars
    global testkeys
    anskeys = list(testkeys)#不要使用anskeys =testkeys，python复习了属于是
    for i in testkeys:
        for s in arr:
            if chr(s ^ i) not in potentialchars:
                anskeys.remove(i)
                break
            #if re.search(re__,str(chr(s ^ i))):
            #    pass
            #else:
            #    anskeys.remove(i)
            #    break
            #使用正则表达式的实现方法
    return anskeys
#找出所有可能密钥，通过删除实现


text = 'F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794'
for i in range(0,len(text),2):
    cipherlist.append(int(text[i:i+2],16))

for keylenth in range(1,12):
    for index in range(0,keylenth):
        modedlist = cipherlist[index::keylenth]
        anskeys = findindexkey(modedlist)
        #print(f"anskeys={anskeys},index is {index},and at this time the len is {keylenth}")
#此时发现只有7的时候有anskeys结果出现，结果为
'''
anskeys=[186],index is 0,and at this time the len is 7
anskeys=[31],index is 1,and at this time the len is 7
anskeys=[145],index is 2,and at this time the len is 7
anskeys=[178],index is 3,and at this time the len is 7
anskeys=[83],index is 4,and at this time the len is 7
anskeys=[205],index is 5,and at this time the len is 7
anskeys=[62],index is 6,and at this time the len is 7
'''
key = [186,31,145,178,83,205,62]
origin = ''
for i in range(0,len(cipherlist)):
    origin = origin + chr(cipherlist[i] ^ key[i%7])
print(origin)