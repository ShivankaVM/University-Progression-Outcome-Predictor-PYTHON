# University Progression Outcome Predictor

This is a Python program designed to predict students' progression outcomes at the end of each academic year based on university regulations.

---

## **Progression Outcomes**
The program determines the student's academic progression based on the number of credits in three categories:
- **Pass**
- **Defer**
- **Fail**

### **Possible Outcomes:**
1. **Progress**: The student advances to the next academic year.
2. **Progress (Module Trailer)**: The student progresses with minor trailing modules.
3. **Module Retriever**: The student must retake some modules.
4. **Exclude**: The student is removed from the course due to excessive failures.

---

## **Program Structure**
### **Part 1 - Main Version & Part 2 - List (Part1 & Part2.py)**

### **A. Outcomes**
- The program prompts the user for pass, defer, and fail credits.
- It then calculates and displays the appropriate progression outcome.

### **B. Validation**
The program ensures:
- **Valid Data Type:** Displays 'Integer required' if input is incorrect.
- **Correct Credit Range:** Accepts only values from {0, 20, 40, 60, 80, 100, 120}.
- **Total Validation:** Ensures that total credits always sum to **120**.
- **Efficient Conditionals:** Uses a structured approach instead of excessive conditions.

#### **Example User Interaction:**
```
Please enter your credits at pass: p
Integer required
Please enter your credits at pass: 140
Out of range.
Please enter your credits at pass: 100
Please enter your credit at defer: 40
Please enter your credit at fail: 20
Total incorrect.
Please enter your credits at pass: 100
Please enter your credit at defer: 20
Please enter your credit at fail: 0
Progress (module trailer)
```

---

## **Part 2 - Multiple Outcomes & Histogram Generation**
### **C. Handling Multiple Outcomes**
- The program loops to allow processing multiple students.
- Users can enter multiple records until they choose to quit ('q').

#### **Example Interaction:**
```
Enter your total PASS credits: 120
Enter your total DEFER credits: 0
Enter your total FAIL credits: 0
Progress
Would you like to enter another set of data? (y/q): y
Enter your total PASS credits: 100
Enter your total DEFER credits: 0
Enter your total FAIL credits: 20
Progress (module trailer)
```

### **D. Histogram Generation**
- When 'q' is entered, the program generates a **histogram** using `graphics.py`.
- The histogram visually represents students in each outcome category.

#### **Example Histogram Output:**
![image](https://github.com/user-attachments/assets/d2bd4c1d-d89b-405b-8659-29639ec6ba8e)

---

## **Part 3 - Text File Storage (Part3.py)**
- The program stores input data into a **text file**.
- On exit, it reads the stored data and prints the progression history.

#### **Example Stored Data:**
```
Part 3:
Progress - 120, 0, 0
Progress (module trailer) - 100, 0, 20
Module retriever - 80, 20, 20
Module retriever - 60, 0, 60
Exclude – 40, 0, 80
```

---

## **Installation & Usage**
### **Requirements:**
- Python 3.x
- `graphics.py` module for histogram visualization

### **To Run the Program:**
1. Clone this repository.
2. Navigate to the project directory.
3. Run `python Part1.py` to start the main version.
4. Run `python Part3.py` to load progression history.

---

## **Contributors**
- Shivanka Maddumarachchi - Developer

---

## **License**
This project is for educational purposes and follows university coursework guidelines.



