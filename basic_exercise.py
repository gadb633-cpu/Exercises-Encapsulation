# # 1. Private Username
# class UserProfile:
#     def __init__(self,username):
#         self.__username=username
#     @property
#     def username(self):
#         return self.__username
# profile = UserProfile("alice99")
# print(profile.username )      
# print(profile.__username )

# 2. Private Email with Getter
class UserProfile:
    def __init__(self,username, email):
        self.__username = username
        self.__email = email
    @property
    def username(self):
        return self.__username
    @property
    def email(self):
        return self.__email
profile = UserProfile("bob", "bob@mail.com")
print(profile.username)
print(profile.email)    

