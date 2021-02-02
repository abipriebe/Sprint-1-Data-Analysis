#Install the necessary libraries
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

# Load the data set 
students = pd.read_csv('StudentsPerformance.csv')
#print(students)

'''
### QUESTION 1:
# Does gender play a role in student performance? 
# Is it consistent across all subjects?
'''

# Create a new variable (average_score) that combines 
# a student's math, reading, and writing scores into one 
# that averages them all together. 
students["average_score"] = (students["math_score"] + students["reading_score"] + students["writing_score"])/3
#print(students)

# Create a boxplot that shows the distribution of 
# average_score grouped by gender
sns.boxplot(x="gender", y="average_score", data=students, orient="v")
plt.show()

# Create a boxplot that shows the distribution of 
# math_score grouped by gender
sns.boxplot(x="gender", y="math_score", data=students, orient="v")
plt.show()

# Create a boxplot that shows the distribution of 
# reading_score grouped by gender
sns.boxplot(x="gender", y="reading_score", data=students, orient="v")
plt.show()

# Create a boxplot that shows the distribution of 
# writing_score grouped by gender
sns.boxplot(x="gender", y="writing_score", data=students, orient="v")
plt.show()


'''
### QUESTION 2:
# Is there a significant relationship between a student's 
# math and english scores?
'''

# Create a new variable (english_score) that combines 
# a student's reading and writing scores into one 
# that averages them together. 
students["english_score"] = (students["reading_score"] + students["writing_score"])/2
#print(students)

# Create a Linear Regression plot that shows the 
# relationship between math and english scores
students = students.reset_index()
sns.regplot(data=students, x="math_score", y="english_score")
plt.show()


'''
### QUESTION 3:
# Does a student's parent's education level have 
# any effect on whether or not a student completed 
# the test preparation course? Was there a 
# difference in scores between the students who 
# completed the course and the students who did?
'''

# How many students with parents who have master's
# degrees completed the test prep course?
students_master = students[students.parental_education == "master's degree"]
print(students_master.set_index(["parental_education", "test_preparation_course"]).count(level="test_preparation_course"))
# 20 out of 59 students = 34%

# How many students with parents with bachelors 
# degrees completed the test prep course?
students_bach = students[students.parental_education == "bachelor's degree"]
print(students_bach.set_index(["parental_education", "test_preparation_course"]).count(level="test_preparation_course"))
# 46 out of 118 students = 39%

# How many students with parents who have associate's
# degrees completed the test prep course?
students_asso = students[students.parental_education == "associate's degree"]
print(students_asso.set_index(["parental_education", "test_preparation_course"]).count(level="test_preparation_course"))
# 82 out of 222 students = 37%

# How many students with parents who have some 
# college experience completed the test prep course?
students_college = students[students.parental_education == "some college"]
print(students_college.set_index(["parental_education", "test_preparation_course"]).count(level="test_preparation_course"))
# 77 out of 226 students = 34%

# How many students with parents who graduated 
# high school completed the test prep course?
students_hs = students[students.parental_education == "high school"]
print(students_hs.set_index(["parental_education", "test_preparation_course"]).count(level="test_preparation_course"))
# 56 out of 196 students = 29%

# How many students with parents who have some 
# high school experience completed the test prep course?
students_high = students[students.parental_education == "some high school"]
print(students_high.set_index(["parental_education", "test_preparation_course"]).count(level="test_preparation_course"))
# 77 out of 179 students = 43%

# Create a bar plot showing the difference of average 
# scores between those who took the prep course and those 
# who did not, grouped by parental education level. 
sns.barplot(x="parental_education", y="average_score", data=students, hue="test_preparation_course")
plt.show()