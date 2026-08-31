##making function by key: value
def user_list(firstname, lastname):
    return(f"{firstname} {lastname}")

print(user_list(firstname="Adhish", lastname="Pokharel"))



### *args and **Kwargs

#args
def list (*names):
    # return(f"user names: {names}")
    return(f"user names: {names[0]}")
print(list("Adhish", "Pratik", "Sujal"))


#kwargs
