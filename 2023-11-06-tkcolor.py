# 2023-11-08-1.py

import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

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
    return round(h,4), round(s,4), round(v,4)

df1=pd.read_excel(r"tk-colours.xlsx") # Path of the file.

df1['紅']=0
df1['綠']=0
df1['藍']=0
for n in range(df1.shape[0]) :
    str1 = df1.loc[n,'rgb'][3:]
    df1.loc[n,'紅'] = int(str1.strip('()').split(',')[0])
    df1.loc[n,'綠'] = int(str1.strip('()').split(',')[1])
    df1.loc[n,'藍'] = int(str1.strip('()').split(',')[2])

df1['H']=0.0
df1['S']=0.0
df1['V']=0.0
for n in range(df1.shape[0]) :
    t1 = rgb2hsv( df1.loc[n,'紅'],df1.loc[n,'綠'],df1.loc[n,'藍'] )
    df1.loc[n,'H'] = t1[0]
    df1.loc[n,'S'] = t1[1]
    df1.loc[n,'V'] = t1[2]

#print(df1.info())

# ans = (df1['紅']>240) & (df1['藍']>240)   #  邏輯索引測試
# print(type(ans)) # <class 'pandas.core.series.Series'>
# df1 = df1[ans].reset_index(drop=True).loc[:,['rgb']]
# print(df1.values.tolist())

# df1 = df1.loc[ (5 < df1.index) & ( df1.index < 20 ) , : ]   #  邏輯索引測試
# print(df1.values.tolist())

# df1 = df1.loc[ (5 < df1.index) & ( df1.index < 20 ) , : ]   #  邏輯索引測試
# df1 = df1[ df1['Color Name'].str.get(0)=='a'].loc[:,['Color Name']]
# print(df1.values.tolist())

# setup
window = tk.Tk()
window.title('color list')
window.geometry('1800x950')

unknown_color = []
for item in df1['Color Name'] :
    try:
         label = ttk.Label(master=window,background=item)
    except :
         print(item)
         unknown_color.append(item)

df1 = df1[  ~df1['Color Name'].isin(unknown_color)  ].reset_index(drop=True)
df1 = df1.sort_values(by=['H', 'V'], ascending=[True, True]).reset_index(drop=True)

# print(df1)

# df1.shape[0]   表格列數
# df1.shape[1]   表格行數

rows = df1.shape[0] // 12 + 1
print(rows)  # 43 列

for m in range(rows):
    for n in range(12):
        try :
            if  df1.loc[n+12*m,'V'] < 0.2 or df1.loc[n+12*m,'H'] == 240  :
                c = 'white'
            else :
                c = 'black'

            label = ttk.Label(master = window,
                                text = df1.loc[n+12*m,'Color Name'],
                                background=df1.loc[n+12*m,'Color Name'],
                                foreground=c,
                                width=16,
                                font=("Arial", 12))
            label.grid(row=m, column=n)
        except :
            break  #  處理最後一列不足的部分

#run
window.mainloop()