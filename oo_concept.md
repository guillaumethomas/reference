# Oriented Programming Concepts

## Class

In object-oriented programming, a class is an extensible program-code-template for creating objects, providing initial values for state (member variables) and implementations of behavior (member functions or methods).In many languages, the class name is used as the name for the class (the template itself), the name for the default constructor of the class (a subroutine that creates objects), and as the type of objects generated by instantiating the class; these distinct concepts are easily conflated.

When an object is created by a constructor of the class, the resulting object is called an instance of the class, and the member variables specific to the object are called instance variables, to contrast with the class variables shared across the class.

In some languages, classes are only a compile-time feature (new classes cannot be declared at runtime), while in other languages classes are first-class citizens, and are generally themselves objects (typically of type Class or similar). In these languages, a class that creates classes is called a metaclass.

## Instance

In object-oriented programming (OOP), an instance is a concrete occurrence of any object, existing usually during the runtime of a computer program. Formally, "instance" is synonymous with "object" as they are each a particular value (realization), and these may be called an instance object; "instance" emphasizes the distinct identity of the object. The creation of an instance is called instantiation.

In class-based programming, objects are created from classes by subroutines called constructors, and destroyed by destructors. An object is an instance of a class, and may be called a class instance or class object; instantiation is then also known as construction. Not all classes can be instantiated – abstract classes cannot be instantiated, while classes that can be instantiated are called concrete classes. In prototype-based programming, instantiation is instead done by copying (cloning) a prototype instance.

An object may be varied in a number of ways. Each realized variation of that object is an instance of its class. Each time a process runs, it is an instance of some program. That is, it is a member of a given class that has specified values rather than variables. In a non-programming context, you could think of "dog" as a type and your particular dog as an instance of that class.

An important distinction is between the data type, which is interface, and the class, which is implementation.

## Object

In computer science, an object can be a variable, a data structure, a function, or a method, and as such, is a location in memory having a value and referenced by an identifier.

In the class-based object-oriented programming paradigm, "object" refers to a particular instance of a class where the object can be a combination of variables, functions, and data structures.

In relational database management, an object can be a table or column, or an association between data and a database entity (such as relating a person's age to a specific person).

## Encasuplation:

Encapsulation is one of the fundamentals of OOP (object-oriented programming). It refers to the bundling of data with the methods that operate on that data.[5] Encapsulation is used to hide the values or state of a structured data object inside a class, preventing unauthorized parties' direct access to them. Publicly accessible methods are generally provided in the class (so-called getters and setters) to access the values, and other client classes call these methods to retrieve and modify the values within the object.

This mechanism is not unique to object-oriented programming. Implementations of abstract data types, e.g. modules, offer a similar form of encapsulation. This similarity stems from the fact that both notions rely on the same mathematical fundamental of an existential type.