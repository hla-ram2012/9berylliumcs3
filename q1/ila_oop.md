# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation acts as a protective mechanism that keeps external code from accessing and modifying an object's internal state. In the case of the sari-sari store inventory system, encapsulation is implemented by combining product information, namely  name, price, and stock level with the functions that manipulate product data in a Product class. To keep variables like stock from being modified directly, such variables must be declared private and updated through controlled public methods, such as restock() and sellProduct(). This way, the programmer can improve the structure of the program by keeping the data safe and ensuring the stock is not unintentionally decreased as it cannot generate negative stock values or be corrupted by other pieces of code.

### 2. Abstraction
Abstraction aids in the program design by concealing complex and unnecessary internal functioning and only revealing the basic functions in the user interface. A typical example of this is a PointOfSale or InventoryManager class which gives a user a simple method like process_sale(product_name, quantity). The store manager does not need to know how the program searches through a database or works with discounts and subtraction process; they only deal with the simple interface. This helps to reduce complexity and enables anyone, preferably with programming experience, to change the logic or database later without disrupting the operations from the end-user's perspective.

### 3. Inheritance
Inheritance allows for the creation of specific product categories from a more general parent class without performing code copying. For instance, PerishableProduct is a derived class that takes its name and price attributes from the parent Product class while providing an additional attribute expiry_date. Such organization of product classes makes it possible to create a clear hierarchy and use more reused code for different product items.

### 4. Polymorphism
With polymorphism, various production types are capable of calling the same method name in different fashion. For instance, the both regular and the perishable items may carry out the same function called calculate_price(), which can be overridden by the perishable item so that discounting activities would take place in case of near expiration. This allows the system design to be improved as multiple items could be processed without complicated conditional checks when being checked out.

## Reflection
Object-Oriented Programming (OOP) helps solve the limitations of procedural programming by grouping data and behaviors into "objects," making large-scale software modular, reusable, and secure; without it, massive codebases will instantly or quickly become messy and hard to fix because a small change in one function can break the entire program. In designing the sari-sari store inventory system, it provided a massive advantage over a purely procedural approach, making the codebase highly structured, easier to debug, scalable, and simple to maintain over time.
