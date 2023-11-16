# 2023-11-06-tkcolorByDict.py

import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd 

df1=pd.read_excel(r"tk-colours.xlsx") # Path of the file.
Color_Name = list(df1['Color Name'])
Color_RGB = list(df1['rgb'])
color_dict = dict(zip(Color_Name,Color_RGB))

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
        label = ttk.Label(master=window,
                          text=key,
                          background=key,
                          width=16,
                          font=("Arial", 12))
        row = n // 12
        column = n % 12
        label.grid(row=row, column=column)
    except:
        break  # 處理最後一列不足的部分

# run
window.mainloop()
