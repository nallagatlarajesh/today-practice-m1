import matplotlib.pyplot as plt

student_name=["rajesh","ramu","rani","raki","ramesh","sonu","rand"]
student_marks=[35,50,20,45,40,25,40]
percentage=[35*100/50, 50 *100/50, 20*100/50, 45*100/50, 40*100/50, 25*100/50, 40*100/50]
def line_chart_of_students_and_marks():
    plt.plot(student_name, student_marks)
    plt.title("student marks graph")
    
    plt.xlabel("student names")
    plt.ylabel("student marks")
    
    plt.xlim(xmin=0,xmax =7)
    plt.ylim(ymin=1, ymax =50)
    
    #now it is for swoing grid
    plt.grid(True)
    plt.show()
    
#now call the function 
line_chart_of_students_and_marks()

    
