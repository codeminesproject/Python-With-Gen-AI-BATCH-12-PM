
import pandas as pd

# 1. Create the original dataset
data = {
    "Hours": [1, 2, 2, 3, 4, 5, 6, 6, 7, 8],
    "Assignment": [0, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    "Previous_Result": [0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
    "Result": ["Fail", "Fail", "Fail", "Fail", "Fail",
               "Pass", "Pass", "Pass", "Pass", "Pass"]
}

df = pd.DataFrame(data)

df.to_excel("Resources/svm_Data.xlsx")