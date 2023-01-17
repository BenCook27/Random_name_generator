from tkinter import *
import tkinter as tk
from tkinter import ttk
import csv
import random
import time

past_selected_students = ['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5']
selection_list = []

def file_name():
    if (var_9a.get() == 1) & (var_9b.get() == 0):
        return 'ClassA.csv'
    elif (var_9a.get() == 0) & (var_9b.get() == 1):
        return 'ClassB.csv'
    elif (var_9a.get() == 1) & (var_9b.get() == 1):
        return 'Both classes selected'
    else:
        return 'Class not selected'


def name():
    file = file_name()
    count = 0
    if file == 'Class not selected':
        random_name_var.set('No class has been selected')
    elif file == 'Both classes selected':
        with open('ClassA.csv', newline='') as f:
            reader = csv.reader(f)
            classA = list(reader)
        with open('ClassB.csv', newline='') as f:
            reader = csv.reader(f)
            classB = list(reader)
        both_classes = classA + classB
        selected_row = random.choice(both_classes)
        print(selected_row)
        random_name_var.set(selected_row)
        root.update()
    elif file == 'ClassA.csv' or 'ClassB.csv':
        while True:
            count = count + 1
            with open(f'{file}') as f:
                reader = csv.reader(f)
                selected_row = random.choice(list(reader))
                #print(selected_row)
                random_name_var.set(selected_row)
                root.update()
                if count < 10:
                    time.sleep(.1)
                elif count < 17:
                    time.sleep(.3)
                elif count < 20:
                    time.sleep(.6)
                else:
                    break
    student_selected()
    
def student_selected():
    file = file_name()
    with open(f'{file}') as f:
        reader = csv.reader(f)
        data = list(reader)
        print(data)
        print('##################')
        selected_student = random.choice(data)
        if selected_student not in past_selected_students:
            print(selected_student)
            random_name_var.set(selected_student)
            past_selected_students.append(selected_student)
            past_selected_students.pop(0)
            print(past_selected_students)
            root.update()

        else:
            student_selected()
        

    
       # print('##################')
    '''
    for selected_student in reader:
        
        reader.remove(selected_student)
        past_selected_students.pop(0)
        
        
        print(past_selected_students)
        root.update()
            '''
       


root = tk.Tk()
root.title("Random Name Generator")
root.geometry('500x400')
random_name_var = StringVar()
var_9a = IntVar()
var_9b = IntVar()

generate_name_button = ttk.Button(root, text="Generate Name", command=name)
generate_name_button.pack(side='top', fill='both', expand=True)

name_field = ttk.Label(root, relief="solid", textvariable=random_name_var, anchor="center", font="times 22 bold")
name_field.pack(side='top', fill='both', expand=True)

checkbox_9a = tk.Checkbutton(root, text='9A', variable=var_9a, onvalue=1, offvalue=0, command=file_name)
checkbox_9a.pack()

checkbox_9b = tk.Checkbutton(root, text='9B', variable=var_9b, onvalue=1, offvalue=0, command=file_name)
checkbox_9b.pack()

countdown = Label(root, text="")
countdown.pack(pady=20)
#countdown.after(2000, timer)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="bottom", fill='both', expand=True)

root.mainloop()
