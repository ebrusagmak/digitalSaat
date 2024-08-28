import tkinter 
import time
import locale
locale.setlocale(locale.LC_ALL,"Turkish")


window=tkinter.Tk()
window.title("DİJİTAL SAAT UYGULAMASI")
window.configure(bg="black")
window.geometry("300x200")
window.resizable(0,0)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)


label3=tkinter.Label(window,background="black",foreground="white",font="arial,50'bold'")
label3.grid(row=0,column=1,padx=20,pady=10)
label4=tkinter.Label(window,background="black",foreground="white",font="arial,50'bold'")
label4.grid(row=1,column=1,padx=20,pady=10)
label=tkinter.Label(window,background="black",foreground="white",font="arial,50'bold'")
label.grid(row=2,column=1,padx=20,pady=10)
label2=tkinter.Label(window,background="black",foreground="white",font="arial,50'bold'")
label2.grid(row=3,column=1,padx=20,pady=10)




def digital_saat():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    time_live1=time.strftime("%Y:%m:%d")
    label2.config(text=time_live1)
    time_live2=time.strftime("%B")
    label3.config(text=time_live2)
    time_live3=time.strftime("%A")
    label4.config(text=time_live3)
    label.after(1000,digital_saat)
   
digital_saat()
window.mainloop()
