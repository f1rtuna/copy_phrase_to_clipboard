#! python3
# mclip.py - A multi-clipboard program.

TEXT = {'agree': """Whaaaa? really that sounds amazing! Lets do it, me and you make the dream team! """, \
        'busy': """Sorry, but i'm soooo busy maybe we can do some other time""",\
        'beg': """I beg of yuouuuuu pleaseeee help me, I'm desperate"""}


import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]     #first comomand line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)