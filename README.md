# Overview

This is an analysis of a data set about [student performance](https://www.kaggle.com/spscientist/students-performance-in-exams). The data set includes their math, reading, and writing scores as well as factors that may or may not play into their performance levels such as gender, parental education level, whether or not the student completed a preparation course, and so on. My goal in this analysis was to decipher which factors had an influence on the students' performance and how great that influence was. 

[Software Demo Video](https://youtu.be/O9yLHxa6cJY)

# Data Analysis Results

1. Does gender play a role in student performance? Is it consistent across all subjects?

I found through my analysis that while there is a slight difference in overall scores and scores for individual subjects, some in favor of females and some in favor of males, there was nothing incredibly convincing that one gender had significnatly out-performed the other in any category.

2. I don't know very many people who are particularly exceptional at both Math and English. People are typically proficient in one or the other. Is there a significant relationship between a student's math and english scores?

The results that I found from analyzing this question did not support my original hypothesis that if you are proficient in one subject, you might be lacking in the other. Instead, the data seemed to show a positive linear correlation between math and english scores, meaning as one score increased the other followed suit. 

3. Does a student's parent's education level have any effect on whether or not a student completed the test preparation course? Was there a difference in scores between the students who completed the course and the students who did?

I found that the proportion of students who completed the test preparation course varied from 29% to 43% accordign to their parents' education level. I was suprised to find that the group of students whose parents had the least amount of schooling (didn't graduate high school) had the highest proportion of students that took the test. 

I also found that regardless of their parents' education level, taking the preparation course always resulted in higher test scores. 

# Development Environment
* Visual Studio Code
* Python 3.9.0 64-bit
* Pandas, Seaborn, and Matplotlib libraries in Python
* Git/GitHub

# Useful Websites

* [Pandas Tutorial](https://pandas.pydata.org/docs/user_guide/10min.html#min)
* [Example Analysis Using Pandas](https://www.kaggle.com/kashnitsky/topic-1-exploratory-data-analysis-with-pandas)

# Future Work
* Learn how to do statistical testing in Python in order to show how statistically significant my findings are. 

* Do analysis on more of the factors. Decide which factors have the most influence. 