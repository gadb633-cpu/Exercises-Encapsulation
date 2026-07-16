# 1. Private Username
class UserProfile:
    def __init__(self,username):
        self.__username=username
    @property
    def username(self):
        return self.__username
profile = UserProfile("alice99")
print(profile.username )      
print(profile.__username )

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

# 3. Username Setter with Validation
class UserProfile:
    def __init__(self,username):
        self.__username=username
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,new_username):
        self.__username =new_username if len(new_username) >=3 else print("Username too short")


p = UserProfile("alice")
p.username = "ab"    
p.username = "alexis"
print(p.username)

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

# 5. Protected Bio Field
class UserProfile:
    def __init__(self,username,bio):
        self.username=username
        self._bio =bio
    @property
    def bio(self):
        return self._bio
class VerifiedUser(UserProfile):
    def __init__(self,username,bio,badge):
        super().__init__(username,bio)
        self.badge=badge
    def full_description(self):
        return f"{self.username} [{self.badge}]: {self._bio}"
celeb = VerifiedUser("celeb", "Singer and songwriter", "✓")
print(celeb.full_description())

# 6. Age Setter with Range Check
class UserProfile:
    def __init__(self,username,age):
        self.username = username
        self.__age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,new_age):
        if 13 <= new_age <= 120:
            self.__age = new_age
            return self.__age
        else:
            print("Invalid age")
profile = UserProfile("dan",18)
profile.age = 10
profile.age = 25
profile.age = 200
print(profile.age) 

# 7. Password Protection
class UserAccount:
    def __init__(self,username, password):
        self.username = username
        self.__password = password
    def check_password(self,attempt):
        return True if attempt == self.__password else False 
    def change_password(self,old, new):
        if self.__password == old:
            self.__password = new
        else:
            print("Incorrect old password")
admin = UserAccount("admin", "secret")
print(admin.check_password("wrong"))
admin.change_password("secret", "new123")
print(admin.check_password("new123"))

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

# 9. Profile Privacy Settings
class UserProfile:
    def __init__(self,username):
        self.username = username
        self.__is_public = True
        self.__show_email = False
        self.__show_age = False
    @property
    def is_public(self):
        return self.__is_public
    @property
    def show_email(self):
        return self.__show_email
    @property
    def show_age(self):
        return self.__show_age
    @is_public.setter
    def is_public(self,new_is_public):
        if new_is_public == True or new_is_public == False:
            self.__is_public = new_is_public
            return self.__is_public    
        else:
            print("is_public must be True or False.")
    @show_email.setter
    def show_email(self,new_show_email):
        if new_show_email == True or new_show_email== False:
            self.__show_email = new_show_email
            return self.__show_email    
        else:
            print("show_email must be True or False.")
    @show_age.setter
    def show_age(self,new_show_age):
        if new_show_age == True or new_show_age== False:
            self.__show_age = new_show_age
            return self.__show_age
        else:
            print("show_age must be True or False.")
    def privacy_summary(self):
        print(self.is_public)
        print(self.show_email)
        print(self.show_age)
profile = UserProfile("gad")
profile.is_public = "yet"
profile.show_email = True
profile.privacy_summary()

# 10. Full User Account System
class UserAccount:
    def __init__(self,username, email, password, age):
        self.__username =username
        self.__email =email
        self.__password = password
        self.__age =age
        self._login_count = 0
    @property
    def username(self):
        return self.__username
    @property
    def email(self):
        return self.__email
    @property
    def age(self):
        return self.__age
    @username.setter
    def username(self,new_username):
        if len(new_username) < 3:
            return "username is too short"
        else:
            self.__username = new_username
            return self.__username
    @email.setter
    def email(self,new_email):
        if "@" in new_email:
            self.__email = new_email
            return self.__email
        else:
            return "email must contain @"        
    @age.setter
    def age(self,new_age):
        if 13<=new_age<=120:
            self.__age = new_age
            return self.__age
        else:
            return "age most be batween 13-120"
    def check_password(self,attempt):
        return True if attempt == self.__password else False
    def change_password(self,old, new):
        if self.__password == old:
            self.__password = new
    def login(self,password):
        if password == self.__password:
            self._login_count +=1
            return "welcome!"
        else:
            return "Login failed"
    def account_summary(self):
        return f"username is: {self.__username} | email is: {self.__email} | age is: {self.__age} | logins: {self._login_count} "
user1 = UserAccount("user1", "u@mail.com", "pass123", 20)
print(user1.login("587"))
print(user1.login("gad47"))
print(user1.login("pass123"))
user1.email = "t@jfjiro.com"
user1.age = 55
print(user1.account_summary())              







