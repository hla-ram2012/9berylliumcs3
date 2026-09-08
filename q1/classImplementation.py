class FriendinPisay:
    def __init__(self, Name, GradeLevel, Section, FriendshipLevel):
        self.Name = Name
        self.GradeLevel = GradeLevel
        self.Section = Section
        self.FriendshipLevel = FriendshipLevel
    
    def updateFriendshipLevel(self, Input_FriendshipLevel):
        self.FriendshipLevel = Input_FriendshipLevel
    
    def updateGradeLevel(self, Input_GradeLevel):
        self.GradeLevel = Input_GradeLevel
    
    def updateSection(self, Input_Section):
        self.Section = Input_Section
    
    def displayInfo(self):
        print(
f"Name: {self.Name}\nGrade Level: {self.GradeLevel}\nSection: {self.Section}\nFriendship Level: {self.FriendshipLevel}" 
        )

object1 = FriendinPisay("Jeb Climaco", 8, "Silicon", "Close Friends")
object2 = FriendinPisay("Chance Caminar", 9, "Silicon", "Best Friends")

print("---Before---")
print(object1.displayInfo())
print('')
print(object2.displayInfo())
print('')
print('')
print(f"Changing Grade Level of {object1.Name}..")
Input_GradeLevel = int(input("Grade Level of friend: "))
object1.GradeLevel = Input_GradeLevel
print('')
print("---After---")
print(object1.displayInfo())
print('')
print(object2.displayInfo())
