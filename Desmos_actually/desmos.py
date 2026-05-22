import PIL
from PIL import Image
import keyboard
import time

image=Image.open('arizona.png').convert('RGB')
image=image.transpose(Image.FLIP_TOP_BOTTOM)

w,h=image.size

count=0

target_count=2000

fullString=""
startPoint=0

sameP=-1
x_same=1

for x in range(w):
    startPoint=0
    for y in range(h):
        
        if keyboard.is_pressed('esc'):
            quit()
            break
            
        r,g,b=image.getpixel((x,y))[:3]
        hexC=f'#{r:02x}{g:02x}{b:02x}'
        
        try:
            rN,gN,bN=image.getpixel((x,y+1))[:3]
        except IndexError:
            rN,gN,bN=(-1,-1,-1)
        
        if (r,g,b)==(rN,gN,bN):
            sameP+=1
        else:
            myS="Calc.setExpression({"
            myS+=f" id: '{x,y}', latex: '{x}<x<{x+1} "
            myS+=r'\\{'
            myS+=f"{startPoint}<y<{y}"
            myS+=r"\\}',"
            myS+=f" color:'{hexC.upper()}'"
            myS+="});"
            sameP=1
            print(x,y)
            fullString+=myS
            count += 1
            startPoint=y
            if count==target_count:
                with open(f'{target_count}.txt','w') as fi:
                    fi.write(fullString)
                    fullString=''
                    target_count+=2000

        
with open('command.txt', 'w') as file:
    file.write(fullString)
        
print('done')
print(f'there are {count} expressions')