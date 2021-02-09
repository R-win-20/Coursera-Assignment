import pandas as pd

students = [{'Name': 'Alice',
					'Class': 'Physics',
					'Score': 85},
			{'Name': 'Jack',
					'Class': 'Chemistry',
					'Score': 82},
			{'Name': 'Hellen',
					'Class': 'Biology',
					'Score': 90}]

df = pd.DataFrame(students, index=['school1', 'school2', 'school1'])

print(df.head())
print('------------------------------------------')
print(df.loc['school2'])
print('------------------------------------------')
print(df.loc['school1'])
print('------------------------------------------')
print('To list all students in school1')
print(df.loc['school1', 'Name'])
print('------------------------------------------')
print('To Transpose your frame; Use this :')
print(df.T)
#Or you can just write print(df.T.loc['Name']) to see list of students transposed
print('------------------------------------------')
print(df.loc[:, ['Name', 'Score']])

#To drop a row into your dataframe, just type:
print('------------------------------------------')
print(df.drop('school1'))
print('------------------------------------------')

#You may make a copy of your dataframe by coping it like this.
 copy_df = df.copy()
print(del copy_df['Class'])