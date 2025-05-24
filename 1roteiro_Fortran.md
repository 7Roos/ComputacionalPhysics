**Personal Notes**
- [x] Write script for the video
- [] Review the script
- [] Record the video
- [] Edit the video
- [] Upload the video
- [] Write the description
- [] Write the title
- [] Write the tags
- [] Draw the thumbnail
- [] Publish the video

# Hello World in Fortran: First Steps with the Oldest Scientific Language
## Intro
Currently, there is a real zoo of programming languages, each with the most diverse purposes, syntaxes and fervent defenders. However, this was not always the case. At the beginning of programming, until the 1990s, there were few languages available, which makes the current scenario a relatively recent event. But after all, what was the first successful programming language, that is, widely used? Well, it was the Fortran, developed by IBM to assist scientists in solving mathematical calculations. Each programming language is aimed at solving a specific class of problems and, if we remember that in the early days of computing, use was restricted to military and scientists, it makes sense that the first programming language was intended for science. Only after some time, its use extended to the corporate sphere and later to the domestic.
The simplest program we can test in a language is the famous "Hello World", popularized by Kernighan e Ritchie in his book "The C Programming Language". It is possible to write Fortran codes in basic text editors, such as the notepad and directly in the terminal via Nano editor and Vim. However, this is not the ideal approach to programming in today’s world. We must use a tool for this, that is, a code editor, because it offers several important features, such as the syntax highlighting with distinct colors and visual indication of typing errors and logic. In other words, before we start writing our first programs in Fortran, we will need to set up a proper development environment. An excellent choice for this is the popular 'VS Code', which stands out for its expandability through extensions, similar to installing applications on smartphones. Making it a great choice for development in Fortran. In particular, through the 'Modern Fortran' extension, which formats the code and analyzes the syntax before we compile the program. Before we write our first program in Fortran, let’s set up the development environment. For this, we will create a workbook called 'Test'. I have already presented in another video here on the channel (link in the description) how to configure the VS Code to work with Fortran, but we will review some important points. When you start VS Code for the first time for a new project, it will prompt you to specify a folder for your project. You can select an existing directory or create a new one now. This offers a significant advantage: when we open the integrated terminal within VS Code, it automatically positions itself in the path of your project folder. This way, we avoid the need to manually navigate between directories using Linux commands in the terminal, which makes the work much easier, especially for beginners who do not yet master the basic Linux commands.
Now, let’s create our first program in Fortran. Open VS Code and in the 'Test' workbook create a new file named 'Hello.f90'. The '.f90' extension is commonly used for source files in modern Fortran. Let’s discuss line by line of code: We start our program with the program block. The keyword 'Program' indicates the beginning of our program, and 'Hello' is the name we are giving to this program. You are required to provide a name for your program in Fortran. We may, for convenience, use the same file name. In the second line, we have the command that tells the computer to write something on the screen. 'Print' is the output statement, which by default is assumed to be the computer screen. The asterisk (*) after Print indicates that we are using default output formatting. A comma separates what we want to print. In quotes, we write our text message, which we want to be displayed on the screen: "Hello World'. Thus, the quotation marks (single or double) delimit the text to be printed. The content in quotation marks is also known as 'String' in many languages, but in Fortran we call it a string, or simply 'Characters'. Particularly, I refer to 'String' too, inheritance of my first learning in Python, besides being a more modern nomenclature. In the last line, we finish the program block that we start with 'Program Hello'. The keyword 'End Program' marks the end of our program, and it is a good practice to repeat the name of the program (although optional) after 'End Program' for clarity, especially in longer programs. It is important to note that Fortran does not differentiate between uppercase and lowercase letters. Similarly, the indentation of the code (the blanks at the beginning of the lines) does not affect how the program is run. However, maintaining a consistent indentation makes your code much easier to read and understand. Finally, after entering this code in the 'VS Code', save the changes by pressing the keys 'CTRL' and’S' simultaneously. Now we are ready to compile and run our "Hello World" in Fortran!
Fortran is a compiled language, which implies that before running a program we need to translate the source code into a form that the computer can understand. This translation process is called compilation. To open a terminal within the VS Code, simply navigate to the top left tab, click on 'Terminal' and select 'New Terminal'. Once the terminal is open, we can invoke the compiler. If you have installed the Intel IFX compiler, use the following command: 'IFX' 'Hello.f90'. If you are using the widely available and free GNU Fortran compiler, the corresponding command is: 'G Fortran' 'Hello.f90 '. The build process generates an executable file. On Unix-like operating systems (such as Linux and macOS), the default name for this file is 'A.out'. To run the program on Unix-like systems, we type in the terminal the path for the executable, which is usually point-slash, followed by the file name and press 'Enter'. Ready! If everything went well, the message "Hello World" will be displayed on your terminal. Did you like it? Then leave your like to support the channel!
In the first lines of the code, we can create a header with basic information such as author and creation date. To include this information without the Fortran compiler interpreting it as executable code and consequently generating errors, we use what we call "comments". In Fortran, the way to indicate a comment is by using the exclamation mark (!). This way, any content written to the right of that symbol in a line will be completely ignored by the compiler during the compilation process. Try adding a few lines of comment in your code to test this functionality.
As I mentioned earlier, the time has come to enable some extensions to increase our productivity in VS Code. The first of these is the overall interface theme. VS Code offers some themes natively, but you can install others as extensions. A popular theme is 'Dracula'. Particularly, I like to use a theme inspired by the works of Da Vinci, which offers more options for visual customization, but there are many other options. Particularly, this site offers a visual example of each of the extensions available in VS Code, eliminating the need to download one by one to check the result, and the possibility of check as the theme is in some other languages. Unfortunately, is not available for Fortran, we are the ugly duckling. Another useful extension is the 'Material Icon Theme'. Note that now our Fortran file displays an icon with the letter 'F', indicating that it is a Fortran file. This extension differentiates the various types of files by means of visual symbols. An essential extension is 'Modern Fortran', which enhances the syntax of our code, making it easier to read, and also alerts us about syntax errors. For example, if I forgot to close a quote, this extension would underline that part of the code. We can then place the cursor over the error or check the lower tab 'Problems', where there is usually a message indicating the cause of the error and sometimes suggesting a solution. The installation of this extension may be a bit complex, and I will leave the link to the documentation in the description. I confess that I often find it difficult to install it on clean Linux installations. Soon, I will do a detailed tutorial showing the correct way to install and configure this extension. Through 'Modern Fortran', we can also format our code, but for this it is necessary to install a formatter like 'Findent' and/or 'F Prettify'. For example, by right-clicking on the code or using a shortcut, we format the code following an indentation pattern. Okay, now our code looks much more professional. Finally, I also like to add an extension that allows you to view PDF files directly in the VS Code, which is very useful for consulting documentation or viewing results of graphs in PDF.
There are a few more important settings. One that I find quite useful is the "Auto Save" (Automatic Saving), so we don’t need to save the program every time we make a change before compiling. To activate it, go to 'File', in the upper right corner, and select the option 'Auto Save'. The terminal area can be expanded with the help of the mouse, by clicking and dragging the border or by clicking on the up arrow located in the lower right tab. We can open a new terminal by clicking on the plus icon (+). If we click on the icon next to it, we open a new terminal that inherits the same directory of the duplicate terminal. We can differentiate the terminals by name, color and symbol. To do this, just right-click on one of the terminals and select 'Change Color' and choose the desired color. Another option is to click on 'Rename' and assign a name to the terminal. You can also change the icon by clicking on the corresponding option. To close a terminal, just click the trash icon. We can also rearrange terminals. For example, to ungroup a cloned terminal, simply right-click on the terminal label in the lower right corner and select 'Unsplit Terminal' (Ungroup Terminal). To group terminals, we select a terminal and drag it to the side of the first terminal. In the tab 'File', we can create new files, import files from another folder, open another folder, among other actions. Alternatively, when hovering over the list of files in your directory in the sidebar, four icons appear at the top. By hovering over these icons, you will find the functions: create a new file, create a new folder, update (refresh) and the last function, which I have particularly never used.
Knowing a variety of shortcuts in VS Code is important because it greatly increases productivity. To shrink the side tab, we can click again on the active icon in the right sidebar or use the 'CTRL+B' command. To search for terms within the code, just use the 'CTRL+F' command; it will do the search. If you left click and hold down the 'Alt' key, it will activate multiple selection, allowing you to edit several lines at once. Still on multiple selection, when we assign an inappropriate name to a variable and after writing enough code, we find a better name, we do not need to search and replace term by term. Just use the default command 'CTRL+Shift+F2'. However, in my notebook, this is not the default shortcut. But no problem. Go to 'File', in the upper left corner, select the 'Preferences' and then 'Keyboard Shortcuts'. A window with all the commands listed will open. Then, look for 'Select All'; you’ll find some options. In my case, the command is 'CTRL+Shift+L'. Returning to the code, we select one of the terms and use 'CTRL+Shift+L'. See that now the cursor blinks on all occurrences; so when you change the word, this change is applied to all others. Another important shortcut is 'Alt+Z', which breaks lines of code artificially so that you can view the entire content of the code. On the VS Code website (link in the description) there is a very detailed tutorial for consultation.
We saw how simple it was to write this example program. I want to demonstrate in this series of videos that Fortran is a language very easy to learn and suitable for writing code for mathematical problems. Even, the name of this language is a contraction of the words 'Formula Translator'. In this sense, the language Julia is the closest to scripts similar to the writing of mathematical formulas. In particular, learning Fortran became is even easier with current generative AI tools, such as Gemini, ChatGPT, Cursor Editor, GitHub Copilot, among others, which assist in writing code and identifying errors. However, this does not exclude the formal study with the books of programming language and computational physics. However, it is worth mentioning that Fortran 77 is not so simple and has some atypical features that were made obsolete in the updates of Fortran 90, 95, 2003 and 2008. I will work here only with these newer versions, popularly known as 'Modern Fortran'. I will follow some excellent textbooks that were essential in my formal learning of the language. The titles of these works are here in the description. In addition, the Fortran language allows to build programs with high performance for complex mathematical problems, this being one more point that justifies its use even after all these decades. In the next video, I will show how to work with Fortran in the editor 'Cursor', which is an alternative with generative AI capabilities, thus allowing to increase productivity. See you next time!

# Integer

## Suggested Titles: 
- Variable Integers: Your Complete Beginner's Guide
- Mastering Integer Variables in Fortran (Easy Tutorial)
- Learn Integer Variables: A Step-by-Step Guide
- Unlocking the Power of Integers: A Beginner's Guide

## Future Videos
- Video 2: Order of Operations Hook
"Did you know that the order of operations in Fortran can lead to unexpected results? In this video, we’ll unravel the mysteries of operator precedence and how it affects your calculations." - The order of operations in Fortran: PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
- Video 3: Integer intrinsic functions
- Video 3: Question Hook
"Ever wondered why your Fortran code crashes when you try to store a decimal number in an integer variable?  Dive into the world of Fortran data types and discover the crucial differences between integers and real variables." - When 4 bytes are no longer sufficient. Expanding the size of an integer. Factors affecting data type selection: Memory usage and speed
- Video 4: Intriguing Statement Hook
"Choosing the right data type in Fortran can mean the difference between a flawless program and a frustrating bug. This video reveals the hidden complexities of integer and real variables and how to avoid common pitfalls." - cubic root of a negative number - if the number is integer, declare it as integer and not real.

## Introduction
Unlock the potential of programming with a solid understanding of integer variables. This video provides a beginner-friendly guide, equipping you with the knowledge and confidence to build your coding skills.

## We need to count objects
Counting objects has been a fundamental task since the dawn of human civilization. From ancient societies to modern times, counting has been essential for trade, agriculture, and record-keeping. To accomplish this, we define the set of natural numbers, denoted by the letter N.

There is considerable debate about whether the set of natural numbers includes zero or not. Some argue that natural numbers should start from 1, because they are used to count objects—you don't start counting "zero oranges, one orange, two oranges." In general convention, the set of natural numbers starts from 0, unless we indicate with an asterisk (*) that we are excluding zero.

Within this set, we can perform addition, the most basic operation in mathematics. For example, if we have 2 oranges and add 3 more, we will have a total of 5 oranges. In other words, addition is simple and intuitive, allowing us to count objects easily.

Specifically, we can organize objects in groups, where the result will be the multiplication of the number of objects in each group by the number of groups. For example, if we have 2 oranges in each group and 3 groups, we will have a total of 6 oranges. This is a simple and efficient way to count objects, especially when dealing with large quantities.

It is natural to define the division operation. For example, if we have 6 oranges and divide them into 3 groups, we will have 2 oranges in each group. This simple example might lead to the incorrect conclusion that division is the inverse of multiplication. In fact, division can seem like the inverse of multiplication in several situations. Let's look at another example: I can multiply 2 oranges by 0, resulting in 0. If I divide 0 by 2 oranges, I will also have 0 oranges. But if I divide 2 oranges by 0, I will have an undefined number of oranges. The key point is that division is not commutative—the order of numbers matters—while multiplication is commutative.

While addition always produces a result within the set of natural numbers, division can lead to results outside this set. For example, if we divide 2 oranges by 3, we will have a fraction of oranges. You'd get zero whole oranges with a remainder of 2. In other words, we have a remainder from the division, which is very important in certain problems, and we'll return to this point in the future.

Indeed, our problems require another operation: subtraction. However, not every subtraction yields natural numbers. We need to define a new set of numbers that includes negative values. This set is called the set of integers, usually denoted by the letter Z, which includes natural numbers, their negative counterparts, and zero.

In other words, we extend the set of natural numbers to include negative numbers; all operations valid for natural numbers remain valid for integers. The set of integers is a superset of natural numbers, meaning that all natural numbers are also integers, but the reciprocal is not always true. Therefore, in programming languages such as Fortran, the integer data type is used to represent whole numbers, both positive and negative. This allows us to perform arithmetic operations on integers, including addition, subtraction, multiplication, and division.

But it doesn't stop there. Integer numbers are used for indexing loops, arrays, and other structures. A loop is a repetition structure—a way to repeat a set of instructions multiple times. For example, if we want to calculate the sum of the first 10 natural numbers, we can use a loop to iterate from 1 to 10 and add each number to a running total. The loop index is typically an integer variable that keeps track of the current iteration. In another example, we use integer variables to index a matrix, identifying the row and column of each element. This is important because matrices are often used to represent data in scientific computing, allowing us to perform complex calculations efficiently through vectorization.

To sum up, although it may seem simple, the integer data type is a fundamental concept in programming, especially for representing discrete values within scientific computations.

- Provide a call to action, inviting viewers to subscribe for more tutorials and insights into the world of scientific computing with Fortran.

## Arithmetic Operations with Integers in Fortran
In Fortran, we can perform arithmetic operations with integers using the following operators:
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Exponentiation: `**`
For example, we perform these operations in this code:
```fortran
program arithmeticOperations
    print *, "Arithmetic Operations with Integers in Fortran"
    print *, "Addition: 2 + 3 =", 2 + 3
    print *, "Subtraction: 5 - 2 =", 5 - 2
    print *, "Multiplication: 4 * 3 =", 4 * 3
    print *, "Division: 10 / 2 =", 10 / 2
    print *, "Exponentiation: 2 ** 3 =", 2 ** 3
end program arithmeticOperations
```
- Step-by-Step Code Walkthrough: Walking viewers through the code, explaining each line and its purpose.
- Running your Program: Demonstrating how to execute the program and observe the output.

- Why Fortran? Its enduring legacy in scientific computing and its relevance today.
- Early limitations and the importance of efficient memory usage in the context of limited computer resources.

If we invert the numerators by denominators, we will have the zero result, because we perform integer division, which means that the result will be rounded down. In Fortran, it is ilegal more one token in operation. For resolve this problem, we need use the parentheses to enclausure the number. Nothe that, in the exponentiation operation, if we take the negative, we will have a negative result, or positive by the parentheses use.

## Implicit Declaration of Integer Variables

## Explicit Declaration of Integer Variables
- Fortran IV's introduction of the "INTEGER" keyword, providing programmers with more control over integer variable declarations.
- What are Integer Variables in Fortran? Explain the fundamental concept of integer variables in Fortran, including their purpose and data type.
- Declaring Integer Variables: Demonstrating how to declare integers in a Fortran program with examples.
- Assigning Values:  Explaining how to assign numerical values to integer variables.
- Language strongly typed.

- Explain the importance of using consistent variable names and adhering to coding conventions.
## Order of Operations in Fortran
- Exploring More Complex Operations: exponentiation with clear explanations and examples.

## Intrinsic Functions
- Introduce common built-in functions for integer operations, such as ABS, MOD (the 'joker' function), and MAX, and show how they can be used to enhance code functionality.

## Conclusion
- Mastering the nuances of Fortran integers and real variables is essential for any programmer
- Benefits of integer variables: Efficiency and simplicity
- The power of Fortran: Exploring its strengths in high-performance computing and numerical simulations.
- The evolution of integer types across Fortran standards, including the expansion to accommodate larger integers and the introduction of more precise integer representations.
- Exploring the impact of these changes on scientific computing, particularly in areas requiring large-scale computations.
- Encourage viewers to explore further resources and practice using integer variables in their own Fortran projects.

# Video 2: PEMDAS it is wrong
## Define the problem
The set integer, we can perform the addition operation, which is the most basic operation in mathematics. For example, if we have 2 oranges and add 3 more, we will have a total of 5 oranges. In other words, the addition operation is simple and intuitive, allowing us to count objects easily. Specially, we can organize the objects in a group, thus the result will be the multiplication of the number of objects in the group by the number of groups. For example, if we have 2 oranges in each group and 3 groups, we will have a total of 6 oranges. This is a simple and efficient way to count objects, especially when dealing with large quantities. It is natural define the division operation, that more people call it the inverse of the multiplication. But it is errorneous to think about it. For example, if we have 6 oranges and divide them into 3 groups, we will have 2 oranges in each group. This is a simple example might conduct to the wrong conclusion that the division is the inverse of the multiplication. In fact, the division operation can sound like the inverse of multiplication in several situations. Let’s take a look another example, I can multiply 2 oranges by 0, it is result 0. If I divide 0 by 2 oranges, I will have 0 oranges too. But, if I divide 2 oranges by 0, I will have an undefined number of oranges. The central key point is that the division operation is not commutative, that is, the order of the numbers matters, while the multiplication operation is commutative. This misconception can lead to confusion and errors in mathematical calculations. For example, the famous rule of the order of operations, which states that multiplication and division should be performed before addition and subtraction, putting the division operation in the same level of the multiplication, but it is not true, because these operations are not inverse of each other which subtration and addition are.  

Nevertheless, the people use this rule without reflect about it to solve the problems, but it is important to understand the underlying principles to avoid mistakes.

Now, since the commutative property of the multiplication, I prove that rule of the order of operations is not true. Before, it is worth to mention that this problem is far of being new, rather, it dates back to the early twentieth century.


