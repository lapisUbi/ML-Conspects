import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Hours_Studied": [1, 2, 3, 4, 5],
    "Exam_Score": [50, 55, 65, 70, 80]
}

df = pd.DataFrame(data)
imgName = 'my_plot.png'

plt.scatter(df["Hours_Studied"], df["Exam_Score"],color='blue')
plt.title("Studied Hours vs Exam Score") # Title
plt.xlabel("Hours")                      # X
plt.ylabel("Exam Score")                 # Y
plt.grid(True)
plt.savefig(imgName)
print("Graph is saved as " + imgName)