Annex B
Computational Thinking Exercise: "Smart Vending Machine"

Section: 9 - Arayat         Score:____________

C# / Name: Angeles, Apostol, Aquino  (C.N 1,2,3) Date: August 12


Scenario
Your school installs a vending machine to provide snacks and drinks. However, students encounter several issues:

Sometimes the machine does not give the correct change.
Items run out, but the machine doesn’t notify anyone.
Students press the wrong buttons and get the wrong item.
The machine is slow when multiple students use it in succession.
Your task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem
Main Problem: The Vending Machine is ineffective, unreliable, and inconvenient

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. Machine gives the incorrect amount of change.
2. Machine doesn't notify owner when a stock of a specific item is depleted.
3. Students press the wrong buttons and end up getting the wrong item.
4. Machine becomes slower when multiple students use it in succession.


Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

Sub-Problem:
Machine gives the incorrect amount of change.
CT Skill:
Algorithm Design
Example Solution:
First, the user inputs the amount they will pay with, next they will input the item they would like to buy and the quantity to be purchased.
The machine will then ask if the user will buy another item. If they do, the user will input another item and the quantity to be purchased.
If the user says no, the machine will then calculate the change needed and give it to the user.

Sub-Problem:
Machine doesn't notify owner when a stock of a specific item is depleted.
CT Skill:
Data Representation, Algorithm Design
Example Solution:
When the machine drops an item, it will subtract 1 from the stock of the item dropped before the purchase was made. 
After this, the machine will check if the stock of the item dropped is zero. If not, nothing will happen.
If the stock is zero, the machine will label the item as sold out and notify the owner or manager of the machine.

Sub-Problem:
Students press the wrong buttons and end up getting the wrong item.
CT Skill:
Algorithm Design
Example Solution:
If a student were to order an item, the machine would ask if they are sure that they would buy it.
If the student says yes, the machine will drop it. If no, the student will pick their desired item.

Sub-Problem:
Machine becomes slower when multiple students use it in succession.
CT Skill:
Algorithm Design
Example Solution:
After a user has received their order from the machine, the machine will then start a 10 second countdown before it takes another order.

Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem (Your group could use a separate sheet of paper)
Flowchart for Sub-Problem 1:
<img width="285" height="596" alt="Actual sub-problem 1 flowchart" src="https://github.com/user-attachments/assets/ac282959-307f-47cf-b7a3-ee43834eeb06" />