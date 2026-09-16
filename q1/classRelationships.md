# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethod.md)

## Existing Class
Class: Friend in Pisay

Description: A class that represents the user's friend in Pisay with information about his or her full name, grade level, section, and friendship level.

## New Related Class
Class: Friend Group

Description: A class that represent's the user's known unique friend groups (also displaying its members) with information about their respective common interests, disinterests, relationship structure, and founders.

## Association
Relationship: Friend group HAS-A / contains / is assigned to Friend in Pisay

Explanation: The class, Friend group, contains the user's Friend in Pisay, but is assigned to their respective unique friend groups.

## Multiplicity
Multiplicity: Friend Group 0..* ───────── 1..* Friend in Pisay

Explanation: A friend group (if the friend doesn't have a friend group, then it will display "N/A") can be assigned to or contain the user's friend/s that are in Pisay.

## UML Class Relationship Diagram
![Class Relationship Diagram](classRelationshipDiagram.png)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](relationshipTestRun.png)

## Object Relationship Diagram
![Object Relationship Diagram](objectRelationshipDiagram.png)

## Analysis

### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
