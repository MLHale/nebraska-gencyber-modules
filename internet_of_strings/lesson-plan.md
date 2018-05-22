# Hands-on IoT: Internet of Strings

### Summary
This is an active classroom activity teaching students about networking routing. 

### Grade
High School

### Time Required
60 Minutes

### First principles
- [ ] Domain Separation
- [ ] Process Isolation
- [ ] Resource Encapsulation
- [x] Modularity
- [ ] Least Privilege
- [x] Abstraction
- [ ] Data Hiding
- [ ] Layering
- [ ] Simplicity
- [ ] Minimization


### Learning Objectives

* Students will understand how routing occurs within networks.

### Materials list

* Post-it Notes
* Small Boxes 
* Toilet Paper Tubes
* Anything that can be connected to strings to act as a node (desks, tables, buckets, cardboard)

### Learning Facilitation

Each item below is optional.

#### Warm up Activity

Host a discussion on routing tables and how packets travel over a network.

#### Focused Activity

Process for Internet of Strings Routing

If you are originating message
1. Receive message and place in packet payload
2. Refer to your node's routing table and select the least cost route to final destination
3. Build packet header on post-it note (see example) and place on packet
4. Pace packet on link and move to the next hop

When you arrive at a node
1. Remove packet from link, review packet header and determine if message is for the node you are at. 
    - If message is for this node, remove payload, verify it is at the right node, and 
      announce results, either, 
      "message recevied" or "message misrouted"
    - If message is not for this node, hand packet to next individual and continue with step 
      2 below
2. Refer to the current node's routing table and select the least cost route to final 
     destination
    - If there is no route to final destination announce "bad route" and go to the end of 
      the line for that node
    - If there is a route but the link you need is not available
      a. Check to see if there is a higher cost route available
      b. If there is a higher cost route use it and continue with number 3
      c. If there is not a higher cost route announce "link down"
3. Build new packet header by adding a new next hop (see example below) and place on 
    packet
4. Place packet on link and move to next hop

If you are moving to the next hop and collide with another packet
1. Return to the node you came from
2. Pick a number between 1 and 10 and then wait that many seconds before going to the next hop again


#### Closure

Provide a 5 minute warning when the activity will end. Once complete, have all the students help put away the supplies.

#### Reflection

Once the activity is over, host a discussion on how this activity translates to networking routing.

### Assessment

Facilitators of this module will observe student participation to ensure that each student gains an understanding of how routing tables work.

[comment]: # (Quiz / Presentation / Project / Writing Assignment / Observation / Walk Around / Oral Questioning / Other)

### Accommodations for students with disabilities

N/A

### Extension Activity 

N/A

### Acknowledgements

Special thanks to Dakota State University for the introduction to Internet of Strings. 

## License
[Nebraska GenCyber](https://github.com/MLHale/nebraska-gencyber) <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Overall content: Copyright (C) 2017  [Dr. Matthew L. Hale](http://faculty.ist.unomaha.edu/mhale/), [Dr. Robin Gandhi](http://faculty.ist.unomaha.edu/rgandhi/), and [Doug Rausch](http://www.bellevue.edu/about/leadership/faculty/rausch-douglas).

Lesson content: Copyright (C) [Your name here](your site here) 2017.
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">This lesson</span> is licensed by the author under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
