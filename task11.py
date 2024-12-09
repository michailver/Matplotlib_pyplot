# Užduotis 6: Palyginkite dviejų studentų klasių rezultatus.
# Sukurkite stulpelines diagramas, kurios vaizduoja 10 studentų vienos klasės suminius rezultatus penkiose skirtingose pamokose.
# Naudokite linijines diagramas, kad parodytumėte ryšį tarp studijų valandų ir rezultatų (galite extrapoliuoti įverčius gražesniam atvaizdavimui)
import matplotlib.pyplot as plt
import numpy as np

subjects = ['Math', 'Science', 'History', 'Art', 'PE']
school = [
    [
        [65, 97, 58, 72, 58],  # pirmos klasės suminiai balai
        [5, 20, 7, 16, 18]  # ruošimosi valandos
    ],
    [
        [85, 90, 78, 92, 88],  # pirmos klasės suminiai balai
        [10, 15, 12, 18, 20]  # ruošimosi valandos
    ]
]
bar_width = 0.4
x = np.arange(len(subjects))

fig, ax1 = plt.subplots(figsize=(10, 6))
class1_marks = ax1.bar(x - bar_width / 2, school[0][0], bar_width, color='skyblue', label='class1 scores')
class2_marks = ax1.bar(x + bar_width / 2, school[1][0], bar_width, color='gray', label='class2 scores')
hours_leg1 = ax1.plot(0, 0, color='blue', marker='o', label='Class1 Hours', linewidth=2)
hours_leg2 = ax1.plot(0, 0, color='cyan', marker='o', label='Class2 Hours', linewidth=2)
ax1.set_xticks(x)
ax1.set_xticklabels(subjects)
ax1.set_title('Class Results and Study Hours by Subject', fontsize=20)
ax1.set_ylabel('Marks', fontsize=15)
ax1.set_xlabel('Subjects', fontsize=15)

ax2 = ax1.twinx()
class1_hours = ax2.plot(subjects, school[0][1], color='blue', marker='o', label='Class1 Hours', linewidth=2)
class2_hours = ax2.plot(subjects, school[1][1], color='cyan', marker='o', label='Class2 Hours', linewidth=2)
ax2.set_ylabel('Hours', fontsize=15)

ax1.legend()
# ax2.legend()
plt.show()
