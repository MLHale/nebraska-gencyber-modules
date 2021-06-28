---
layout: page
title: Internet of Strings
---

# Hands-on IoT: Internet of Strings

### Cybersecurity First Principles in this lesson

* __Modularization__: The concept of modularity is like building blocks. Each block (or module) can be put in or taken out from a bigger project. Each module has its own separate function that is interchangeable with other modules.

* __Abstraction__: An abstraction is a representation of an object or concept. It could be something such as a door, a speedometer, or a data structure in computer science. Abstraction decouples the design from the implementation. The gauges in an automobile are an abstraction of the performance of a car. A map is an abstraction of the earth.

### Introduction

In this module, you will learn the roles of the components of a digital network.

### Materials

* Index cards
* Paper to make labels
* Blue painters' tape
* Envelopes
* Post-it notes (for MS/HS version)

### Preparation
#### For a class of 30 kids (can be modified for other class sizes)

* Label 4 envelopes with “From: Computer 1, To: Computer 2”. Label the next 4 with “From: Computer 2, To: Computer 3”. Label the last 4 with “From: Computer 3, To: Computer 1”.
* Write 4-word phrases on the index cards - one word per index card.
* Create labels for computers, routers, and TCP for the floor network map. Give each computer & router a number (e.g. "Computer 1", "Router 1").
* Create a map on the ground using the blue tape and labels, using the map below as reference or creating your own.\*

\* If running the MS/HS version, the routing tables are only compatible with the given floor network map, so you will have to create your own routing tables if you modify the map.

### Warm-up Activity

Host a discussion on routing tables and how packets travel over a network after watching [this video](https://www.youtube.com/watch?v=AYdF7b3nMto).

## Activity Instructions

***Role Assignments***
* `Computer`: The computers are responsible for giving packets their messages and declaring the received message once the TCP verifies it.
* `TCP`: The TCP is responsible for verifying packets when they arrive, organizing the messages from verified packets, and relaying that message to the computer.
* `Packet`: The packets are responsible for delivering their message from an originating computer to its destination.
* `Router`: The routers are responsible for directing packets on the quickest route to their destination computer. 

1. Assign 3 kids as `computers`, 3 as `TCP`, 12 to hold `packets` (4 at each computer), and 12 as `routers`.
2. Originating computers each hold 4 papers (when the papers are put together, they make a phrase). Packets each hold an envelope.
3. When the game starts, originating computers put one piece of the phrase in each packet’s envelope.

#### Activity Process

* Once packets receive the "message" from their computer, they start to travel the network lines (the blue tape). Encourage them not to travel together. 
* When they arrive at a router, the router directs the packets on the quickest route to its destination. 
* If a packet collides with another packet, return the packet to the router it came from, wait 10 seconds before going to the next hop again.
* When a packet arrives at its destination, TCP must verify that it arrived at the correct computer by checking the envelope. It then informs the computer, and the computer must yell “Packet Received!”
* When all packets have been received and TCP has put them in the correct order, the receiving computer must yell the phrase. 
* <b>To increase difficulty:</b> While the game is in process, cut random network lines (break the tape between two routers) and declare that line "Out of Service". The routers must adapt to find the quickest available route without that line.

#### Continued Activity Process (MS/HS Level)

If you are the first router to receive this packet
1. Refer to your node's routing table and select the least cost route to final destination.
2. Build packet header on post-it note (see below) and place on packet envelope.
3. Move to the next hop.

***Packet Header Format (for MS/HS version)***: Each post-it note packet header should contain the following information:

<ul>
 
    Source: computer the message started at
    Destination: computer the message should travel to
    Next Hop: next router to travel to
    
</ul>

<br>

*When you arrive at a router:*
1. Review packet header and determine if message is for the router you are at.
    - If message is for this router, announce results, either "message received" or "message misrouted".
    - If message is not for this router, hand packet to next individual and continue with step 2 below.

2. Refer to the current node's routing table and select the least cost route to final destination
    - If there is no route to final destination announce "bad route" and go to the end of the line for that router.
    - If there is a route but the link you need is not available.
      - Check to see if there is a higher cost route available.
      - If there is a higher cost route use it and continue with number 3.
      - If there is not a higher cost route announce "link down".
      
3. Build new packet header by adding a new next hop and place on packet

*If you are moving to the next hop and collide with another packet:*
1. Return to the router you came from
2. Wait 10 seconds before going to the next hop again.

<br>
<br>

### Closure

Provide a 5 minute warning when the activity will end. Once complete, have all the students help put away the supplies.

### Reflection

Once the activity is over, host a discussion on how this activity translates to networking routing.

### Optional Alterations

-	If class is slightly larger/smaller than 30, simply get rid of as many router spots as needed. 
-	If class is significantly larger/smaller than 30, add or remove a computer; or change the length of the phrases at each computer.
-	To play outside, set up the game using chalk or use string/yarn as the network lines.

## Reference Materials

#### Floor Network Map

<img width="1142" alt="IoS Map" src="https://user-images.githubusercontent.com/86324276/123014494-ff2d3600-d38b-11eb-92cd-904ecf8e65a7.png">

#### Node Routing Tables

<img width="300" alt="node1" src="https://user-images.githubusercontent.com/86324276/123000325-0f85e680-d375-11eb-9164-1645eeeedb57.png"> 
<img width="300" alt="node2" src="https://user-images.githubusercontent.com/86324276/123000814-a488df80-d375-11eb-814b-ccf0b0f5c81b.png"> 
<img width="300" alt="node3" src="https://user-images.githubusercontent.com/86324276/123000859-b23e6500-d375-11eb-9486-4b5173cc23a5.png"> 
<img width="300" alt="node4" src="https://user-images.githubusercontent.com/86324276/123000899-c1251780-d375-11eb-8c53-dcd3e3e7ad67.png"> 
<img width="300" alt="node5" src="https://user-images.githubusercontent.com/86324276/123000919-c8e4bc00-d375-11eb-8fd4-c8490cebf021.png"> 
<img width="300" alt="node6" src="https://user-images.githubusercontent.com/86324276/123000942-d0a46080-d375-11eb-998b-4ededdade5f1.png"> 
<img width="300" alt="node7" src="https://user-images.githubusercontent.com/86324276/123000966-d7cb6e80-d375-11eb-807c-08c39dc2e379.png">
<img width="300" alt="node8" src="https://user-images.githubusercontent.com/86324276/123001250-237e1800-d376-11eb-9433-ee5f8e1c9a77.png">
<img width="300" alt="node9" src="https://user-images.githubusercontent.com/86324276/123001261-27aa3580-d376-11eb-8c2b-10cd99860095.png">
<img width="300" alt="node10" src="https://user-images.githubusercontent.com/86324276/123001267-2b3dbc80-d376-11eb-995b-7139caba91dd.png">
<img width="300" alt="node11" src="https://user-images.githubusercontent.com/86324276/123001277-2e38ad00-d376-11eb-904e-819734ddc2bb.png">
<img width="300" alt="node12" src="https://user-images.githubusercontent.com/86324276/123001286-31cc3400-d376-11eb-8f46-b54ea21d45cc.png">

[comment]: # (Quiz / Presentation / Project / Writing Assignment / Observation / Walk Around / Oral Questioning / Other)


### Lead Author
Sara Braga

### Acknowledgements

Special thanks to Dakota State University for the introduction to Internet of Strings.

## License
[Nebraska GenCyber](https://github.com/MLHale/nebraska-gencyber) <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Overall content: Copyright (C) 2017-2018-2018  [Dr. Matthew L. Hale](http://faculty.ist.unomaha.edu/mhale/), [Dr. Robin Gandhi](http://faculty.ist.unomaha.edu/rgandhi/), and [Doug Rausch](http://www.bellevue.edu/about/leadership/faculty/rausch-douglas).
