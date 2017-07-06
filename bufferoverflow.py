#!/usr/bin/python
import string, sys, re

def help():
    print sys.argv[0], '<length>            - max lenght: 20280'
    print sys.argv[0], 'TARGET:<HEX>        - example: TARGET:32714131\n' 
    sys.exit()

try: 
    arg = sys.argv[1].upper()
except:
    help()

# Generate injeciton pattern
low = list(string.ascii_lowercase)
high = list(string.ascii_uppercase)
num = range(0, 10)
bufmax = ''
for h in high:
    for l in low:
        for n in num:
            bufmax += h+l+str(n)

# decode target hex pattern and find target overflow pointer
if 'TARGET:' in arg:
    target = re.sub('TARGET:','', arg).decode('hex')
    if bufmax.find(target) != -1:
        buf = bufmax.find(target)
        print "Big-Endian detected"
        print "Overflow:         'A' * %i + 'BBBB'\n" % buf
    if bufmax.find(target[::-1]) != -1:
        buf = bufmax.find(target[::-1])
        print "Little-Endian detected (reversed bytes)"
        print "Overflow:         'A' * %i + '\\xBB\\xBB\\xBB\\xBB'\n" % buf

    else:
        print "Pattern not found."
elif int(arg) > 20280:
    help()

else:
    print bufmax[:int(arg)]+'\n'
