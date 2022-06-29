# Project 01. Guess the number

## Table of contents
[1. Project description](https://github.com/f999145/f_data_science/blob/main/Project_01/README.md#Project-description)

[2. Which case are we solving?](https://github.com/f999145/f_data_science/blob/main/Project_01/README.md#Which-case-are-we-solving?)

[3. Data summary](https://github.com/f999145/f_data_science/blob/main/Project_01/README.md#Data-summary)

[4. Stages of the project](https://github.com/f999145/f_data_science/blob/main/Project_01/README.md#Stages-of-the-project)

[5. Result](https://github.com/f999145/f_data_science/blob/main/Project_01/README.md#Result)

[6. Conclusions](https://github.com/f999145/f_data_science/blob/main/Project_01/README.md#Conclusions)

### Project description
Guess the number given by the computer in the minimum number of attempts.

:arrow_up:[table of contents](https://github.com/f999145/f_data_science/blob/main/Project_01/README.md#Table-of-contents)

### Which case are we solving?
You need to write a program that guesses a number in the minimum number of attempts.

**Terms of competition:**
- The computer guesses an integer from 1 to 100, and we have to guess it. By "guess" we mean "write a program that guesses the number.
- The algorithm takes into account the information about whether a random number is larger or smaller than the number we want.

**Quality metric**
The results are evaluated by the average number of attempts at 1000 repetitions. It is necessary to achieve the minimum number of attempts.

**What we practice**
Learning to write good code in python.

### Data summary
The computer itself must guess a number from 1 to 100 inclusive.

:arrow_up:[table of contents](https://github.com/f999145/f_data_science/blob/main/Project_01/README.md#Table-of-contents)

### Stages of the project
+ Загружаем библиотеку numpy
+ Create a search function, which argument will be the sought number from 1 to 100 inclusive
  + Setting the search range between 1 and 100
  + Initiate an infinite loop
  + Check if the sought number is not 1 or 100
  + Find the middle value of the range and check if it is the sought value
  + Shift the boundary of the search by the middle value of the range:
    + Left if the average value is less than the value you are looking for
    + Right if the average value is greater than the sought value
  + Return the number of attempts to find the sought value
+ Create a function for finding the average number of attempts to find the guessed number with the search function

:arrow_up:[table of contents](https://github.com/f999145/f_data_science/blob/main/Project_01/README.md#Table-of-contents)

### Result
The algorithm finds the number from 1 to 100 in an average of 7 attempts.

:arrow_up:[table of contents](https://github.com/f999145/f_data_science/blob/main/Project_01/README.md#Table-of-contents)

### Conclusions

The algorithm for dividing in half is simple and quite efficient.
It required minimal intervention in the training code.
It was difficult to cope with the design, because there is no clear understanding of what needs to be done and how to do it.
I had to study additional materials and the mistakes of other students on the course.
I got the image in my head. But I'm not sure it's what it's supposed to be.

:arrow_up:[table of contents](https://github.com/f999145/f_data_science/blob/main/Project_01/README.md#Table-of-contents)