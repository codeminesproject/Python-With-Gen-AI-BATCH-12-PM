
import re

description = "At our institution, we are committed123 ● to delivering high-quality 56789 education in programming and technology. Our courses are designed to provide comprehensive knowledge and practical skills in various programming languages and technologies. We pride ourselves on offering a supportive learning environment where students can thrive and reach their full potential."

print(description)
print("-----------------------------------------------------------")

# replace special characters with space

description_without_special_characters = re.sub(r"[^a-zA-Z0-9\s]"," ",description)
print(description_without_special_characters)


print("-----------------------------------------------------------")

# replace extra spaces with single space
final_description = re.sub(r"\s+"," ",description_without_special_characters)
print(final_description)

print("-----------------------------------------------------------")

# replace numbers with empty

description_without_numbers = re.sub(r"\d+","",final_description)
print(description_without_numbers)
