def segregate_zeros_and_ones(input_array):
    zeros_count = input_array.count(0)
    ones_count = len(input_array) - zeros_count
    
    output_array = [0] * zeros_count + [1] * ones_count
    
    return output_array

# Ask for user input
user_input_str = input("Enter a sequence of 0s and 1s (e.g., 101010110): ")
user_input_list = [int(char) for char in user_input_str]

# Call the function with user input
output_array = segregate_zeros_and_ones(user_input_list)

# Display the result
print("Input: ", user_input_list)
print("Output:", output_array)
