# I declare that my workcontains no examples of misconducts, such as plagiarism, or collusion
# Any code taken from other sources is referenced within my code solution.
# UOW Number – w2051745
# IIT student Number - 20230684
# Date:10/12/2023

from graphics import *

progress = 0
trailer = 0
retrieve = 0
exclude = 0
out = []
out_to_list = ""

loop = 'y'

def student_or_staff(): #this function will allow user to select the user type
    print("Select whether you are a student or staff memeber")
    print("1. Student")
    print("2. Staff")
    try:
        stud_or_staff = int(input("Enter the number of selected category: "))
        if(stud_or_staff == 1):
            return True
        elif(stud_or_staff == 2):
            return False
        else:
            print("Please select the correct number!")
            student_or_staff()
    except ValueError:
        print("Type the number for selected option please.")
        student_or_staff()


def collect_data(): # this function will allow user to enter data and check the data type
    global pass_credit, defer_credit, fail_credit
    try:
        pass_credit = int(input("Enter your total pass credits: "))
        if(range_check(pass_credit)):
            print("Out of range")
            collect_data()

        defer_credit = int(input("Enter your total defer credits: "))
        if(range_check(defer_credit)):
            print("Out of range")
            collect_data()

        fail_credit = int(input("Enter your total fail credits: "))
        if(range_check(fail_credit)):
            print("Out of range")
            collect_data()
        
        if(total_check(pass_credit, defer_credit, fail_credit)):
            collect_data()
    except ValueError:
        print("Integer Required")
        collect_data()

def total_check(pass_cred,defer_cred,fail_cred): # this function will allow user to check the total of credits
    if pass_cred + defer_cred + fail_cred != 120:
        print('Total Incorrect')
        return True

def range_check(num): #this function check the entered values in one from the list given below
    range = [0,20,40,60,80,100,120]
    if(num not in range):
        return True

def main_logic(x,y): 
    global progress,trailer,retrieve,exclude,out_to_list
    if x == 120:
        print('Progress')
        progress += 1
        out_to_list = "Progress"
    elif x == 100:
        print('Progress (Module Trailer)')
        trailer += 1
        out_to_list = "Progress (Module Trailer)"
    elif x == 40 and y == 0:
        print('Exclude')
        exclude += 1
        out_to_list= "Exclude"
    elif x == 80 or x == 60 or x == 40:
        print('Module Retriever')
        retrieve += 1
        out_to_list = "Module Retriever"
    elif x == 20 and y == 0 or y == 20:
        print('Exclude')
        exclude += 1
        out_to_list = "Exclude"
    elif x == 20:
        print('Module Retriever')
        retrieve += 1
        out_to_list = "Module Retriever"
    elif y == 60:
        print('Module Retriever')
        retrieve += 1
        out_to_list = "Module Retriever"
    elif x == 0 and y == 0 or 20 or 40:
        print('Exclude')
        exclude += 1
        out_to_list = "Exclude"
    else:
        print('Module Retriever')
        retrieve +=1
        out_to_list = "Module Retriever"

def create_list(out_txt, pass_c, defer_c, fail_c): #this will store data entered by the user to a list
    list1 = [out_txt, pass_c, defer_c,fail_c]
    out.append(list1)

def print_list(list): # this function will print the data inside the given list
    print("Part 2: ")
    for items in list:
        for x, item in enumerate(items):
            if x < 1:
                print(item, end=" - ")
            elif x == len(items) - 1:
                print(item, end=" ")
            else:
                print(item, end=", ")
        print("")

def write_file(data): # this function will write data of the given list to text.txt
    file1 = open("text.txt", "w+")
    for items in data:
        for x, item in enumerate(items):
            if x < 1:
                file1.write(item + " - ")
            elif x == len(items) - 1:
                file1.write(str(item))
            else:
                file1.write(str(item) + ", ")
        file1.write("\n")

def read_file(data): # this function will read the data inside text.txt and will print those data
    file2 = open("text.txt", "r")
    print("Part 3:")
    for items in data:
        for x, item in enumerate(items):
            if x < 1:
                print(item, end=" - ")
            elif x == len(items) - 1:
                print(item, end=" ")
            else:
                print(item, end=", ")
        print("")

if(student_or_staff()):
    # if the selected user is a student, this part will run
    collect_data()
    main_logic(pass_credit, defer_credit)
else:
    # if the selected user is a staff member, the below code will run 
    while(loop == 'y'):
        collect_data()
        main_logic(pass_credit, defer_credit)
        create_list(out_to_list, pass_credit, defer_credit, fail_credit)
        
        print('would you like to enter another set of data?')
        loop = input('Enter "y" for yes and "q" to quit and view results: ')

    if loop == 'q':

        window = GraphWin('Histogram',480,550) # creating the window for the histogram
        progress_rectangle = Rectangle(Point(80, 430-(20*progress)), Point(140, 430)) # creating the rectangle for the histogram
        progress_text_count = Text(Point(110, 420-(20*progress)),progress)
        progress_text = Text(Point(110, 440), "Progress").draw(window)
        progress_rectangle.setFill(color_rgb(50, 168, 74))
        progress_rectangle.draw(window)
        progress_text_count.draw(window)

        trailer_rectangle = Rectangle(Point(160, 430-(20*trailer)), Point(220, 430))
        trailer_text_count = Text(Point(190, 420-(20*trailer)), trailer)
        trailer_text = Text(Point(190, 440), "Trailer").draw(window)
        trailer_rectangle.setFill(color_rgb(42, 156, 222))
        trailer_rectangle.draw(window)
        trailer_text_count.draw(window)

        retrieve_rectangle = Rectangle(Point(240, 430-(20*retrieve)), Point(300, 430))
        retrieve_text_count = Text(Point(270, 420-(20*retrieve)), retrieve)
        retrieve_text = Text(Point(270, 440), "Retreive").draw(window)
        retrieve_rectangle.setFill(color_rgb(222, 120, 42))
        retrieve_rectangle.draw(window)
        retrieve_text_count.draw(window)

        exclude_rectangle = Rectangle(Point(320, 430-(20*exclude)), Point(380, 430))
        exclude_text_count = Text(Point(350, 420-(20*exclude)), exclude)
        exclude_text = Text(Point(350, 440), "Exclude").draw(window)
        exclude_rectangle.setFill(color_rgb(222, 42, 90))
        exclude_rectangle.draw(window)
        exclude_text_count.draw(window)

        histogram_txt = Text(Point(150,39),"Histogram Results")
        histogram_txt.setStyle('bold')
        histogram_txt.draw(window)
        line = Line(Point(60, 431), Point(400, 431)).draw(window)

        total_outcomes = progress+trailer+retrieve+exclude
        outcomes_txt = Text(Point(150, 470), (str(total_outcomes) + ' Outcomes in total'))
        outcomes_txt.draw(window)

        window.getMouse()
        window.close()

        print_list(out)
        write_file(out)
        read_file(out)
    else: 
        print("Enter the valid letter")

