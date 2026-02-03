#Finding students who have failed only in one subject.
import pandas as pd
dt=pd.read_csv(r"C:\Users\Fahim\Downloads\150_students_separate_roll_name.csv")
s_c=dt.drop(columns=["Roll"]).select_dtypes(include='number')
fail=dt[(s_c<50).sum(axis=1)==1]
print(len(fail))