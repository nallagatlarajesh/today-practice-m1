import matplotlib.pyplot as plt

students=["rajesh","ram","ranveer","rajin"]
marks=[40,50,60,20]
def scatter():
    plt.scatter(students,marks)
    plt.title("student marks of the scatter graph")
    plt.xlabel("students")
    plt.ylabel("marks")
    plt.grid(True)
    #plt.show()
    
#function calling
scatter()
