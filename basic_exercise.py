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

# # 4. Private Follower Count
# class UserProfile:
#     def __init__(self,username):
#         self.__username=username
#         self.__followers = 0
#     @property
#     def followers(self):
#         return self.__followers
#     def follow(self):
#         self.__followers +=1
#     def unfollow(self):
#         self.__followers -=1 if self.__followers > 0 else None
# profile = UserProfile("gad")
# profile.follow()
# profile.follow()                    
# profile.follow()                    
# profile.unfollow()
# print(profile.followers)

# # 5. Protected Bio Field
# class UserProfile:
#     def __init__(self,username,bio):
#         self.username=username
#         self._bio =bio
#     @property
#     def bio(self):
#         return self._bio
# class VerifiedUser(UserProfile):
#     def __init__(self,username,bio,badge):
#         super().__init__(username,bio)
#         self.badge=badge
#     def full_description(self):
#         return f"{self.username} [{self.badge}]: {self._bio}"
# celeb = VerifiedUser("celeb", "Singer and songwriter", "✓")
# print(celeb.full_description())

# # 6. Age Setter with Range Check
# class UserProfile:
#     def __init__(self,username,age):
#         self.username = username
#         self.__age = age
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,new_age):
#         if 13 <= new_age <= 120:
#             self.__age = new_age
#             return self.__age
#         else:
#             print("Invalid age")
# profile = UserProfile("dan",18)
# profile.age = 10
# profile.age = 25
# profile.age = 200
# print(profile.age) 

# # 7. Password Protection
# class UserAccount:
#     def __init__(self,username, password):
#         self.username = username
#         self.__password = password
#     def check_password(self,attempt):
#         return True if attempt == self.__password else False 
#     def change_password(self,old, new):
#         if self.__password == old:
#             self.__password = new
#         else:
#             print("Incorrect old password")
# admin = UserAccount("admin", "secret")
# print(admin.check_password("wrong"))
# admin.change_password("secret", "new123")
# print(admin.check_password("new123"))

# 8. Post Like Counter
class Post:
    def __init__(self,author, content):
        self.author = author
        self.content = content
        self.__likes = 0
        self.__liked_by = []
    @property
    def likes(self):
        return self.__likes
    def like(self,username):
        if username not in self.__liked_by:
            self.__likes +=1
            self.__liked_by.append(username)
    def unlike(self,username):
        if username in self.__liked_by:
            self.__likes -=1
    def status(self):
        return f"Post by {self.author}: {self.likes} likes"
alice = Post("alice", "Hello world!") 
alice.like("gad")
alice.like("yossi")
alice.like("dan")
alice.unlike("yossi")
alice.like("gad")
print(alice.status())






