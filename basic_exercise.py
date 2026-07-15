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

# # 2. Private Email with Getter
# class UserProfile:
#     def __init__(self,username, email):
#         self.__username = username
#         self.__email = email
#     @property
#     def username(self):
#         return self.__username
#     @property
#     def email(self):
#         return self.__email
# profile = UserProfile("bob", "bob@mail.com")
# print(profile.username)
# print(profile.email)  

# # 3. Username Setter with Validation
# class UserProfile:
#     def __init__(self,username):
#         self.__username=username
#     @property
#     def username(self):
#         return self.__username
#     @username.setter
#     def username(self,new_username):
#         self.__username =new_username if len(new_username) >=3 else print("Username too short")


# p = UserProfile("alice")
# p.username = "ab"    
# p.username = "alexis"
# print(p.username)

# 4. Private Follower Count
class UserProfile:
    def __init__(self,username):
        self.__username=username
        self.__followers = 0
    @property
    def followers(self):
        return self.__followers
    def follow(self):
        self.__followers +=1
    def unfollow(self):
        self.__followers -=1 if self.__followers > 0 else None
profile = UserProfile("gad")
profile.follow()
profile.follow()                    
profile.follow()                    
profile.unfollow()
print(profile.followers)



