class User():
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"Şu anda {cls.active_users} adet aktif kullanıcı var."

    def __init__(self,firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        User.active_users += 1

    def fullname(self):
        return self.firstName + self.lastName

class Moderator(User):

    active_moderators = 0

    @classmethod
    def display_active_moderators(cls):
        return f"Şu anda {cls.active_moderators} adet aktif moderator var."
    
    def __init__(self, firstName, lastName,community):
        super().__init__(firstName, lastName)
        self.community = community
        Moderator.active_moderators += 1

    def removePost(self):
        return f"{self.fullname()} isimli kullanıcı {self.community} konusundan bir post sildi"
    
    def updatePost(self):
        return f"{self.fullname()} isimli kullanıcı {self.community} konusundan bir post güncelledi"


print(User.display_active_users())
print(Moderator.display_active_moderators())
u1 = User("Mehmet","Yılmaz")
m1 = Moderator("Semih","Yılmaz","Temiz Enerji")
m2 = Moderator("Deniz","Gökçe","Atık Yönetimi")
print(User.display_active_users())
print(Moderator.display_active_moderators())
print("-"*30)
print(m1.removePost())
print(m2.updatePost())


# isinstance nesnenin hangi sınıftan türetildiğini sorar.
# print(isinstance(u1,User))
# print(isinstance(m1,Moderator))
# print(isinstance(m1,User))