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
print(object2.displayInfo())
print(f"Changing Grade Level of {object1.Name}..")
Input_GradeLevel = 9
object1.GradeLevel = Input_GradeLevel
print("---After---")
print(object1.displayInfo())
print(object2.displayInfo())
