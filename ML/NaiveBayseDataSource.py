import pandas as pd

# Dataset
data = {
    "Hours": [1, 2, 2, 3, 3, 4, 4, 5, 5, 6,
              6, 7, 7, 8, 8, 9, 2, 4, 6, 9],

    "Assignment": [
        "No", "No", "Yes", "No", "Yes",
        "No", "Yes", "No", "Yes", "Yes",
        "No", "Yes", "No", "Yes", "Yes",
        "Yes", "No", "Yes", "Yes", "No"
    ],

    "Previous": [
        "Fail", "Fail", "Fail", "Pass", "Fail",
        "Fail", "Pass", "Pass", "Fail", "Pass",
        "Pass", "Pass", "Fail", "Pass", "Fail",
        "Pass", "Pass", "Fail", "Fail", "Pass"
    ],

    "Result": [
        "Fail", "Fail", "Fail", "Fail", "Fail",
        "Fail", "Pass", "Pass", "Pass", "Pass",
        "Pass", "Pass", "Pass", "Pass", "Pass",
        "Pass", "Fail", "Fail", "Pass", "Pass"
    ]
}

df = pd.DataFrame(data)

df.to_excel("Resources/NB_srudent_pass_fail.xlsx",index=False)