# Objects, Classes & Data Containers

1. Classes should be small.
   - Classes should have a single responsibility. 
2. Cohesion --> the goal is achieve **High Cohesion**
3. Apply the Law Of Demeter
4. Write Classes in a SOLID way.
    - S => Single Responsibility Principle
    - O => Open Closed Principle
    - L => Liskov Substitution Principle
    - I => Interface Segregation Principle
    - D => Dependency Inversion/Injection Principle

## Difference Between Objects and Data Structures.

1. **Objects**
   1. Private internals / Properties, public API (methods)
   2. Contain your business logic
   3. Abstractions over concretions
   

2. **Data Structures / Data Container**
   1. Public internals / properties, almost no API (methods)
   2. Store and transport data
   3. Concretions only

## Polymorphism
- the ability of an object to take many forms.

## Cohesion
- Mean that the class have a single responsibility.
- Also Means that **How much are your class methods using the class properties?**

## Law of Demeter
- is concerned with the code like this: `this.customer.lastPurchase.date`
- The law of demeter says that we should avoid this code.
- The principle of Least Knowledge: Don't Depend on the internals of "strangers" (Other objects which you don't know)


## Single Responsibility Principle - SRP
- Classes should have a single responsibility - a class shouldn't change for more than one reason.

## Open-Closed Principle - OCP
- A class should be open for extension but closed for modification.
  - extend the class using the subclassing (inheritance).

## Liskov Substitution Principle - LSP
- Objects should be replaceable with instances of their subclasses without altering the behavior.

## Interface Segregation Principle - ISP
- Many client-specific interfaces are better than one general purpose interface.

## Dependency Inversion/Injection Principle - DIP
- You should depend upon abstractions, not concretions