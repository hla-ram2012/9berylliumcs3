# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)
## Existing System Description:
1. What classes currently exist in your system?
Class FriendinPisay and FriendGroup.

2. What problem or limitation exists in your current design?
**Unable to access the information of each friend in pisay through the class Group Friends** - The user is only able to access the information of each friend by looking or using the individual class Friend in Pisay. Thus, the names of each friend will appear in the class Group Friends, but each of their information will not be publicly shown.

## Inheritance Relationship
Parent: Friend

Child: FriendinPisay

Explanation: The parent class Friend contains the information, while the child class FriendinPisay inherits these feature and determines the FriendshipLevel of the Friend to the user. Also, the child class has methods like updating the friendship level, updating the grade level, and updating the section.

## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Aggregation

Explanation: The class FriendinPisay_BestFriend cannot meaningfully exist without the class Friend in Pisay; however, class FriendinPisay can exist independently, possibly having their Best Friend assigned to them or not if they don't have any, ultimately making the class FriendinPisay_BestFriend HAS-A weak relationship with class FriendinPisay.
## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](images/advancedTestRun.png)
## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:
