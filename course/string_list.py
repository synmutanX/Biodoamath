# move file
import shutil
import os

# Define the source file path and the destination path
source_file = '/mnt/c/Users/maula/Downloads/rosalind_ini1.txt'  # Replace with your source file path
destination_file = '/mnt/d/Bioinformatika/Biodoamath/rosalind/dataset/'  # Replace with your destination file path

# Move the file
# try:
#     shutil.move(source_file, destination_file)
#     print(f"File moved from {source_file} to {destination_file}")
# except FileNotFoundError:
#     print("The source file does not exist.")
# except PermissionError:
#     print("You do not have permission to move this file.")
# except Exception as e:
#     print(f"An error occurred: {e}")

# Open the file in read mode
with open('dataset/rosalind_ini3.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()
# Process the first line (the text)
text = lines[0].strip()  # Remove any leading/trailing whitespace or newlines
# Process the second line (the numbers)
numbers = list(map(int, lines[1].strip().split()))  # Convert the string of numbers to a list of integers

# def get_particular_string(string, integer_string):
#     get_list_of_index_from_integer_string = integer_string.split()
#     index_a = int(get_list_of_index_from_integer_string[0])
#     index_b = int(get_list_of_index_from_integer_string[1]) + 1
#     index_c = int(get_list_of_index_from_integer_string[2])
#     index_d = int(get_list_of_index_from_integer_string[3]) + 1
#     return string[index_a:index_b] + " " + string[index_c:index_d]

def get_particular_string(string, index):
    index_a = index[0]
    index_b = index[1] + 1
    index_c = index[2]
    index_d = index[3] + 1
    return string[index_a:index_b] + " " + string[index_c:index_d]

# take dataset
# string = 'NELMHX4P3JE3uySXgchXXGHEzzvrVhgnLDtvHqUzNwA8sBujwdx8BkfXFErzCapellaAn2ML78kNDorQ4DhsA57HyKyJa6vjpenwOCIIVqLMYWcrYGKhsX31du2ANDhtwlVxEXbhirundoh6jan78pD9DtAyLU4s.'
# integer_string = '60 66 135 141'

q3 = get_particular_string(text, numbers)
print(q3)

