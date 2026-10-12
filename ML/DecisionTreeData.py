
import pandas as pd

data = {
    "Outlook": [
        "Sunny", "Sunny", "Cloudy", "Rainy", "Rainy",
        "Rainy", "Cloudy", "Sunny", "Sunny", "Rainy",
        "Sunny", "Cloudy", "Cloudy", "Rainy", "Sunny"
    ],
    "Temperature": [
        "Hot", "Hot", "Mild", "Cool", "Mild",
        "Cool", "Hot", "Mild", "Cool", "Mild",
        "Mild", "Cool", "Mild", "Hot", "Hot"
    ],
    "Humidity": [
        "High", "High", "Normal", "Normal", "High",
        "Normal", "High", "Normal", "Normal", "High",
        "Normal", "High", "Normal", "Normal", "High"
    ],
    "Windy": [
        "No", "Yes", "No", "No", "Yes",
        "Yes", "Yes", "No", "No", "No",
        "Yes", "Yes", "No", "Yes", "No"
    ],
    "Ground": [
        "Dry", "Dry", "Dry", "Wet", "Wet",
        "Dry", "Dry", "Wet", "Dry", "Wet",
        "Dry", "Dry", "Dry", "Wet", "Dry"
    ],
    "Play_Cricket": [
        "Yes", "No", "Yes", "No", "No",
        "Yes", "Yes", "No", "Yes", "No",
        "Yes", "Yes", "Yes", "No", "No"
    ]
}

df = pd.DataFrame(data)

df.to_excel("C:\\CodeMines\\CodeMines Python\\DATA SCIENCE\\BATCH 12\\Resources\\cricket_data.xlsx")