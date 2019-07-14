---
layout: page
title: Introduction to Computational thinking and design process 
---

### Cybersecurity First Principles in this lesson

* __Abstraction__: An abstraction is a representation of an object or concept. It could be something such as a door, a speedometer, or a data structure in computer science. Abstraction decouples the design from the implementation. The gauges in an automobile are an abstraction of the performance of a car. A map is an abstraction of the earth.

* __Modularization__: The concept of modularity is like building blocks. Each block (or module) can be put in or taken out from a bigger project. Each module has its own separate function that is interchangeable with other modules.

* __Resource Encapsulation__: Encapsulation is an object oriented concept where all data and functions required to use the resource are packaged into a single self-contained component. The goal is to only allow access or manipulation of the resource in the way the designer intended. An example, assume a flag pole is the object. There are fixed methods on how the flag pole is to be used. Put the flag on, take the flag off, raise or lower the flag. Nothing else can be done to the flag pole.

* __Simplicity__: Simplicity allows a person to better understand hardware and software. Without the clutter of unnecessarily complicated code and interfaces, the software will be more understandable by people that will update the code when requirements change. It will be easier to understand by the testers and they will be able to spot problems sooner. By keeping software as simple and as focused as possible, the reliability and security is greatly increased.

### Introduction
In this lesson, we will learn how components can be used to solve a problem by decomposing it into sub-problems. We will also learn about how the `design process` can be applied to imagine a problem, think about different solutions, and then iteratively make attempts to solve it - getting better solutions at each iteration. 

### Goals
By the end of this tutorial, you will be able to:
* express the key steps of the design process
* conceptualize and decompose a problem into smaller sub-problems
* come up with implementation ideas and test them

### Materials Required

* paper
* tape (optional)

### Prerequisite lessons
None

### Table of Contents
<!-- TOC -->
- [Cybersecurity First Principles in this lesson](#cybersecurity-first-principles-in-this-lesson)
- [Introduction](#introduction)
- [Goals](#goals)
- [Materials Required](#materials-required)
- [Prerequisite lessons](#prerequisite-lessons)
- [Table of Contents](#table-of-contents)
- [The Design Process](#the-design-process)
  - [Empathizing and Defining](#empathizing-and-defining)
    - [Some processes for empathizing and defining the problem](#some-processes-for-empathizing-and-defining-the-problem)
    - [Exercise:](#exercise)
  - [Ideating](#ideating)
    - [Exercise:](#exercise-1)
  - [Prototyping and Testing](#prototyping-and-testing)
- [Exercise: Apply design thinking to solve a problem](#exercise-apply-design-thinking-to-solve-a-problem)
  - [Empathize and Define](#empathize-and-define)
  - [Ideate](#ideate)
  - [Prototype](#prototype)
  - [Test](#test)
- [Reflection and takeaways](#reflection-and-takeaways)
- [Additional Resources](#additional-resources)
- [Lead Author](#lead-author)
  - [Acknowledgements](#acknowledgements)
  - [License](#license)

<!-- /TOC -->

### The Design Process
Design is about more than sitting down and starting to code or building something. In the real world when faced with a complex problem, companies, and individuals need a systematic process to think about the problem, consider all of the stakeholders and come up with a solution. In this lesson, we examine a 5-step `design thinking process` created by the [Hasso-Plattner Institute of Design at Stanford](https://dschool.stanford.edu/). Their process is iterative and non-linear.

![design process](./img/design-process.jpg)
> Author/Copyright holder: Teo Yu Siang and Interaction Design Foundation. Copyright licence: CC BY-NC-SA 3.0

#### Empathizing and Defining
I group these two stages together as they are very iterative. 

![design process](./img/empathize.jpg)
> Author/Copyright holder: Teo Yu Siang and Interaction Design Foundation. Copyright licence: CC BY-NC-SA 3.0

Before trying to solve a problem, one must understand it. Complex real-world problems involve more than one stakeholder. If you are trying to design software, for instance, you need to be cognizant of _all_ of your users, not just some of them. `Implicit bias` (where problem solvers accidentally leave some users out) can be a real issue if problem solvers don't `empathize` with their users. In this sense, empathizing is the part of the design process where we observe and study our user base, build `user stories` that describe who our users are and what they want to do with our product, and then make sure we have coverage across our user population. Empathy is also important for **setting aside our assumptions** so that our product can meet the needs our users and not ourselves.

![design process](./img/define.jpg)
> Author/Copyright holder: Teo Yu Siang and Interaction Design Foundation. Copyright licence: CC BY-NC-SA 3.0

After we have gathered some data about our users and empathically considered their perspective, we can begin to `define` the problem. It should be noted that the `define` stage is not done once we initially define the problem. We will keep returning to the problem statement as we test our potential solutions. With definition, we want to make problem assumptions clear and define the requirements for any potential solution. 

##### Some processes for empathizing and defining the problem
A good technique for empathizing and defining the problem is `affinity diagramming`. This technique helps development teams consider multiple perspectives and is a great process to use with groups of users from the target population.

For affinity diagramming, you need some sticky note cards, a few ink pens or markers, and a few questions. The questions get posed to the group. Individuals in the group think up their answers and write them on the note cards, and then the facilitator goes note by note and the group decides how to categorize the notes. No note is bad.

This can produce some interesting categories that help define and contextualize the problem. 

`User stories` are another useful technique for contextualizing a problem. User stories are used pretty extensively in software design and development - particularly in teams using a process called `Agile`.

A user story is generally written as:

As a `type of user`, I want to `some action`, so that I can `rationale`.

an example would be:

As a `instagram user in high school`, I want to `post pictures of myself and my friends`, so that I can `build my social status at school`.

This may create very different requirements that a different kind of instagram user with different actions and rationales, e.g.

As a `company on instagram`, I want to `post pictures of my products`, so that I can `build brand recognition`.

Both statements help define requirements for any potential solution.

##### Exercise:
* Read [https://www.mountaingoatsoftware.com/blog/advantages-of-the-as-a-user-i-want-user-story-template](https://www.mountaingoatsoftware.com/blog/advantages-of-the-as-a-user-i-want-user-story-template)
* Read [https://uxdict.io/design-thinking-methods-affinity-diagrams-357bd8671ad4](https://uxdict.io/design-thinking-methods-affinity-diagrams-357bd8671ad4)
* try it

#### Ideating
Once we can begin to stabilize the problem definition, we can start zoning in on solutions. The `ideation` phase is very important to help us find as many possible solutions to the problem as possible - so that we can pick the best one. Often times, computer scientists and developers **don't ideate enough** before jumping into development. This can lead to some myopic focus on one particular design - that might be _bad_. 

When ideating, there are several techniques you can use to come up with good ideas.

One is obviously `brainstorming` - where the team sits around a table and thinks up different ideas to address the problem. Brainstorming is great, but it is better applied as a second step. 

First, a technique called `worst possible idea` is a good starting place. The worst possible idea process, seems counter-intuitive to solving a problem, but it is a helpful exercise. Here, participants come up with the absolute worst solutions to a problem that they can think of. Bad solutions are considered for _why_ and _how_ they are bad - to list out all the reasons. 

Going through this process, the group begins to get a notion of the **solutions to avoid**. This is a great time to introduce brainstorming. The group can start to frame new ideas in terms of how they avoid the mistake and pitfalls of the bad ideas. This can help break down team-dynamics barriers that often emerge whenever a particular team member becomes _attached_ to their particular idea.

##### Exercise:
* Read [https://www.interaction-design.org/literature/article/learn-how-to-use-the-best-ideation-methods-worst-possible-idea](https://www.interaction-design.org/literature/article/learn-how-to-use-the-best-ideation-methods-worst-possible-idea) (~5 min read)
* try it

![design process](./img/ideate.jpg)
> Author/Copyright holder: Teo Yu Siang and Interaction Design Foundation. Copyright licence: CC BY-NC-SA 3.0

#### Prototyping and Testing
![design process](./img/prototype.jpg)

Prototyping is the stage where you start making. `Prototypes` should not be full-fledged at the beginning. Since we aren't always sure if an idea coming out of the ideation stage is really going to work, we don't want to spend too much time on it at first. Prototypes can help to identify whether or not an idea will pan out. Often prototypes lead to new ideas - because different members of a team begin to bounce ideas off one another to create better ones.

As you progress, prototypes need to be `tested.` 

![design process](./img/test.jpg)
> Author/Copyright holder: Teo Yu Siang and Interaction Design Foundation. Copyright license: CC BY-NC-SA 3.0

Testing a prototype helps us to learn whether or not it succeeds (i.e. does it meet the requirements of the problem) and can help to refine the definition of the problem - if we learn something about the problem that we hadn't thought of before. 

### Exercise: Apply design thinking to solve a problem 
The problem: Create a paper airplane that can fly 10 feet.  
#### Empathize and Define

You have two stakeholders, yourself (as a camper) and me as an instructor. 

My user story is:
As an instructor, I want students to test their airplanes in the hall, so that the technology in the room doesn't get broken. 

What is your user story? Write it in the workbook in the `empathize` box.

What are the core attributes of the problem? Write what you think they are in the workbook in the `define` section.

#### Ideate
Use the worst possible idea method to think about some designs that wouldn't work well. Once you've ruled some out, brainstorm and draw a diagram (an abstraction) of your proposed solution. Use the `ideate` section of your workbook.

#### Prototype 
Use the sheet of paper you are given to create a basic prototype of the design you came up with. Write down your thoughts after building it. How do you think it will work?

#### Test 
Test your prototype airplane by flying it in the hallway. How far did it fly? What other information would be useful to gather in your tests? How would you use this information to improve your design if you were to build a new prototype? Write down your answers and thoughts in the workbook in the `test` section. 

### Reflection and takeaways
The design process is useful for conceptualizing a problem and exploring different solutions that meet all of your user's needs or meet the requirements of the problem. Often, breaking a problem down into subproblems can help you tackle complex issues. Components can be used in more than one way for more than one purpose. This leads to `reuse` and is a positive side effect of `modularization` and `resource encapsulation`.

### Additional Resources
For more information, investigate the following:

* [Advantages of User stories](https://www.mountaingoatsoftware.com/blog/advantages-of-the-as-a-user-i-want-user-story-template)
* [Affinity diagramming process](https://uxdict.io/design-thinking-methods-affinity-diagrams-357bd8671ad4)
* [Worst Possible ideas](https://www.interaction-design.org/literature/article/learn-how-to-use-the-best-ideation-methods-worst-possible-idea)

## Lead Author

- Matt Hale

### Acknowledgements
This lesson was inspired and informed by a [blog post](https://www.interaction-design.org/literature/article/5-stages-in-the-design-thinking-process) written by Rikke Dam and Teo Siang. Materials in this lesson are used consistent with their CC-v3 license.

### License
[Nebraska GenCyber](https://www.nebraskagencyber.com) <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Overall content: Copyright (C) 2017-2019  [Dr. Matthew L. Hale](http://faculty.ist.unomaha.edu/mhale/), [Dr. Robin Gandhi](http://faculty.ist.unomaha.edu/rgandhi/), and [Dr. Briana B. Morrison](http://www.brianamorrison.net).

Lesson content: Copyright (C) [Dr. Matthew L. Hale](http://faculty.ist.unomaha.edu/mhale/) 2019.  
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">This lesson</span> is licensed by the author under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
