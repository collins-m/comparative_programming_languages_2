# comparative_programming_languages_2

### Object Oriented

​	I will start by outlining the object oriented implementation of the binary tree. Object oriented programming is a paradigm of programming wherein you program in accord with the principles of object oriented design.  The principals are as follows:

- Abstraction

  - Encapsulation
  - Inheritance
  - Polymorphism

I will outline my implementation of these four principals as I explain my approach.

___

##### _The Main class:_

​	The Main class is initiated with one paramater: __self._tree__. This is a binary tree object, and is initially empty. The Main class contains two methods: __help()__, and __main()__. The help() method prints out a series of commands that the program accepts, while the main() method is what builds the user interface and takes the inputs for the program. This class itself was not necessary, but I created it to stay true to the principal of _encapsulation_. Creating another class, and thus an object, kept the program in object oriented style and kept everything neatly formatted and contained. 

​	It also had the benefit of adding another layer of abstraction, which benefits the user and any future programmers that end up reading the code.

___

##### _The BinaryTree class:_

​	This class itself does not add anything new to the program, it simply relays the commands from the _Node_ class. Its sole purpose is for abstraction. To comment on the use of both a Main class and a BinaryTree class, it may seem redundant to have both.

​	However in a typical situation the Main class would not be necessary, as it is only used for demonstration purposes, so the two layers of abstraction are not very useful in this specific example, but in real-world application this class would be useful. For example, it could be extended and further application could be added from this level, this would speak to both _inheritance_and _polymorphism_. I will detail the methods used here in the Node class as they are largely the same.

___

##### _The Node class:_

​	Each node contains three parameters; data is the integer contained in the node, left is the node with a lower value that itself, and right is the node with a greater value. All of these parameters are privatized to keep true to _encapsulation_. Given that they are private, getters and setters have been created as well _(Note: the setters are public for simplicity and in real-world applications they would not be made public for typical programs)_.

​	The __insert()__ method takes one parameter - the integer you wish to insert - and allocates it in the appropriate position on the tree. As this is not a specifically balanced tree, the structure of the tree is totally dependent upon the order in which you place the integers.

​	The __search()__ method functions very much the same as the insert() method. Yet it returns true upon finding the correct integer instead of returning a string. It traverses the tree in the same fashion.

​	Apart from this, there are three separate ordered string methods. They are: __preorder()__, __inorder()__, and __postorder()__. These are very similar in code, but very different in output. The code is virtually identical, the only difference is the order of the statements.

___

​	Throughout this implementation, I tried to stick to the paradigm of object oriented programming as much as possible, as you can see, each of the principles have been mentioned and their use outlined in the program. Abstraction and Encapsulation were the most applicable however; this program had less use for polymorphism or inheritance than some others might have, but I have touched on their possible use cases.