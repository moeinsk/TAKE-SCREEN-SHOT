import pyautogui
import tkinter  as tk 

windo =tk.Tk()

def callback():
     shot_btn = pyautogui.screenshot('screen.png')


shot_btn = tk.Button(windo,text="TAKE SCREEN SHOT",command = callable)


shot_btn.place(x=40,y=40)

windo.mainloop()
print(shot_btn)
print(windo)
callback()