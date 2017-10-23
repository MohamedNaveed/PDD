from Tkinter import *
import re
import sys
import pyqrcode
import pdd
root= Tk()
root.title("Intelligent Qr Code Tag Generator")
root.geometry("700x500")
root.configure(background=None)

#declaring labels
Name_label=Label(root,text="Name ",font=("times new roman", 20))
PassPortNumber_label=Label(root,text="Passport Number",font=("times new roman", 20))
StartingPlace_label=Label(root,text="Starting Place",font=("times new roman", 20))
Destination_label=Label(root,text="Destination",font=("times new roman", 20))
Weight_label=Label(root,text="Weight in kgs",font=("times new roman", 20))

#error
Name_label_error=Label(root,text="*please enter a valid name",font=("times new roman", 10))
PassPortNumber_label_error=Label(root,text="*please enter a valid passport number",font=("times new roman", 10))
StartingPlace_label_error=Label(root,text="*please enter a valid Starting Place",font=("times new roman", 10))
Destination_label_error=Label(root,text="*please enter a valid Destination",font=("times new roman", 10))
Weight_label_error=Label(root,text="*please enter a valid weight",font=("times new roman", 10))
#result
result=Label(root,text="Your QR code is successfully generated. Thank You \n Press Clear",font=("times new roman", 10))


#declaring variables
NameV=StringVar()
PassPortNumberV=StringVar()
StartingPlaceV=StringVar()
DestinationV=StringVar()
WeightV=StringVar()

#declaring entries
Name_entry=Entry(root,textvariable=NameV,font=("times new roman",15))
PassPortNumber_entry=Entry(root,textvariable=PassPortNumberV,font=("times new roman",15))
StartingPlace_entry=Entry(root,textvariable=StartingPlaceV,font=("times new roman",15))
Destination_entry=Entry(root,textvariable=DestinationV,font=("times new roman",15))
Weight_entry=Entry(root,textvariable=WeightV,font=("times new roman",15))

#FUNCTIONS
def StringCheck(s):
    match = re.match("^[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz. ]*$", s)
    if(match is not None and s!=""):
        return True
    return False
def PP(s):
    s1=s[1:len(s)]
    match = re.match("^[0123456789]*$", s1)
    if(len(s)==8 and s!="" and s[0]>='A' and s[0]<'Z' and s[0]!='Q' and s[0]!='X'and match is not None ):
        return True
    return False

def is_int(x):
    try:
        x = int(x)
        return True
    except:
         return False

def Validate(Name,PassPortNumber,StartingPlace,Destination,Weight):
    if(StringCheck(Name)==False):
        Name_entry.delete(0,END)
        Name_label_error.grid(row=0,column=2)
        return False
    else:
        Name_label_error.grid_forget()

    if(PP(PassPortNumber)==False):
        PassPortNumber_entry.delete(0,END)
        PassPortNumber_label_error.grid(row=1,column=2)
        return False
    else:
        PassPortNumber_label_error.grid_forget()

    if(StringCheck(StartingPlace)==False):
        StartingPlace_entry.delete(0,END)
        StartingPlace_label_error.grid(row=2,column=2)
        return False
    else:
        StartingPlace_label_error.grid_forget()

    if(StringCheck(Destination)==False):
        Destination_entry.delete(0,END)
        Destination_label_error.grid(row=3,column=2)
        return False
    else:
        Destination_label_error.grid_forget()

    if(is_int(Weight)==False):
        Weight_entry.delete(0,END)
        Weight_label_error.grid(row=4,column=2)
        return False
    else:
        Weight_label_error.grid_forget()

    return True



def printName():
    Name=NameV.get()
    PassPortNumber=PassPortNumberV.get()
    StartingPlace=StartingPlaceV.get()
    Destination=DestinationV.get()
    Weight=WeightV.get()
    if(Validate(Name,PassPortNumber,StartingPlace,Destination,Weight)):
        print("Name: "+ NameV.get()+" \n"+"PassPortNumber: "+ PassPortNumberV.get()+"\n"+"StartingPlace: "+StartingPlaceV.get()+"\n"+"Destination: "+DestinationV.get()+"\n"+"Weight:"+WeightV.get())
        result.grid(row=7,column=1)
        qr = pyqrcode.create('Name:'+ Name + '\n Passport number:' + PassPortNumber + ' \n Weight:' + Weight + ' \n From:'+ StartingPlace + ' Destination:' + Destination + ' \n Content composition: \n organic % =' + str(pdd.orange_area)+'%' + '\n metal % =' +str(pdd.blue_area)+'%')
        qr.png('QR_tag.png', scale=5)


def clear():
    Name_entry.delete(0,END)
    PassPortNumber_entry.delete(0,END)
    StartingPlace_entry.delete(0,END)
    Destination_entry.delete(0,END)
    Weight_entry.delete(0,END)
    result.grid_forget()
    Name_label_error.grid_forget()
    PassPortNumber_label_error.grid_forget()
    StartingPlace_label_error.grid_forget()
    Destination_label_error.grid_forget()
    Weight_label_error.grid_forget()

#label allignment
Name_label.grid(row=0,column=0,sticky=W)
PassPortNumber_label.grid(row=1,column=0,sticky=W)
StartingPlace_label.grid(row=2,column=0,sticky=W)
Destination_label.grid(row=3,column=0,sticky=W)
Weight_label.grid(row=4,column=0,sticky=W)

#entries allignments
Name_entry.grid(row=0,column=1)
PassPortNumber_entry.grid(row=1,column=1)
StartingPlace_entry.grid(row=2,column=1)
Destination_entry.grid(row=3,column=1)
Weight_entry.grid(row=4,column=1)

#button
button=Button(root, text="Generate QR Code", command=printName,height=1,width=20,font=("times new roman",15,"bold"))
button.grid(row=8,column=1)
button1=Button(root, text="Clear", command=clear,height=1,width=20,font=("times new roman",15,"bold"))
button1.grid(row=9,column=1)


#open(imageFile)

root.mainloop()
