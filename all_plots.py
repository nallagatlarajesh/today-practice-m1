import matplotlib.pyplot as plt

student_name = ["rajesh", "ramu", "rani", "raki", "ramesh", "sonu", "rand"]
student_marks = [35, 50, 20, 45, 40, 25, 40]
percentage = [35 * 100 / 50, 50 * 100 / 50, 20 * 100 / 50, 45 * 100 / 50, 40 * 100 / 50, 25 * 100 / 50, 40 * 100 / 50]

def line_chart_of_students_and_marks():
    plt.figure(figsize=(8, 6))
    plt.plot(student_name, student_marks, marker='o', color='b', linestyle='-')
    plt.title("Student Marks Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Student Marks")
    plt.grid(True)
    plt.show()

def bar_chart_of_students_and_their_percentage():
    plt.figure(figsize=(8, 6))
    plt.bar(student_name, percentage, color='g')
    plt.title("Students Percentage")
    plt.xlabel("Student Names")
    plt.ylabel("Student Percentage Marks")
    plt.grid(True)
    plt.show()

def scatter_plot_of_students_and_marks():
    plt.figure(figsize=(8, 6))
    plt.scatter(student_marks, percentage, color='r', marker='o')
    plt.title("Scatter Plot of Student Marks vs Percentage")
    plt.xlabel("Student Marks")
    plt.ylabel("Student Percentage Marks")
    plt.grid(True)
    plt.show()

def histogram_of_student_marks():
    plt.figure(figsize=(8, 6))
    plt.hist(student_marks, bins=5, color='purple', edgecolor='black', alpha=0.7)
    plt.title("Histogram of Student Marks")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

def pie_chart_of_students():
    plt.figure(figsize=(8, 6))
    plt.pie(student_marks, labels=student_name, autopct='%1.1f%%', startangle=140)
    plt.title("Pie Chart of Student Marks")
    plt.axis('equal')
    plt.show()

# Call all the functions
line_chart_of_students_and_marks()
bar_chart_of_students_and_their_percentage()
scatter_plot_of_students_and_marks()
histogram_of_student_marks()
pie_chart_of_students()
