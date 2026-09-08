# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)
## Design Revision
Describe any changes made to your original class.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| Name | Integer | Public | Public so that anyone can see my friend's name. |
| GradeLevel | Integer | Public | Public so that anyone can see my friend's grade level. |
| Section | String | Public | Public so that anyone can see my friend's section. |
| FriendshipLevel | String | Private | Private so that I am the only one who can see my relationship with my friend.. |

+--------------------------------------------+
| FriendsinPisay |
+--------------------------------------------+
| + Name : string |
| + GradeLevel : integer |
| + Section : string |
| - FriendshipLevel : string |
+--------------------------------------------+
| + addFriend(Input_Name : string) |
| + removeFriend(Input_Name : string)|
| + updateFriendshipLevel(Input_Name : string) |
| + updateGradeLevel(Input_Name : string) |
| + updateSection(Input_Name : string) |
| + displayListofFriendsinPisay() |
| + displayInfo(Input_Name : string) |
+--------------------------------------------+
## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)
## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
