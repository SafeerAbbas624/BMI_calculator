from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

label1 = Label(text="Enter your height in m: ")
label1.grid(row=1, column=1)
label1.config(padx=10, pady=10)

label2 = Label(text="Enter your weight in kg: ")
label2.grid(row=2, column=1)
label2.config(padx=10, pady=10)

font = ("Arial", 10, "bold")
# Entries
entry1 = Entry(width=10)
entry1.insert(END, string="0")
entry1.grid(row=1, column=2)

# Entries
entry2 = Entry(width=10)
entry2.insert(END, string="0")
entry2.grid(row=2, column=2)


def calculate():
    height = float(entry1.get())
    weight = float(entry2.get())
    bmi = round(weight / height ** 2)
    if bmi <= 18.5:
        label3.config(text=f"Your BMI is {bmi}, you are underweight.", font=font)
    elif bmi <= 25:
        label3.config(text=f"Your BMI is {bmi}, you have a normal weight.", font=font)
    elif bmi <= 30:
        label3.config(text=f"Your BMI is {bmi}, you are slightly overweight.", font=font)
    elif bmi <= 35:
        label3.config(text=f"Your BMI is {bmi}, you are slightly overweight.", font=font)
    else:
        label3.config(text=f"Your BMI is 40, you are clinically obese.", font=font)


label3 = Label(text="Your BMI is 0 ", font=font)
label3.grid(row=4, column=1)
label3.config(padx=10, pady=10)

button = Button(text="Calculate", command=calculate)
button.grid(row=3, column=3)
button.config(padx=10, pady=10)

label4 = Label(text="Feet to Meter Conversion", font=font)
label4.grid(row=5, column=2)
label4.config(padx=10, pady=10)

label5 = Label(text="enter your height in Feet: ")
label5.grid(row=6, column=1)
label5.config(padx=10, pady=10)

entry3 = Entry(width=10)
entry3.insert(END, string="0")
entry3.grid(row=6, column=2)


def calculate_height():
    feet = float(entry3.get())
    meter = round(feet * 0.3048, 2)
    label6.config(text=f"Your Height in meter is: {meter}", font=font)


button1 = Button(text="Calculate", command=calculate_height)
button1.grid(row=6, column=3)
button1.config(padx=10, pady=10)

label6 = Label(text="Your Height in meter is: 0", font=font)
label6.grid(row=7, column=1)
label6.config(padx=10, pady=10)

window.mainloop()
