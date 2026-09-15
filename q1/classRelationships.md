# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethod.md)
## Existing Class
Class: Friends in Pisay
Description: A class that represents the user's friends in Pisay with information about their full name, grade level, section, and friendship level.
## New Related Class
Class: Friend Group
Description: A class that represent's the user's known unique friend groups (also displaying its members) with information about their respective common interests, disinterests, relationship structure, and founders.
## Association
Relationship: Friend group HAS-A / contains / is assigned to Friends in Pisay
Explanation: The class, Friend group, contains the user's Friends in Pisay, but is assigned to their respective unique friend groups.
## Multiplicity
Multiplicity: Friend Group ───────── * Friends in Pisay
Explanation:
## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
