import matplotlib.pyplot as plt

student_name = ["rajesh", "ramu", "rani", "raki", "ramesh", "sonu", "rand"]
student_marks = [35, 50, 20, 45, 40, 25, 40]
percentage = [35 * 100 / 50, 50 * 100 / 50, 20 * 100 / 50, 45 * 100 / 50, 40 * 100 / 50, 25 * 100 / 50, 40 * 100 / 50]

def line_chart_of_students_and_marks():
    plt.plot(student_name, student_marks)
    plt.title("Student Marks Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Student Marks")
    
    # Setting tick labels
    plt.xticks(range(len(student_name)), student_name)
    
    plt.xlim(xmin=0, xmax=6)
    plt.ylim(ymin=1, ymax=50)
    
    # Showing grid
    plt.grid(True)
    plt.show()


    
def bar_chart_of_students_and_their_percentage():
    left_edges= student_name
    height = percentage
    plt.bar(left_edges,height)
    plt.title("students perchentage")
    plt.xlabel("student Names")
    plt.ylabel("student percentage marks")
    plt.show()

def pie_chart_of_students():
    plt.figure(figsize=(8,6))
    plt.pie(student_marks,labels=student_name,autopct="%1.1f%%", startangle=140)
    plt.title("pie chart of students marks")  #add title  
    plt.axis("equal")
    plt.show()
    
    

# Call the function
line_chart_of_students_and_marks()
bar_chart_of_students_and_their_percentage()
pie_chart_of_students()

