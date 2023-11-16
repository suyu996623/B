# 2023-11-06-tkcolorByDict1.py

import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd 

df1=pd.read_excel(r"tk-colours.xlsx") # Path of the file.
Color_Name = list(df1['Color Name'])
Color_RGB = list(df1['rgb'])
color_dict = dict(zip(Color_Name,Color_RGB))

print(len(color_dict)) # 556
print(color_dict)

def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return round(h,4), round(s,4),round(v,4)

for x in color_dict :
    t1 = tuple(color_dict[x].strip('RGB()').split(','))
    t1 = ( int(t1[0]), int(t1[1]), int(t1[2]) )
    t1 = t1 + rgb2hsv(*t1)
    color_dict[x] = t1      # (240, 248, 255, 208.0, 0.0588, 1.0)

print(len(color_dict)) # 556
print(color_dict)

# setup
window = tk.Tk()
window.title('buttons')
window.geometry('1800x950')

unknown_color = []
for key in color_dict :
    try:
        label = ttk.Label(master=window,background=key)
    except Exception as e:
        str1 = str(e).strip("unknown color name ").strip('"')
        if str1 != 'ist index out of rang':
            unknown_color.append(str1)
print(len(unknown_color)) # 44
print(unknown_color)

for key in unknown_color :
    color_dict.pop(key)
print(len(color_dict)) # 512
print(color_dict)

for n,key in enumerate(color_dict) :

    try:
        if color_dict[key][5] < 0.2  or ( 239 < color_dict[key][3] < 241 and color_dict[key][4] > 0.1) :
            fg = 'white'
        else :
            fg = 'black'
        label = ttk.Label(master=window,
                          text=key,
                          background=key,
                          foreground=fg,
                          width=16,
                          font=("Arial", 12))
        row = n // 12
        column = n % 12
        label.grid(row=row, column=column)
    except:
        break  # 處理最後一列不足的部分

# run
window.mainloop()
