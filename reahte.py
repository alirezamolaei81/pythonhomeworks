import re
reshte = input() .split()

reshte = "Formatted Text: "+" ".join(reshte)

reshte=re.sub(r"\\n","\n",reshte)

final =""

atCnt=0

for ch in reshte:
    if(ch=="@"):
        atCnt+=1

    if (atCnt>0 and ch=="#") :
        atCnt-=1
    else:
        final+=ch

print(final)