class FriendGroup:
    def __init__(self, friendgroupName, friendgroupInterest, friendgroupDisinterest, friendgroupRelationship, friendgroupStatus, friendgroupList):
        self.friendgroupName = friendgroupName
        self.friendgroupInterest = friendgroupInterest
        self.friendgroupDisinterest = friendgroupDisinterest
        self.__friendgroupRelationship = friendgroupRelationship
        self.friendgroupStatus = friendgroupStatus
        self.friendgroupList = friendgroupList
    def displayList(self, friendgroupList):
        i = 0
        if len(friendgroupList) == 1:
            print("List of members: ")
            for i in range(len(friendgroupList)):
                print(friendgroupList[i])
    def add(self, friend):
      list = self.friendgroupList
      self.friendgroupList = list.append(friend)
      
    def displayInfo(self):
        print(f'''Friend Group Name: {self.friendgroupName}
        Common Interest: {self.friendgroupInterest}
        Common Disinterest: {self.friendgroupDisinterest}
        Relationship Structure: {self.__friendgroupRelationship}
        Status: {self.friendgroupStatus}
        List of Members: {self.friendgroupList}''')

class FriendinPisay:
    def __init__(self, Name, GradeLevel, Section, FriendshipLevel):
        self.Name = Name
        self.GradeLevel = GradeLevel
        self.Section = Section
        self.__private_FriendshipLevel = FriendshipLevel
    
    def updateFriendshipLevel(self, Input_FriendshipLevel):
        self.FriendshipLevel = Input_FriendshipLevel
    
    def updateGradeLevel(self, Input_GradeLevel):
        self.GradeLevel = Input_GradeLevel
    
    def updateSection(self, Input_Section):
        self.Section = Input_Section
    
    def displayInfo(self):
        print(
f"Name: {self.Name}\nGrade Level: {self.GradeLevel}\nSection: {self.Section}\nFriendship Level: {self.__private_FriendshipLevel}" 
        )

friend1 = FriendinPisay("Phil Bausa", 9, "Magnesium", "Close Friends")

fg1 = FriendGroup("Kulto ni Jacob", "Roblox", "Geng geng", "Strong", "Active", ["Alex Coleto", "Jacob Fortuno","Kate Grajo", "Miranda Tayo","Sofiya Abcede"])
fg2 = FriendGroup("Tara Gala", "Maggala", "Geng geng", "Strong", "Active", ["Jacob Fortuno", "Shaun Dy", "Krisha Arimado"])

print("--- BEFORE RELATIONSHIP ---")

friend1.displayInfo()

print("\nFriend groups:")
fg1.displayInfo()
print()
fg2.displayInfo()

print("\n--- BUILDING RELATIONSHIP ---")
print("Adding friend in pisay to friend groups...")

fg1.add(friend1.Name)
fg2.add(friend1.Name)

print("\n--- AFTER RELATIONSHIP ---")

print("\nInformation of each Friend Groups:")
fg1.displayInfo()
print()
fg2.displayInfo()
