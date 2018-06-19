---
layout: page
title: Introduction to Cybersecurity First Principles
---
## Cybersecurity First Principles in this lesson

This lesson is about cybersecurity first principles. So all of them will be discussed.

## Lesson goals

1. Understand and apply cybersecurity first principles
2. Explain cybersecurity first principles

## Materials required
- [Gencyber Cyber Realm Card Deck](https://gencybercards.com)

## Prerequisite lessons
- None, just lots of curiosity

## Table of Contents    

- [Cybersecurity First Principles](#cybersecurity-first-principles)
- [CIA Triad - Expectations of Information](#cia-triad---expectations-of-information)
- [Card Game](#card-game)
- [Additional Resources](#additional-resources)
- [Acknowledgements](#acknowledgements)
- [License](#license)


## Cybersecurity First Principles

### What are first principles?

Building a secure system is a design problem. Which means that there is no de-facto recipe to do so. In the absence of methodical techniques, experience has contributed to a set of first principles. The principles are basic, foundational propositions regarding what qualities of a system contribute to cybersecurity. These principles guide tradeoffs during system design that contribute to security.

### Stepping through the principles

We now examine 10 cybersecurity first principles. This discussion is adapted from [NSA guidance](https://users.cs.jmu.edu/tjadenbc/Bootcamp/0-GenCyber-First-Principles.pdf) on this topic.

#### 1. Domain Separation

- What is a `Domain`?
  - In a computer, this word refers to a _collection of data or instructions_ that warrant protection. Outside of a computer, a domain can be an area of responsibility or control.
  - Separating domains allows for enforcement of rules governing the entry and use of domains by entities outside the domain.
  - During system testing, test data should be separated from "real" data, such as personal information. Such separation avoids unauthorized or accidental disclosure of personal or sensitive data.


- Examples
  - Most computer processors run in two states. The `supervisor domain` and the `user domain`. The processor, when in the supervisor domain, can directly access memory (i.e. RAM) or manipulate access control tables in a primitive file system. When in the user domain, the processor cannot access memory that belongs to other programs or the operating system.
  - A virtual machine (or a container) is a domain that is separate from other virtual machines (or containers)


- Implications
  - Crossing domain boundaries requires access control. Transactional overhead and maintenance of access control rules are side-effects.
  - Stakeholders should negotiate the level of granularity at which domains require separation.


- Related principles
  - Process isolation
  - Resource encapsulation
  - Layering
  - Abstraction

#### 2. Process Isolation

- What is a Process?
  - A `process` is a program running on a computer. Each process has a region of the memory (address space), which only it can access.  
  - Isolating the process address space from other address spaces prevents tampering or interference from/by other processes.


- Examples
  - A word processor, a database, and a browser running on a computer are all running in different addresses spaces. Process isolation ensures that each one cannot influence the others address space.
  - A non-technical example of process isolation is when a prosecutor and defense attorney run their cases in court. It would be a problem if either had access to each other's work. Keeping their work seperate protects it from misuse by the other party.


- Implications
  - Processes have to use defined communications mediated by the operating system to communicate with other processes.
  - A process should never trust any other process on the computer.


- Related principles
  - Domain separation
  - Resource encapsulation

#### 3. Resource Encapsulation

- What is a Resource?
  - A computer has many resources. A `resource` can be the memory, disk drive, network bandwidth, battery power, or a monitor. It can also be system objects such as shared memory or a linked list data structure.


- What is encapsulation?
  - `Encapsulation` finds its origin in object-oriented programming (OOP). In OOP, a class definition encapsulates all data and functions to operate on the data. The goal is to allow access or manipulation of the class data in only the ways the designer intended.


- Examples
  - The application logic of a website only allows access and manipulation of database records in defined ways. Here the database is a resource encapsulated by the website application logic.
  - A flag pole only allows certain operations (raise the flag, lower the flag, unhook the flag). No one needs to know how the flag pole works internally, just that they can use it only in certain ways.


- Implications
  - Programs or users have to be aware of the interface for the resource and only communicate with it in a defined manner.


- Related principles
  - Domain separation
  - Process Isolation
  - Modularization
  - Abstraction


#### 4. Least Privilege

- What is a privilege?
  - In a computer, a `privilege` is a right for the user to act on managed computer resources.


- Why should privileges be minimized?
  - Minimizing the number of privileges granted to a user for accomplishing assigned duties improves accountability and limits accidental misuse. The operating system must also disable privileges when not required.


- Examples
  - When a person gets a new computer, they install or log onto it using an administrative account. This account has privileges to install software, add users, add hardware, and add and delete almost any program or file. Now, if the person opens a malicious phishing attachment, the malware will run with administrative privileges. Instead, if the person lowered their privileges to a regular user immediately after the initial installation is over, the malware would not be able to acquire administrative privilege.
  - If a user doesn't need a permission, why give it to them? Should a military radio operator have permission to access a nuclear silo?


- Implications
  - The operating system may frequently prompt users to elevate their privilege for tasks that have high consequences, such as installing software or deleting a system file.


- Related principles
  - Minimization

#### 5. Layering

- What is a Layer?
  - In the context of computer security, a `layer` is a separate level that must be conquered by an attacker to breach a system.
  - Layering slows down an attacker. The attacker needs to conquer each layer before moving on to the next.


- Examples
  - A moat is an outer layer that protects a castle. The next layer that an intruder has to go through is the high walls. All of this has to be done by the intruder while avoiding the watchful guards. Finally, the intruder needs to scale the inner walls before getting to the king's treasure.
  - Firewall, intrusion detection systems, internal encryption, access control and personnel controls are examples of layers typically employed to protect enterprise data and programs.


- Implications
  - Multiple independent layers require separate management and integration to get the full benefits of layered protection.


- Related principles
  - Domain separation
  - Resource encapsulation
  - Abstraction
  - Data Hiding


#### 6. Abstraction

- What is abstraction?
 - `Abstraction` is the concept that something complicated can be thought of and represented more simply. All models are abstractions - since they reduce the complexity of an object into something that is understandable.



- How does abstraction contribute to cybersecurity?
  - Remove/reduce any clutter that can distract the user or programmer from using a resource correctly.  
  - Only provide the necessary details, while reducing the complexity to a set of essential characteristics.
  - Excess complexity may hide malicious behaviors.


- Examples
  - The gauges in a car are an abstraction of the car's performance.
  - A map is an abstraction of an area.
  - A model airplane is an abstraction of a real airplane and may be used to test aerodynamics.


- Implications
  - Different users/roles may need different abstractions.


- Related principles
  - Layering
  - Data Hiding
  - Resource encapsulation


#### 7. Data Hiding

- How does data hiding contribute to cybersecurity?
  - Only allow necessary aspects of a data structure or a record to be observed or accessed. Log all access attempts.


- Examples
  - A stack data structure exposes only the data at the top of the stack using simple push and pop instructions. The operating system applies access control to different regions of the stack.
  - Websites don't need to load all of a user's data to show a list of usernames - they only need the username, the rest of the record fields can be hidden.


- Implications
  - Programmer or user frustration if allowed access is not sufficient to carry out the task.


- Related principles
  - Resource encapsulation
  - Abstraction

#### 8. Modularity

- What is modularity?
  - `Modulatiry` is a design technique that separates the functionality of a program into independent, interchangeable components.
  - Each component/module is self-sufficient and capable of executing a unique part of the desired functionality through well-designed interfaces.


- How does modularity contribute to cybersecurity?
  - Modules can be mutually-untrusting
  - Compartmentalization is possible using modularization. It contains damage to a single module.
  - Using modules means that you can swap out a bad part. If batteries weren't modules, any time a battery died you would need to throw out the entire electronic device it was in.


- Examples
  - Electronic circuits.
  - Lego blocks.
  - Network nodes.


- Implications
  - Well defined interfaces allow a system designer to replace one module with another.
  - Prevents vendor lock-in
  - Encourages re-use of well designed modules by other modules.


- Related principles
  - Domain separation
  - Process isolation
  - Resource encapsulation
  - Abstraction



#### 9. Simplicity

- How does simplicity contribute to cybersecurity?
  - The lack of complexity allows system designers and programmers to identify unwanted access paths.
  - Users can easily translate their general protection goals to appropriate system security configurations.


- Examples
  - Interface designs that allow correct application of security features.
  - Intuitive and straightforward access control rules
  - Easy to follow and maintain program statements.


- Implications
  - Testers will be able to cover all possible combinations and spot problems sooner.
  - Simplicity may feed aspirations to add complexity!


- Related principles
  - Abstraction
  - Minimization


#### 10. Minimization

- What is minimization?
  - Having the least functionality necessary in a program or device


- How does minimization contribute to cybersecurity?
  - Decrease the number of ways in which attackers can exploit a program or device.


- Examples
  - Turn off unnecessary features.
  - Block unnecessary ports using a firewall.
  - Reduce the amount of code.


- Implications
  - Expanding feature sets in future versions can be difficult.
  - Reduce test combinations.


- Related principles
  - Simplicity
  - Abstraction

### CIA Triad - Expectations of Information

#### Confidentiality
It is an expectation for the entity entrusted with data (or code) to keep it a secret. For example, if a healthcare provider is entrusted with patient data, the user expects the health care provider to keep it secret.

#### Integrity
It is an expectation for the entity entrusted with data (or code) to only allow authorized modifications to it. For example, only authorized individuals are allowed to make changes to an employee's salary.   

#### Availability
It is an expectation for the entity entrusted with data (or code) to allow access to it when needed. For example, the personnel records in a database are available when needed.   

## Card Game

The Cyber Realm card game helps teach the 10 principles of cybersecurity. The cards reinforce the 10 principles using hand gestures, or by playing single person or group games.

Split in groups of 4 or less. Hand two cards decks to each group.

#### Game 1: Question Cards
- STEP 1: Ask the groups to further split their team into two sub-groups. Give each sub-group a card deck. Students in the sub-groups take turns to examine the cards with first principles on it.
- STEP 2: Use question cards (cards 1-20) of the one of the sub-group's decks as the question stack.
Shuffle these cards and place them face down in a stack to the left of sub-group 1.
- STEP 3: Turn a question card over
- STEP 4: Both sub-groups read the question and then place what they think the correct principle card is _face down_.
- STEP 5: When both sub-groups have placed the card down, then both can turn over their cards at the same time.
- STEP 6:
> - If both sub-groups picked the same principle they will put that question card face up to the right of the turned up question card area.  
> - If the principles don't match, the two sub-groups discuss and reach consensus. The sub-groups may invite the instructor if the mismatch cannot be resolved.

- Repeat steps 3 – 6 for all question cards

#### Game 2: Cybersecurity Matrix

- STEP 1: Have each sub-group identify and examine the following cards
> Cards 22, 23, 24 are the expectations of information  
Cards 25, 26, 27 are the information states

- STEP 2: Arrange these two sets of cards into an matrix as shown in the diagram below

![array](https://gencybercards.com/wp-content/uploads/2017/06/d1.jpg)

- STEP 3: Have each sub-group identify and examine the following cards
> Cards 31 – 39

- STEP 4: Now ask each sub-group to arrange the cards 31-39 as examples that fit at the cross section of the cards in the row and column. In the example below – Card 31 “Javier’s Concern” indicates that he wants to encrypt his hard drive. As such it is put in the first row first column since it cross references storage (hard drive) and encryption (confidentiality).
> Ask students to place cards in a Round Robin fashion. Internally discuss and resolve any disagreements. Each team must put all 9 cards down in the matrix within 5 minutes.

- STEP 5: Ask the sub-groups to share their solution. Discuss and resolve any disagreements raised by between the sub-groups using your answer key.  

- Now ask the sub-groups to replace the `states of information` cards with the following cards that represent information countermeasures
> Cards 28, 29, 30 are information countermeasures  

- Repeat above steps

- Now create a matrix for characteristics of information  vs. information countermeasures

- Repeat steps 4 and 5

#### Game 2 Solution

*Combo 1: States vs Characteristics*

| **Game 1**              | *22* Confidentiality (C)                     | *23* Integrity (I)                                 | *24* Availability (A)                             |
|-------------------------|----------------------------------------------|----------------------------------------------------|---------------------------------------------------|
| **25 Storage (S)**      | **31** `Encryption` (C) `Hard Drive` (S)       | **36** `altered by anyone` (I) `backups` (S)         | **38** `files` (S) `finding files` (A)              |
| **26 Transmission (T)** | **32**  `send email` (T) `no one can read` (C) | **34** `digital signature` (I) `email` (T)           | **39** `email` (T) `disaster recovery` (A)          |
| **27 Processing (P)**   | **33** `compute` (P) `secrecy` (C)             | **35** `CPU calculations` (P) `incorrect values` (I) | **37** `slow and freezes` (A) `run application` (P) |


*Combo 2: States vs. Countermeasures*

| **Game 2**              | *28* Education (E)                     | *29* Policy (Po)                      | *30* Technology (Te)                              |
|-------------------------|----------------------------------------|---------------------------------------|---------------------------------------------------|
| **25 Storage (S)**      | **38** `files` (S) `training` (E)        | **36** `rules` (Po) `backups` (S)       | **31** `hard drive` (S) `AES encryption` (Te)       |
| **26 Transmission (T)** | **32**  `send email` (T) `unsure` (E)    | **39** `recovery plan` (Po) `email` (T) | **34** `email` (T) `digital signature` (Te)         |
| **27 Processing (P)**   | **35** `compute` (P) `reads article` (E) | **33** `compute` (P) `rule` (Po)        | **37** `powerful device` (Te) `run application` (P) |

*Combo 3: Characteristics vs. Countermeasures*

| **Game 3**                 | *28* Education (E)                        | *29* Policy (Po)                                              | *30* Technology (Te)                                 |
|----------------------------|-------------------------------------------|---------------------------------------------------------------|------------------------------------------------------|
| **22 Confidentiality (C)** | **32** `unsure` (E) `no one can read` (C)   | **33** `secrecy` (C) `rules` (Po)                               | **31** `sensitive data` (C) `AES encryption` (Te)      |
| **23 Integrity (I)**       | **35**  `incorrect` (I) `reads article` (E) | **36** `not altered` (I) `rules` (Po)                           | **34** `digitally signed` (Te) `digital signature` (I) |
| **24 Availability (A)**    | **38** `find files` (A) `training` (E)      | **39** `constant email communications` (A) `recovery plan` (Po) | **37** `powerful device` (Te) `slow and freezes` (A)   |

If there is a question as to where the card should be placed the answer is on the card – encrypted. For example on card 31 the lower right hand has the code XON21. This code is a simple rotation cipher and it rotated 21. You will get a three letter answer. In this case it will be CTS. The first letter will be either C, I, or A for Confidentiality, Integrity, Availability. The second letter will be P, E, or T for safeguards – Policy, Education or Technology. The third letter will be S, T or P for states – Storage, Transmission or Processing. In this case the answer is C for Confidentiality, and S for Storage.


## A test of your principles...

[Quiz](https://unomaha.az1.qualtrics.com/jfe/form/SV_eVbcBA7Pk0VqD7D)

## Additional Resources

- [NSA document listing Cybersecurity first principles](https://users.cs.jmu.edu/tjadenbc/Bootcamp/0-GenCyber-First-Principles.pdf)
- [First Principle Hand Gestures](https://gencyber.utulsa.edu/wp-content/uploads/2016/10/10-Principles-GenCyber-Card-Game.pdf)


[Top](#table-of-contents)

## Lead Author

- Robin Gandhi

## Acknowledgements

- A special thanks to Matt Hale for reviews of this module and thoughtful discussions.

[Top](#table-of-contents)

## License
[Nebraska GenCyber](https://github.com/MLHale/nebraska-gencyber) <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Overall content: Copyright (C) 2017-2018  [Dr. Matthew L. Hale](http://faculty.ist.unomaha.edu/mhale/), [Dr. Robin Gandhi](http://faculty.ist.unomaha.edu/rgandhi/), [Dr. Briana B. Morrison](http://www.brianamorrison.net), and [Doug Rausch](http://www.bellevue.edu/about/leadership/faculty/rausch-douglas).

Lesson content: Copyright (C) [Robin Gandhi](http://faculty.ist.unomaha.edu/rgandhi/) 2018.  
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">This lesson</span> is licensed by the author under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
