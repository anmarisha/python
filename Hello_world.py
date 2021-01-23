def read_float(user_prompt):
    # same as float(input(user_prompt))
    user_input = input(user_prompt)
    float_input = float(user_input)
    return float_input

n_float = read_float("enter number ")

op = input("enter operation ")

d_float = read_float("enter second number ")

if op == "add":
    result = n_float + d_float

elif op == "subtract":
    result = n_float - d_float

elif op == "multiply":
    result = n_float * d_float

elif op == "divide":

    if d_float == 0:
        print("zero division is not allowed")
    else: 

        result = n_float / d_float
else: 
    print("operation invalid")
    result = "huj"

print("hello world", n_float, op, d_float, result)