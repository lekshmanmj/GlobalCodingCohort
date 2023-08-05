# solution
import string
uc = string.ascii_uppercase
lc = string.ascii_lowercase
temp = [each_uc + each_lc for each_uc, each_lc in zip(uc,lc)]
all = ' ' + ''.join(temp)

def find_length(strs):
    length = 0
    while True:
        try:
            strs[length]
            length += 1
        except: break
    return length
def compare(prev,curr):
    for each_p, each_c in zip(prev,curr):
        if each_p > each_c:
            return True
        elif each_p < each_c: 
            return False
    # return False
def invert(list_str_converted):
    sorted_words = []
    for each_num_word in list_str_converted:
        temp = []
        for each_num in each_num_word:
            temp.append(all[each_num])
        sorted_words.append(''.join(temp))
    return sorted_words
def convert(list_str):
    list_str_converted = []
    for each_word in list_str:
        temp = []
        for each_letter in each_word:
            temp.append(all.index(each_letter))
        list_str_converted.append(temp)
    return list_str_converted

def find_moves(list_str):
    first_round = False
    count = 0
    i = 1
    input_length = find_length(list_str)
    list_str_converted = convert(list_str)
    # print(invert(list_str_converted))
    while i < input_length:
        prev = list_str_converted[i-1]
        curr = list_str_converted[i]
        move = compare(prev,curr)
        # print('I',i-1,invert([prev,curr]),prev,curr,move)
        j = None # comment it if you've commented print statements
        if move:
            count += 1
            j = i - 2
            while move and j >= 0:
                prev = list_str_converted[j]
                move = compare(prev,curr)
                # print('J',j,invert([prev,curr]),prev,curr,move)
                j -= 1
            list_str_converted.insert(j+1,curr)
            del list_str_converted[i+1]
        # print(i,j,invert(list_str_converted))
        # print()
        i += 1
        # print('EACH',each_round_count,i,input_length)
    # print(invert(list_str_converted))
    return count

t = int(input())
file = open('output.txt','w+')
for a in range(t):
    s = int(input())
    temp = []
    for b in range(s):
        temp.append(input())
    out = ''.join(["Case #",str(a+1),': ',str(find_moves(list_str = temp)),'\n'])
    file.write(out)
file.close()