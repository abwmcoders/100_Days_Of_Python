def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide a valid input"
    
    formated_l_name = l_name.title()
    formated_f_name = f_name.title() 
    formated_name = f"{formated_f_name} {formated_l_name}"
    return formated_name


output = format_name(
    f_name = input("Enter your first name? "),
    l_name= input("Enter your last name")
)

print(output)