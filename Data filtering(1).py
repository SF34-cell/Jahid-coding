#Finding any student who have failed any(at least one or many) subject.
import pandas as pd
dt=pd.read_csv(r"C:\Users\Fahim\Downloads\150_students_separate_roll_name.csv")
selected_subs=dt.drop(columns=["Roll"]).select_dtypes(include='number')
fail=dt[(selected_subs<50).any(axis=1)]
print(fail)
