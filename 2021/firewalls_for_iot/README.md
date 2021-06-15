---
layout: page
title: Firewalls
---

Firewalls are often the first line of defense for an enterprise or home network. In this unit, we will understand the fundamentals of firewalls, write firewall rules that configure its behavior and then test if the firewall performs as expected.

### Cybersecurity First Principles
* __Minimization__: Minimization refers to having the least functionality necessary in a program or device. The goal of minimization is to simplify and decrease the number of ways that software can be exploited. This can include **turning off ports that are not needed**, reducing the amount of code running on a machine, and/or turning off unneeded features in an application. This lesson focuses specifically on turning off ports and limiting network connections that aren't required for correct operation.

* __Abstraction__: Something complicated can be thought of and represented more simply using Abstraction. Network packets are abstractions that only provide necessary details to network operators, while reducing the complexity to a set of essential characteristics.

* __Layering__: Cyber security uses multiple layers of defense or protecting information. If one layer is defeated the next layer should catch it. Firewalls are a key aspect of any layered defense.

* __Least Privilege__: One of the ways to protect information is by limiting what people can see and do with your information and resources. The principle of least privilege says to allow the minimum number of privileges necessary to accomplish the task.

### Table of Contents  
[Overview](#overview)  
[Firewalls as a Collection of Valves](#firewall-as-a-collection-of-valves)  
[Firewall Rules](#firewall-rules)  
[Windows Firewall](#windows-firewall)   
[Additional Readings](#additional-readings)  
[Teacher Developed Modules](#teacher-developed-modules)  
[Acknowledgements](#special-thanks)  


## Overview

The name `firewall` is inspired from its physical manifestation in construction which refers to walls that are designed to stop a fire from spreading.

> ![Firewall in a substation](https://upload.wikimedia.org/wikipedia/commons/3/3c/Firewall_Electrical_Substation.jpg)

While these firewalls are "cool", we are interested in a different kind of firewall. Namely, the ones that protect internal networks from external networks. These kinds of firewalls allow us to control the flow of information between networks. Firewalls __minimize__ the number of ways that internal networks and computers on them can be exploited. They also encourage __least functionality__ by turning off ports that are not needed. Firewalls can also drop network traffic that does not conform to expected patterns (such as malicious requests to an application server).

> ![network firewalls](./img/networkfirewall.png)


Firewalls aren't just for networks. Each computer in a network can have its own `personal firewall`. All popular operating systems now come with a firewall installed. For Windows Server and Desktop installations we will focus on the built-in `Windows Firewall with Advanced Security` application. This application can be configured with a graphical user interface or the command line interface using `netsh` or Powershell `NetSecurity` modules. These options provide a lot of flexibility and control over the configuration of the firewall for personal and enterprise use.

> ![Windows firewall](./img/windowsfirewall.png)

When two machines communicate (such as a client talking to a server), communication spans many different __layers__. Each of these layers is progressively lower level as you move downward. These layers provide abstractions that show only the necessary details, while reducing the complexity to a set of essential characteristics. In general there are 7 layers:

- `Application` - The highest level layer where application data is handled (HTTP/FTP/DHCP/SSH/SSL, etc)
- `Presentation` - often the same as the application level, sometimes acts as a translation between application and session
- `Session` - The layer that is used to form sessions between applications (often issues remote procedure calls (RPCs))
- `Transport` - One of the two layers that are foundational to the modern internet (TCP / UDP), this layer serves to transport packets from one host to another.
- `Network` - The second of the foundation layers for the modern internet (IP, IPv4, IPv6, IPSec, etc). This layer serves to transport packets between routers (often referred to as __packet forwarding__).
- `Data Link` - The biggest example of the data link layer is `ethernet`. It provides a protocol for exchanging data over a local network.
- and `Physical` - This layer is nothing but raw bits that underly the interpretation of those bits at higher levels.

> ![network layers](https://javirodz.files.wordpress.com/2013/07/21acd-osi.gif)

### Question

At which [OSI layer](https://support.microsoft.com/en-us/kb/103884) does it make the most sense for a firewall to filter the information flowing between two different networks?

- [ ] Physical layer  
- [ ] Data link layer  
- [ ] Network layer and above  

Discussion:  
The headers on ethernet frames at the `Data link` layer and below are not useful for routing across networks. Packet filtering Firewalls rules are authored using routing information starting at the `Network` (also called the IP layer in the TCP/IP implementation) layer and above, all the way to the `Application` layer. As a result IP layer firewalls are the simplest and most widely used.


[Top](#table-of-contents)

### Firewall as a Collection of Valves

A packet filtering Firewall can be understood as a collection of valves  

* Each valve/port corresponds to single service at the application level (e.g. HTTP, SSH, HTTPS, SMTP)
* Each valve can  
  - Permit traffic in one or both directions  
  - Deny traffic  

![valves](./img/valves.png)  

Here are three basic scenarios to keep in mind.  

First, lets consider **Ports 1 and 4**. These ports are open. Which means they permit packets from internal and external sources. So in the case of the TCP protocol, which forms explicit connections or circuits before transmitting data via a handshake mechanism, such connections can be externally or internally initiated.

In the case of **Port 2**, it allows unrestricted flow of information if the connection is initiated internally. However, it blocks all external requests to initiate an information flow. That is, it permits packets from external sources only if they correspond to a `connection` initiated by an internal source. The firewall will not permit connection requests from external sources. This restriction is useful when an internal web client initiates a web browsing request, then the firewall will allow the corresponding incoming response from an external webserver to pass through the firewall. Any connection initiated externally will not be allowed.

Finally, **Port 3** is closed. Which means that it denies all traffic. A closed port may just drop the packets or send back an RST or "Reset" packet. From a security and resource consumption standpoint, it is always better to just drop the packet. Upon denial of access, no additional or useful information should be communicated back.

[Top](#table-of-contents)

## Firewall Rules

Firewalls are configured using simple `if then` rules. In a packet filtering firewall, a rule says: `IF source IP, destination IP, protocol, and local ports and remote ports match a pattern THEN take this action`. Since there are many rules involved, the order of the rules matters. **A LOT!**

Rules are evaluated **in order**, starting with the first one at the top until a first match is discovered. If your top rule is very generic, i.e. matches almost every packet, then **none of the later specific rules will ever be evaluated**. So it is best to start with rules that are the `most restrictive` (i.e rules that focus on to specific services and have a very small chance of interfering with other rules). After ordering by restrictiveness it is then best to order rules according to `how well they match the majority of your network traffic`. This minimizes the number of checks required to find a matching rule. If `block` and `allow` rules do not match, the default policy of the firewall is applied.

Always start firewall configuration with a `whitelisting` philosophy, where you **Deny by default** and allow only specific information flows. This means, start the firewall configuration by dropping all packets by default. Then add rules to `allow` specific traffic patterns (incoming, outbound, or forwarding) as required by application needs.

Let's look at an example for exposing a web service over HTTP.

| Rule#  | Direction     | Source        | Destination   | Local Port   | Remote Port   | Action   |
| ------ |:-------------:|:-------------:| :------------:|:------------:|:-------------:|:--------:|
| 1      | inbound       | any           | web server    | http (80)    | any           | ```accept```   |
| 2      | outbound      | web server    |   any         | http (80)    | any           | ```accept```   |
| 3      | any           | any           |   any         | any          | any           | ```reject```   |

**Rule 1** permits externally initiated requests (Direction: inbound) to a webserver behind the firewall. So the source is ```any```, since we cannot anticipate a specific IP address at the time of writing the rule. The destination is the IP address of the webserver and the Local Port specifies the port number where the service is typically hosted. That would be port ```80``` for a web server. The request may originate from any Remote Port. If these conditions match an incoming packet then the action is ```accept```(allow packet to come in).

**Rule 2** permits internal requests (Direction: outbound) out to the Internet. So the source is any IP address of the ```web server``` and the Destination is  ```any```. The Local Port is ```80``` (originating port) and Remote Port is ```any```. If a packet matches these conditions then the action is ```accept``` (allow packet to go out).

**Rule 3** denies all traffic (in ```any``` direction). So all match conditions are specified as ```any``` and the action is ```reject```. This is ```Default Deny``` behavior.

### Question

What would happen if we re-ordered these rules? Specifically, if Rule 3 was exchanged with Rule 1.

Discussion:
* Inbound and outbound rules are typically maintained in separate lists. We will see this shortly. Rule 3 is typically implemented as a ```Default Policy``` in Inbound and Outbound rule lists. It applies if none of the specified rules match.

[Top](#table-of-contents)


## Interactive Firewall Game

Let's play a game that helps us understand firewall rules. These rules are the basic building blocks of a fundamental packet filtering mechanism.

[Click here to play the Game](https://groups.inf.ed.ac.uk/tulips/projects/1617/PermissionImpossible/)

## Windows Firewall

As mentioned before, Windows has a built-in firewall. Depending on the profile (type) of Network your computer is connected to, the firewall can be configured to have a different behavior. Your home network should be assigned the ```Private``` profile, while coffee-shop and airport networks are best assigned to the ```Public``` profile. Enterprise computers are typically part of a ```Domain``` in an enterprise network. For this option, the ```Domain``` profile is used. When you bring up the firewall, you will see these profiles listed. You will also see the default policy for inbound and outbound network connections associated with each profile.

> ![Windows firewall](./img/network-profiles.png)

### Observations:  

* The firewall is ON
* Inbound connections are being blocked by default. Allowed connections have to be whitelisted.
* Outbound connections are being allowed by default!!!    
Which means that unless you block a connection, it is allowed. This is not a secure setting. Once malware is installed on your machine (quite plausible with phishing), it can easily call out to a remote server and exfiltrate data. This poor [design choice](https://docs.microsoft.com/en-us/windows/access-protection/windows-firewall/create-an-outbound-port-rule) is perhaps motivated by a trade-off between usability and security.

The defaults for Outbound connections go against the fundamental security principle of ```Default Deny``` and ```Whitelisting``` allowed connections. Let's go ahead and make it right.

> Be ready for many internet connected programs to stop working after this change!

Click on Firewall Properties to view the defaults for all profiles

> ![Windows firewall](./img/firewall-defaults.png)


Let's change the default behavior for Outbound connections to ```Block```.

> ![Windows firewall](./img/block-outbound.png)

Repeat the same for Private and Public profiles (tabs). Then hit ```Apply``` to save these settings.

By default, all rules apply to all network interfaces for both IPv4 and IPv6 protocols. The network interfaces protected by Windows Firewall can be changed clicking on the ```Customize``` button next to ```Protected network connections```

> ![Windows firewall](./img/network-connections.png)

We see that all network interfaces are selected. Observe that DockerNAT is also covered.  
Hit ```OK``` to exit.  
Hit ```OK``` again to exit the Properties dialog box.  

Now the firewall status page should look like this:

> ![Windows firewall](./img/default-deny.png)

Let's test with Chrome. Open the Chrome browser and see if you can navigate to any website.

The web request fails. Why?

> The request can not pass through the firewall (outgoing direction) to reach web servers

So we need to allow Chrome program through our firewall in the Outbound direction.
We want to be very specific to the Program, Ports, and Protocol in our Rule (Cybersecurity First principle: Minimization).

Let's start to author a new Outbound rule. Select ```Custom``` rule to provide the most flexibility. Click ```Next```.

> ![Windows firewall](./img/outbound-rule.png)

Next, we locate the program that we want to allow through the firewall in the outbound direction. Click the browse button and locate the Chrome executable here: `%ProgramFiles%\Google\Chrome\Application\chrome.exe`

Click ```Next```. That brings us to ```Protocols and Ports```.   
We want Chrome to be able to contact web servers on HTTP (Port ```80```) and HTTPS (Port ```443```) services using the ```TCP``` protocol.    
So adjust the settings as shown:

> ![Windows firewall](./img/outbound-ports.png)

Click ```Next```. We will not limit the connection to specific IP addresses, so we will leave ```Scope``` as is.   
Click ```Next``` again.

Now for ```Action```. Select ```Allow the connection``` since we are whitelisting this application.

> ![Windows firewall](./img/outbound-action.png)

Next, for ```Profile``` select all profiles so that the rule applies to all network types.  
Finally, provide the rule a Name and Description to identify it later.

Click ```Finish```. The rule is now active and should be listed in the Outbound rules listing.

Now use similar steps as above to add a rule for the same program (Chrome), but allowing protocol ```UDP``` for remote port ```53```. This allows DNS requests to go through. DNS helps with domain name discovery.

Once the UDP rule is added, we are ready to try accessing a website again.

It should work this time. Call the instructor to troubleshoot if are still not able to browse to a website.

If you would like to practice further, [firewall configuration with Docker for Windows is available here.](./advanced.md)

## Test your blockage, err … knowledge!


[Firewall Quiz](https://unomaha.az1.qualtrics.com/jfe/form/SV_2nx7ci6Tm2NE7Jz)

That's it for Firewalls in this Unit. Happy Surfing.

> Firewalls are an essential component of "Defense-in-Depth" strategy. It can certainly slow down an attacker. However, firewalls cannot keep a determined adversary out. There are many ways in which firewalls can be abused and easily bypassed. Such attacks need to be constantly monitored using Intrusion Detection Systems (IDS) and Network Monitoring solutions. The final line of defense is applications built using secure coding practices and proper encryption implementations. This is an example of `Layering`.

[Top](#table-of-contents)

## Additional Readings

* [Order of Windows Firewall Rule Evaluation](https://technet.microsoft.com/en-us/library/cc755191%28v=ws.10%29.aspx)
* [Microsoft Windows Firewall in Enterprise Environment Resources](https://docs.microsoft.com/en-us/windows/access-protection/windows-firewall/windows-firewall-with-advanced-security-design-guide)
* [Microsoft The OSI Model's Seven Layers Defined and Functions Explained](https://support.microsoft.com/en-us/kb/103884)  
* Linux firewalls
  * [Ubuntu iptables Wiki](https://help.ubuntu.com/community/IptablesHowTo)  
  * [CentOS iptables Wiki](https://wiki.centos.org/HowTos/Network/IPTables)
  * 25 Most Used iptables commands, [The Geek Stuff](http://www.thegeekstuff.com/2011/06/iptables-rules-examples/)
  * [UFW - Uncomplicated Firewall for Ubuntu](https://help.ubuntu.com/community/UFW)

[Top](#table-of-contents)

## Lead Author

- Robin Gandhi

## Special Thanks

* A special thanks to Matt Hale for reviews of this module and thoughtful discussions.

[Top](#table-of-contents)

# License
[Nebraska GenCyber](https://github.com/MLHale/nebraska-gencyber) <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Overall content: Copyright (C) 2017-2018  [Dr. Matthew L. Hale](http://faculty.ist.unomaha.edu/mhale/), [Dr. Robin Gandhi](http://faculty.ist.unomaha.edu/rgandhi/), [Dr. Briana B. Morrison](http://www.brianamorrison.net), and [Doug Rausch](http://www.bellevue.edu/about/leadership/faculty/rausch-douglas).

Lesson content: Copyright (C) [Robin Gandhi](http://faculty.ist.unomaha.edu/rgandhi/) 2017-2018.  
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">This lesson</span> is licensed by the author under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
