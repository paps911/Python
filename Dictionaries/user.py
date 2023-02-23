#adding items
# profile = {}
# profile["Username"] = "user123"#adding vlues in the dictionaries
# profile["age"]= 23
# profile["email"]= "user123@gmail.com"
# profile["repos"] = {"name":"python",
#                     "commits":5}
# print(profile)  

profile={}
def register():
    u = input("Enter username: ")
    e = input("Enter email: ")
    p = input("Enter password: ")

    #store in dictionary
    profile["Username"] = u
    profile["email"] = e
    profile["Password"] = p

def get_profile():
    print(profile)

def change_username(new_name):
    new_name = input("Enter new username: ")
    profile["Username"] = new_name

register()
change_username("new_name")
get_profile()