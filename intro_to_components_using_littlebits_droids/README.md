# Intro to Components using Littlebits Droids

### Cybersecurity First Principles in this lesson

* __Abstraction__: An abstraction is a representation of an object or concept. It could be something such as a door, a speedometer, or a data structure in computer science. Abstraction decouples the design from the implementation. The gauges in an automobile are an abstraction of the performance of a car. A map is an abstraction of the earth.

* __Modularization__: The concept of modularity is like building blocks. Each block (or module) can be put in or taken out from a bigger project. Each module has its own separate function that is interchangeable with other modules.

* __Simplicity__: Simplicity allows a person to better understand hardware and software. Without the clutter of unnecessarily complicated code and interfaces, the software will be more understandable by people that will update the code when requirements change. It will be easier to understand by the testers and they will be able to spot problems sooner. By keeping software as simple and as focused as possible, the reliability and security is greatly increased.

### Introduction
In this lesson, we will learn about components and how to solve a problem by decomposing it into sub-problems. We will also explore a cool hands-on technology called [Littlebits](http://littlebits.cc/). Littlebits follows a _component-based design_ paradigm using _GPIO_ (or general purpose input/output) to let you easily make apps. We will learn how to plug and play bits together to make some simple inventions. Littlebits is used as an enabling technology platform and is used in many other lessons.

### Goals
By the end of this tutorial, you will be able to:
* Understand and be able to describe `modularity`
* Use components to solve a problem
* Decompose a problem into smaller problems
* Use Littlebits and GPIO to make your first (or another) IoT app

### Materials Required

* [Littlebits Droid Inventor Kit](https://shop.littlebits.com/products/droid-inventor-kit)
* [Number bit](https://shop.littlebits.com/products/number-bit)
* [LED bit](https://shop.littlebits.com/products/led)
* [Sound trigger bit](https://shop.littlebits.com/products/sound-trigger)
* [Temperature sensor bit](https://shop.littlebits.com/products/temp-sensor)
* [Button bit](https://shop.littlebits.com/products/button)
* [Wire bit](https://shop.littlebits.com/products/wire-bit)
* [USB power bit](https://shop.littlebits.com/products/usb-power)
* [Rechargable battery pack](https://shop.littlebits.com/products/rechargeable-battery)

### Prerequisite lessons
None

### Table of Contents
<!-- TOC START min:1 max:3 link:true update:true -->
- [Intro to Components using Littlebits Droids](#intro-to-components-using-littlebits-droids)
    - [Cybersecurity First Principles in this lesson](#cybersecurity-first-principles-in-this-lesson)
    - [Introduction](#introduction)
    - [Goals](#goals)
    - [Materials Required](#materials-required)
    - [Prerequisite lessons](#prerequisite-lessons)
    - [Table of Contents](#table-of-contents)
    - [Step 1: Unbox it!](#step-1-unbox-it)
    - [Step 2: Gotta start somewhere](#step-2-gotta-start-somewhere)
    - [Step 3: Count all the things!](#step-3-count-all-the-things)
    - [Step 4: The world is more than True or False - Variable Inputs](#step-4-the-world-is-more-than-true-or-false---variable-inputs)
    - [Step 5: Hey, Listen - Audio](#step-5-hey-listen---audio)
    - [Step 6: Turning on an outlet with the IR transmitter](#step-6-turning-on-an-outlet-with-the-ir-transmitter)
    - [Step 7: Motoring onward](#step-7-motoring-onward)
    - [Self Exploration](#self-exploration)
    - [Test Your Bits, err... Wits!](#test-your-bits-err-wits)
    - [Additional Resources](#additional-resources)
    - [Acknowledgements](#acknowledgements)
    - [License](#license)

<!-- TOC END -->

### Step 1: Unbox it!
First, open your Littlebits box. Take a second to look at the different components you have. Littlebits is organized around three colors:

* **<span style="color: pink">Pink</span>** modules are _inputs_, like an On/Off button.
* **<span style="color: green">Green</span>** modules are _outputs_, like LEDs and Fans.
* **<span style="color: orange">Orange</span>** modules are special and usually are _supportive_ - think splitters and logic handlers.
* **<span style="color: blue">Blue</span>** modules are power related.

Look over each module. Your kit should include all of these parts:

![unbox](./img/box-contents.jpg)
> Note: Dog not included!

![unbox](./img/droid-kit.jpg)

### Step 2: Gotta start somewhere
No time like the present. Before we get into the droid, lets start with the basics to make a simple invention:

* find the blue ```power``` module.
* find the pink ```button``` input module
* find the green ```led``` output module

Lets make a simple circuit:

* Connect micro USB end to the ```power``` module and plug up to a computer or the `battery`
* Connect the ```button``` to the ```power``` module
* Connect the ```led``` to the ``` button```.

![unbox](./img/simple-circuit.jpg)

Press the button and the light turns on. That was easy!

This is `GPIO` in a nutshell. Each module has a general purpose input and output, with a standard interface, and **doesn't need to understand or know anything about what they are connected to**. These modules also need to protect themselves from invalid input. This is a great example of the `modularity` cybersecurity first principle.

### Step 3: Count all the things!
Ok, we've made our first circuit - but it's pretty simple. Let's add some more modules:

* Find the green ```o21 number``` output module

Time to extend your previous circuit to ![count](./img/count-all-the-things.jpg)

* Connect the ```o21 number``` to the ```bright led```
* Set the switch to the up position on the ```o21 number``` module. This puts it into **count** mode instead of **voltage** mode.

Press the button!

Pretty simple. Notice we can **chain the output modules together** (```bright led``` and a ```counter``` in this case). Any number of output modules can be chained together.

Now, lets switch up our circuit a bit.

* Find the pink ```sound trigger``` input module
* Find the pink ```light sensor``` input module

Lets swap some components around.

* Remove the ```bright led``` module (it is really bright!)

Press the button. Everything still works!

* Connect the ```light sensor``` to the ```power``` and then to the ```button```

Press the button. Does it work? How about if you cover up the light sensor?

This shows you that you can also **chain multiple input modules together** and their **total behavior is a combination of their input designs**. In this case, our counter only worked if the light was detected **AND** the button was pressed.

Lets try one more combo:

* Remove the ```button``` module.
* Remove the ```light sensor``` module.
* Connect the ```sound trigger``` between the ```power``` and the ```o21 number``` module.

Snap your fingers or tap the table near your device.

![unbox](./img/sound-counter.gif)

### Step 4: The world is more than True or False - Variable Inputs
So far, we have outputs and inputs that result in an **on** (True) or **off** (False) behavior.

![grey](./img/grey-world.jpg).

The world is not always **on** or **off**

* Find the pink ```temperature sensor``` input module.
* Get the ```light sensor``` and ```led``` out again

We are going to make a circuit that shows off variable voltage.

* Remove all components.
* Connect the ```temperature sensor``` to the ```o21 number``` module.
* Set the ```o21 number``` switch to **value** (middle position)
* Set the ```temperature sensor``` switch to **f** (for Fahrenheit)

You should see the current temperature in the room near the device.
![temperature](./img/temperature.jpg)


* Replace the ```temperature sensor``` with the ```light sensor```
* Put the ```o21 number``` module back into **voltage** mode by moving the switch to the bottom position.
* Move your finger closer to and further away from the light sensor

You should see that the more light it gets, the more voltage it outputs.

* Now connect the ```led``` to the right-hand side of the ```o21 number``` module
* Move your finger closer to and further away from the light sensor

You should notice the light dimming and brightening depending on the voltage it receives.

### Step 6: Motoring onward
We've saved the best for last. It is time to unbox and open up your droid! There are a lot of parts, but we Littlebits provides some nice `missions` to walk students through each of them.

* Open droid inventor box
* Install [Littlebits Droid Inventor App](https://littlebits.com/app) on your phone or tablet.
* Complete Missions 1-9, 13

### Self Exploration
Try some different designs yourself.

### Test Your Bits, err... Wits!
[Quiz](https://www.qzzr.com/c/quiz/430545/all-about-littlebits-introduction)

<div class="quizz-container" data-width="100%" data-iframe-title="QUIZ: All About Littlebits - Introduction" data-height="auto" data-quiz="430545"></div>

### Additional Resources
For more information, investigate the following:

* [Littlebits](http://littlebits.cc/how-it-works) - Overview of concepts and available bits
* [https://shop.littlebits.cc/products/smart-home-kit](https://shop.littlebits.cc/products/smart-home-kit) - Information about the Smart Home Kit

### Acknowledgements
Special thanks to [Dr. Robin Gandhi](http://faculty.ist.unomaha.edu/rgandhi/) for reviewing and editing this lesson.

### License
[Nebraska GenCyber](https://github.com/MLHale/nebraska-gencyber) <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Overall content: Copyright (C) 2017-2018  [Dr. Matthew L. Hale](http://faculty.ist.unomaha.edu/mhale/), [Dr. Robin Gandhi](http://faculty.ist.unomaha.edu/rgandhi/), [Dr. Briana B. Morrison](http://www.brianamorrison.net), and [Doug Rausch](http://www.bellevue.edu/about/leadership/faculty/rausch-douglas).

Lesson content: Copyright (C) [Dr. Matthew L. Hale](http://faculty.ist.unomaha.edu/mhale/) 2017.  
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">This lesson</span> is licensed by the author under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
