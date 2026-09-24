# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)
## Existing System Description:
1. What classes currently exist in your system?
Class Friend in Pisay and Friend Group.

2. What problem or limitation exists in your current design?
**Unable to access the information of each friend in pisay through the class Group Friends** - The user is only able to access the information of each friend by looking or using the individual class Friend in Pisay. Thus, the names of each friend will appear in the class Group Friends, but each of their information will not be publicly shown.

## Inheritance Relationship
Parent: Friend Group

Child: Friend in Pisay

Explanation: Class Group Friends contain atleast two or many class Friend in Pisay. Thus, we can be able to classify each class Friend in Pisay to their respective Group Friends.

## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Aggregation

Explanation: The class Friend Group cannot meaningfully exist without the class Friend in Pisay; however, class Friend in Pisay can exist independently, having no Friend Group assigned to them, ultimately making the Friend Group HAS-A weak relationship with Friend in Pisay.
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
