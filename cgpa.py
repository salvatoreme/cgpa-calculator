import pandas as pd
import json

grade_points = {'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C': 5, 'RA': 0}
cgpa = 0
gpa = 0
ttl_credits = 0
grade = 0
file = ["sem1.csv", "sem2.csv"]
df = []

for files in file:
    frames = pd.read_csv(files)
    df.append(frames)

combined_df = pd.concat(df)
combined_df['grade'] = combined_df['grade'].map(grade_points)

for index, row in combined_df.iterrows():
    gpa += row['credits'] * row['grade']
    ttl_credits += row['credits']
    

cgpa = gpa / ttl_credits
print("CGPA:", cgpa)
