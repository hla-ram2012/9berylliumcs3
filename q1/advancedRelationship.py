# Contained Object Class
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
            print(f"List of members: {friendgroupList}")
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

# Parent Class
class Friend(FriendGroup):

    def __init__(self, Name: str, GradeLevel: int, Section: str, FriendGroup: FriendGroup = None):
        self.Name = Name
        self.GradeLevel = GradeLevel
        self.Section = Section
        self.FriendGroup = FriendGroup

    def get_Info(self) -> str:
        return f"""{self.Name} is currently in Grade {self.GradeLevel} in the section {self.Section}, whose main friend group is called {self.FriendGroup}."""


# Child Class using Inheritance
class FriendinPisay(Friend):

    def __init__(self, Name: str, GradeLevel: int, Section: str, FriendGroup: str, FriendshipLevel: str):
        super().__init__(Name, GradeLevel, Section, FriendGroup)
        self.FriendshipLevel = FriendshipLevel

    def updateFriendshipLevel(self, Input_FriendshipLevel):
        self.FriendshipLevel = Input_FriendshipLevel
    
    def updateGradeLevel(self, Input_GradeLevel):
        self.GradeLevel = Input_GradeLevel
    
    def updateSection(self, Input_Section):
        self.Section = Input_Section

# Aggregation: FriendinPisay_BestFriend receives an existing Friend object
class FriendinPisay_BestFriend:

    def __init__(self, bestfriendName: str, friend: Friend = None):
        self.bestfriendName = bestfriendName
        self.friend = friend

    def displayInfo(self):
        if self.friend:
            print(f"{self.bestfriendName} is {self.friend}'s best friend.")
        else:
            print(f"{self.bestfriendName} does not have a best friend!")


# Execution / Testing
if __name__ == "__main__":
    friendgroup1 = FriendGroup(friendgroupName="Basta FG nina Mateo", friendgroupInterest="ML", friendgroupDisinterest="Chance", friendgroupRelationship="Strong", friendgroupStatus="Active", friendgroupList=["Mateo", "Basty", "Jeb", "Don"])
    
    # Test 1 — Inheritance
    friend1 = FriendinPisay(Name="Jeb", GradeLevel=9, Section="Silicon", FriendshipLevel="Close Friends", FriendGroup=friendgroup1.friendgroupName)
    print("--- Test 1: Inheritance ---")
    print(friend1.get_Info())

    # Test 2 — Aggregation
    bestfriend = FriendinPisay_BestFriend(bestfriendName="Chance", friend=friend1.Name)
    print("\n--- Test 2: Aggregation ---")
    print(f"{bestfriend.bestfriendName} has a bestfriend named: {bestfriend.friend}")

    # Test 3 — Dependency
    print("\n--- Test 3: Dependency ---")
    print(f'Friend Group "{friendgroup1.friendgroupName}" is assigned to {friend1.Name}') 
