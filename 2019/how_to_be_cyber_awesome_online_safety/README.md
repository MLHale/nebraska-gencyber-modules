---
layout: page
title: How to be Cyber Awesome: Online Safety and Privacy
---

### Cybersecurity First Principles
* __Layering__: Cybersecurity uses multiple layers of defense when protecting information or resources. If one layer is defeated the next layer should still be defending.

* __Information Hiding__: Information hiding is any attempt to prevent people from being able to see information. It can be hiding the content of a letter, or it can be applied to hiding how the letter is delivered. Both ways can prevent people from being able to see the information. This lesson looks at how malicious information can be hidden in URLs or other data fields.

# Introduction

## Lesson goals
- Open Source INTelligence (OSINT) gathering

## Materials required
- Internet connected machine

## Prerequisite lessons
- None

## Table of Contents
   
[Open Source INTelligence Gathering](#open-source-intelligence-gathering)    
[Additional Readings](#additional-readings)  
[Acknowledgements](#special-thanks)  

## Open Source INTelligence Gathering

### Spear-Phishing
Crafting URLs is just one part of the deception used by spammers. *Spear-Phishing* is a social engineering technique where a spammer uses intimate details about your life, your contacts, and/or recent activities to tailor a very specific phishing attack.

Watch this 3 min video (if you do not have audio, it is OK):   
[https://www.youtube.com/watch?v=F7pYHN9iC9I](https://www.youtube.com/watch?v=F7pYHN9iC9I)

There is a ton of information on the web pertaining to most of us. This is true even if you do not use social media. Voting registries, court records, county and property records, phone books, and online review sites are just some examples. For so social media users, there is even more information on the web. All you need is your target's name to start `reconnaissance` (Hey! thats the name of a card in our GenCyber Card Deck. See if you can find it).

A site called __Spokeo__ allows its users to search for information about people spanning all sorts of public information sources. Visit the Spokeo site and see how much information is available about yourself or a family member. You may have to pick the correct entry from the search results. But that should be easy with additional information about age and location of your target.

- [Spokeo](https://www.spokeo.com)

Another site like Spokeo is [Pipl](https://pipl.com). It used to be free but now it only offers a paid solution (one low price of $99/month. Phone numbers are guaranteed!).

Finally, sites like Facebook, LinkedIn, company websites, organizational charts and employee directories, make it easy to for attackers to learn information about their targets. This can help them craft emails that appear to come from colleagues, friends, and/or family. 

The process of gathering information online is called Open Source INTelligence or OSINT. There are many tools online that have been built to gather OSINT. One such tool, called maltego, is very prominent, it even has free version): [https://www.paterva.com/web7/buy/maltego-clients/maltego.php](https://www.paterva.com/web7/buy/maltego-clients/maltego.php)

> Maltego is an interactive data mining tool that renders directed graphs for link analysis. The tool is used in online investigations for finding relationships between pieces of information from various sources located on the Internet.

> **Security Tip**: Even when clicking on links in emails or websites shared by close colleagues, friends, and family; trust but verify. This advice will seem even more reasonable after going through the Email analysis module.

Often, attackers start by gathering information about people from prior breaches. A `breach` is an attack that has penetrated a network or system of a company. You may have heard of breaches like the __target data breach__ or the __sony data breach__. These breaches exposed a lot of information about a lot of people. Attackers use prior breach information to focus their efforts and to zone in on targets for further exploitation. Security researchers have tried to help protect people online by compiling lists of known breaches to alert people that their information may have been exposed in prior attacks. You can find out if your information is included in a prior breach by visiting a website called [https://haveibeenpwned.com](https://haveibeenpwned.com). It helps you identify if you or your family's information has been exposed in a data breach. Try searching your own email or someone in your family.

### Geolocation

GPS-enabled smartphones allow photos, videos, messages and social media posts to be **Geotagged**. Location information is embedded in the metadata for media alongside file name, date, camera information, etc. When geotagged media is shared publicly, location information is often inadvertently shared along with it. Such information aggregated over time starts to reveal private information such as: work and home locations, daily routines, frequented places, vacation destinations, shopping places, and much more.

Tools are freely available for conducting Geolocation OSINT. For example, this tool is aptly named geoCreepy!  
Downloads: [http://www.geocreepy.com/](http://www.geocreepy.com/)  
Source code: [https://github.com/ilektrojohn/creepy](https://github.com/ilektrojohn/creepy)  

Another website that overlays images on a map is called __localize__. This site uses images that have been posted on websites like Flickr with unrestricted public access and a geotag embedded in their metadata.

 - [Localize US](https://loc.alize.us/)

Here are Pictures near our camp: [https://loc.alize.us/#/geo:41.247140,-96.016767,18,/](https://loc.alize.us/#/geo:41.247140,-96.016767,18,/)

Here is an image of some of our colleagues found through this website: [https://www.flickr.com/photos/sociotechnika/41740794011/](https://www.flickr.com/photos/sociotechnika/41740794011/)

Let's upload the image on to an EXIF (Exchangeable image file format) processor ([https://tool.geoimgr.com](https://tool.geoimgr.com)). Do you see any problems here?

To spread awareness of such issues with social media, an educational web application called __teachingprivacy.org__ has been developed.

[http://app.teachingprivacy.org](http://app.teachingprivacy.org) (Beware of the ".com" version of this site. This is called [`domain-squatting`](https://en.wikipedia.org/wiki/Cybersquatting))

The teaching privacy web-application takes a twitter handle and aggregates all publicly available geotagged information on a map. For example, here are the travel patterns of Steve Wozniak, co-founder of Apple.

![geotagging](./img/stevewoz.png)

It is often prudent for celebrities and politicians to turn off geotagging in their posts. For instance, if you have a twitter account, there is a setting (Settings --> Security and Privacy) to delete any previously tagged locations.

Generating analytics about social media posts is also real easy. The following website provided detailed breakdown of tweets. All you need is a twitter handle.

[https://socialbearing.com/search/user/](https://socialbearing.com/search/user/)

Checkout what your instructors are up to:

[https://socialbearing.com/search/user/mlhale_](https://socialbearing.com/search/user/mlhale_)
[https://socialbearing.com/search/user/robinagandhi](https://socialbearing.com/search/user/robinagandhi)
[https://socialbearing.com/search/user/kristeenshabram](https://socialbearing.com/search/user/kristeenshabram)
[https://socialbearing.com/search/user/lynnspady](https://socialbearing.com/search/user/lynnspady)

Protecting privacy requires **Information Hiding**. Deleting or hiding metadata prevents sensitive patterns from being learned over time. This is true even for encrypted `https` Internet traffic. While `https` encryption protects message contents, it still reveals the communication endpoints. Over time an accurate communication graph can be built by examining many such communications. To conceal browsing patterns over the Internet, Virtual Private Networks (VPN) are very effective. VPNs work by forming a tunnel between your current connection and a known network (such as the unomaha network). Once a tunnel is formed, all requests you make appear as if they originate from within the known network, since they emanate from the location you have tunneled to.

[Top](#table-of-contents)

## Additional Readings

* [Ten Principles for Online Privacy](https://teachingprivacy.org)
* APWG, Phishing [Public Education](http://phish-education.apwg.org/r/en/index.htm)

[Top](#table-of-contents)

## Lead Author

- Robin Gandhi

## Special Thanks

* A special thanks to Matt Hale, Aaron Vigal and Cade Wollcott for reviews of this module and thoughtful discussions.

[Top](#table-of-contents)


## License
[Nebraska GenCyber](https://www.nebraskagencyber.com) <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Overall content: Copyright (C) 2017-2019  [Dr. Matthew L. Hale](http://faculty.ist.unomaha.edu/mhale/), [Dr. Robin Gandhi](http://faculty.ist.unomaha.edu/rgandhi/), and [Dr. Briana B. Morrison](http://www.brianamorrison.net).

Lesson content: Copyright (C) [Robin Gandhi](http://faculty.ist.unomaha.edu/rgandhi/) 2017-2019.  
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">This lesson</span> is licensed by the author under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
