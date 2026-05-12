def join_strings(strings):
    joined_string = ""
    if len(strings) == 0:
        return joined_string
        
    last_string = strings[len(strings) - 1]
    
    for string in strings[:-1]:
        joined_string = joined_string + string + ","
 
    return joined_string + last_string

# Test case example
string_list = ["Annie", "Reiner", "Bertholdt"]
joined_string = join_strings(string_list)
print(joined_string)
# "Annie,Reiner,Bertholdt"

string_list = ["Eren", "Mikasa", "Armin"]
joined_string = join_strings(string_list)
print(joined_string)
# "Eren,Mikasa,Armin"