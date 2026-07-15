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
