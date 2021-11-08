def rot(num):
    for anladım in range (len(num)):
        if num [anladım] == '6':
            num = num[:anladım] + '9' + num [anladım + 1:]
            break
    return num

num=input().split('=')[1]
print (rot(num))

