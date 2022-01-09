
import base64
import binascii

cipherbase64 = b'HUIfTQsPAh9PE048GmllH0kcDk4TAQsHThsBFkU2AB4BSWQgVB0\dQzNTTmVS\
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'
cipher = base64.b64decode(cipherbase64)
cipher64 = binascii.b2a_hex(base64.b64decode(cipherbase64))
cipherlist = []
for i in range(0,len(cipher64),2):
    cipherlist.append(int(cipher64[i:i+2],16))
#print(cipherlist)
#cipherlist是一个list，里面每项为字符ASCII的int值
dict1 = {}
def HammingDistance(list1,list2):
    string = ''
    for i in range(0,len(list1)):
        a = bin(list1[i]^list2[i])
        string+=a[2:]
    return string.count('1')

def hamdistenceaverage(mlist):
  count = 0
  for j in mlist:
      for k in mlist:
        if j != k:
          count += HammingDistance(j,k) / i
  return count
  

for i in range(2,41):
    firstm = cipherlist[0:i]
    secondm = cipherlist[i:2*i]
    thirdm = cipherlist[2*i:3*i]
    fouthm = cipherlist[3*i:4*i]
    mlist = [firstm,secondm,thirdm,fouthm]
    count = hamdistenceaverage(mlist)
    dict1[f'{i}'] = count
#此部分用于找KEYSIZE

print(dict1)
list1= sorted(dict1.items(),key=lambda x:x[1])
print(list1)

OptionalKEYSIZE = [29,5,2,24]
'''
[('29', 32.96551724137932), ('5', 34.8), ('2', 36.0), ('24', 36.25), ('7', 36.85714285714286), ('6', 37.0), ('19', 37.1578947368421), ('20', 37.2), 
('3', 37.333333333333336), ('8', 37.5), ('28', 37.85714285714286), ('30', 38.13333333333333), ('34', 38.1764705882353), ('9', 38.22222222222222), ('39', 38.35897435897436), ('10', 38.4), ('17', 38.47058823529411), ('16', 38.5), ('40', 38.6), ('18', 39.0), ('26', 39.0), ('37', 39.027027027027025), ('32', 39.125), ('23', 39.130434782608695), ('38', 39.21052631578947), ('15', 39.33333333333333), ('33', 39.45454545454546), ('21', 39.61904761904762), ('35', 39.65714285714286), ('31', 39.74193548387096), ('25', 39.76), ('13', 39.84615384615385), ('4', 40.0), ('14', 40.142857142857146), ('27', 40.148148148148145), ('22', 40.54545454545455), ('36', 40.611111111111114), ('11', 41.09090909090909), ('12', 41.5)]
'''

def singlekey_xor(cipher):
    '''get the most probable key byte
    cipher: encrypted by the same byte of key(bytes)
    return: the byte of key(bytes)'''
    result = -1
    for i in range(256):
        tempmsg = bytes([i ^ x for x in cipher])
        #tempresult = score(tempmsg.decode('latin1'))
        tempresult = ChiSquared(tempmsg.decode('latin1') , 1)
        if tempresult > result:#比较如果score更大则几率更大
            result = tempresult
            key = bytes([i])
    return key
def break_key_reuse_xor(msg):#显示所有可用的keysize对应密文，词典形式排序
    '''msg: bytes
    return a dic {keysize : key},keysize is int, key is bytes'''
    key_size = OptionalKEYSIZE
    key = []
    for i in key_size:
        tempkey = b''
        for j in range(i):
            tempkey += singlekey_xor(msg[j::i])
        key.append(tempkey)
    return key
  
def ChiSquared(msg , mod):#重要！使用这个函数进行score排序，不然返回的将是一大堆列表，都可以
    '''Chi-squared Statistic
    msg: str
    mod: 1 is simply plus, 0 is multiple'''
    standard_letter_frequency = {  # From https://en.wikipedia.org/wiki/Letter_frequency.
    'e': 0.12702,'t': 0.09056,'a': 0.08167,'o': 0.07507,'i': 0.06966,'n': 0.06749,
    's': 0.06327,'h': 0.06094,'r': 0.05987,'d': 0.04253,'l': 0.04025,'c': 0.02782,
    'u': 0.02758,'m': 0.02406,'w': 0.02360,'f': 0.02228,'g': 0.02015,'y': 0.01974,
    'p': 0.01929,'b': 0.01492,'v': 0.00978,'k': 0.00772,'j': 0.00153,'x': 0.00150,
    'q': 0.00095,'z': 0.00074,' ': 0.25000}
    score = 0
    msg = msg.lower()
    if mod:
        for i in msg:
            if i in standard_letter_frequency:
                score += standard_letter_frequency[i]
    else:
        msg = msg.lower()
        for i in standard_letter_frequency:
            temp = standard_letter_frequency[i] * len(msg)
            score += (msg.count(i)- temp)**2 / temp
    return score

#均以bytes类型，防止串类型做不出来
XOR = lambda s1 , s2 : bytes([x1 ^ x2 for x1 , x2 in zip(s1 , s2)])
key = break_key_reuse_xor(cipher)
print(key)#可以看出key[0]有意义其余无意义
key = key[0]*len(cipher)
print(XOR(key , cipher))