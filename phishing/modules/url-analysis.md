# Phishing

## Cybersecurity Commonsense
[Source: DHS Stop. Think. Connect. [Campaign](https://www.stopthinkconnect.org/tips-advice/general-tips-and-advice)]

* __Protect your $$:__ When banking and shopping, check to be sure the site is security enabled. Look for web addresses with `https://`, which means the site takes extra measures to help secure your information. `http://` is not secure.

* __When in doubt, throw it out:__ Links in emails, social media posts and online advertising are often how cybercriminals try to steal your personal information. Even if you know the source, if something looks suspicious, delete it.

* __Stay current:__ Keep pace with new ways to stay safe online: Check trusted websites for the latest information, and share with friends, family, and colleagues and encourage them to be web wise.

* __Safer for me, more secure for all:__ What you do online has the potential to affect everyone – at home, at work and around the world. Practicing good online habits benefits the global digital community.

### Cybersecurity First Principles
* __Layering__: Cyber security uses multiple layers of defense or protecting information. If one layer is defeated the next layer should catch it.

* __Information Hiding__: Information hiding is any attempt to prevent people from being able to see information. It can be hiding the content of a letter, or it can be applied to hiding how the letter is delivered. Both ways can prevent people from being able to see the information. This lesson looks at how malicious information can be hidden in URLs or other data fields.

## Phishing Humor

Phishing is a play of words on "fishing". The bait is often a email or social media message from a spammer, the fish are the unsuspecting victims who act on them.
> ![dibert1](http://assets.amuniversal.com/c82f58606d5101301d7a001dd8b71c47)

Spammers send out millions of messages, only a few need to succeed...
> ![dibert2](http://assets.amuniversal.com/b0d71fd0abaf01314782005056a9545d)

Phishing victims often fear ridicule and do not report crimes...
> ![dibert3](http://assets.amuniversal.com/b1cbb110abaf01314782005056a9545d)

# Introduction

## Lesson goals
- Read URLs
- Spot common techniques for URL manipulation

## Materials required
- Internet connected Machine

## Prerequisite lessons
- Lots of curiosity


## Table of Contents
[Introduction](#introduction-to-urls)  
[Reading a URL](#reading-a-url)  
[URL Tricks](#url-tricks)  
[AntiPhishing Phil Game](#antiphishing-phil-game)   
[Additional Readings](#additional-readings)  
[Teacher Developed Modules](#teacher-developed-modules)  
[Acknowledgements](#special-thanks)

## Introduction to URLs

Most Phishing attacks start with a specially-crafted URL. When clicked on, phishing URLs take you to fake websites, download malware or prompt for credentials.

A URL is an acronym for Uniform Resource Locator. It is a standard format for locating web resources on the Internet. Most Internet users refer to it as the "address for a website". For example, http://www.amazon.com. News story URLs like this one: http://www.cnn.com/2016/07/06/health/juno-jupiter-nasa/index.html are often much longer. On social media sites we are used to seeing short URLs like this one: http://cnn.it/29lG6OK or links on shopping sites: https://amzn.com/0132390779. Even emails are often filled with URLs that senders want us to click on. URLs also give us access to our bank accounts, tax filing, healthcare, billing, and many government services. While all Internet users use it everyday, very few are confident in their abilities to read a URL, much less understand what might happen if clicked on. Let's change that. A vigilant, trained and aware human user is a critical layer of defense against threats both internal and external. Even if malicious URLs and Emails get past spam filters and anti-virus software, a human user can catch it. Such a defensive strategy is common in secure system designs. It is a *cyber security first principle* called `Layering.`

[Top](#table-of-contents)

## Reading a URL

Computer users often have misconceptions about understanding a URL. Spammers take advantage of these misconceptions when crafting phishing URLs.

##### Misconception 1   
Read a URL from left to right, just like English [WRONG!]

Consider this email snippet:

```text
Dear user:
Your facebook account has been locked out due to inactivity.
To re-activate your account please on the click below.

	http://activate.facebook.fblogins.net/88adbao798283o8298398?login.asp

```

So is this a Facebook URL?  How do we tell if this link is legitimate or not without clicking on it?  

If we just start reading the URL from left to right, like English, then this URL appears legitimate because we encounter the word `facebook` in the URL. But that is not the correct way of reading a URL.

### The "Right" way to read a URL

The Internet is a network of networks. Each network that is under the control of an authority, is a separate **Domain**. For example, organizations like University of Nebraska at Omaha, Facebook or Apple have authority over their own Domains/Networks that are connected to the Internet. URLs, which are used to reference computers in a particular network are also called **Domain Names**. Continuing our example, some top-level domains are `unomaha.edu`, `facebook.com` and `apple.com`.

These domain names have to be **unique** on the Internet. So who is responsible for ensuring this? This function is coordinated by ICANN. Here is what is listed on the ICANN website:

>Internet Corporation for Assigned Names and Numbers (ICANN) coordinates the Internet Assigned Numbers Authority (IANA) functions, which are key technical services critical to the continued operations of the Internet's underlying address book, the Domain Name System (DNS).

There is a structured scheme to assign domain names to various organizations. All domain names end in a period `.`. But the period is not always required when using URLs. So it does not matter if it is there or not. Go ahead and paste this URL in your browser window. Notice the period at the end.

```text
www.google.com.
```
The browser still takes you to the google search page.

The period is the "root" of the entire DNS (Domain Name System). The next level child nodes are the "com", "edu", "org", "in", etc. Next, if the organization Wikipedia want a domain name like `wikipedia.org`, then IANA or another ICANN-accredited registrar will insert the `wikipedia` node into the Global DNS system for the Internet. This is where the control of ICANN ends.

Below the `wikipedia` node, the Wikipedia organization has full autonomy and authority to make up whatever names that it wants for specific computers in its **Domain**. So for its Russian office, if it wants to create a `ru` node, then Wikipedia has full authority to do so.

This is depicted in the figure below.

![domainnames](./img/domainnames.png)


So if wikipedia wants to name a computer `apple` in its domain, then it has full freedom to do so. The name of the computer on the Internet would be `apple.wikipedia.org.` This URL has nothing to do with the `apple.com.` top-level domain.

Now it should be apparent that the "right" way to read a url is to actually start reading it from the *right*. Starting from the right allows us to identify the top-level domain for the URL. There are two simple rules to follow:

* If no single forward-slash characters (`/`) exists in the URL, start reading the top-level domain names from the far right to left.

  > For example: https://www.icann.org has no single forward-slash characters. It does have double forward-slash characters (`//`), but that is not what we are looking for. So in this case, start reading the top-level domains from the far right to left. It is `org` and then `icann`

* If single forward-slash characters (`/`) exist in the URL, then find the farthest one from the right. Start reading the top-level domain names right to left from that point onwards.

  > For example: `http://activate.facebook.fblogins.net/88adbao798283o8298398?login.asp`   
  In this link the farthest single forward-slash(`/`) from the right is between `net` and `88adbao798283o8298398`. So the top-level domains here are `net` and then `fblogins`. Beyond these two names, the organization that owns `fblogins` domain can makeup whatever names that it wants, such as `www`, `login`,`facebook`, `apple` or `google`.   
  So now we know that this link is not at all affiliated with `facebook.com`!


#### Exercise:

##### What are the top-level domain names for these URLs:

```
http://www.cnn.com/tiger-woods/story.html   

http://www.buy.com.money.ru
```

Check your answers with your peers. Do they match?

##### Which link will you click on? #1 or #2  

```
#1: ftp://ftp.microsoft.com/software/patches/fixit.exe  
#2: http://www.micosoft.com/software/patches/fixit.exe  

```  
Check your answers with your peers. Do they match?  
[Answer key](./misc.md)


##### Misconception 2
`www` is a standard part of a URL and cannot be changed. ```WRONG!```

Beyond the top-level domains, a organization or individual that has registered the domain has much control over the names of the computers in their networks. The name `www` is commonly give to computers that serve pages to the _World Wide Web_. But it is not necessary to name a web-server as `www`. For example, it is OK to have names such as `http://www2.nationalgeographic.com` or even `http://web.nationalgeographic.com`. So there is nothing special about the `www` part of a URL.

[Top](#table-of-contents)

## URL Tricks

The knowledge in the previous section should serve you well in reading URLs. But spammers often conceal the real URL in HTML formatted emails or fake websites. Let's explore a few such tricks. Some URL behaviors are browser specific. So for our discussion let's open the links below in a `Chrome` browser.

## Tricky Links  
Open this link in a Chrome browser: http://faculty.ist.unomaha.edu/rgandhi/phishing-demo/phishing.html

### Link #1  

On the first link, you will notice that it appears to be a legitimate wellsfargo.com URL. But if you hover over the link, your status bar should show `www.google.com`. How did that happen?

![trickyurls](./img/1-tricky-urls.png)

Examine the page HTML source by right clicking on a blank area of the webpage and selecting `View Page Source` option.

![trickyurls](./img/2-tricky-urls.png)

![trickyurls](./img/3-tricky-urls.png)

In the source code you will see that the `href` attribute, which controls the link target is set to `google.com`. This explains the strange behavior. Hovering over links without clicking them will reveal their real destination in the status bar of the browser.

### Link #2  

For link #2, we explore a peculiarity of browsers. Many browsers will not display, named rightly so, the "shy" character, which is expressed as follows: `&shy`. The page source shows that this character is present in the `href` attribute and the link text. But the character is not displayed in the page!

![trickyurls](./img/6-tricky-urls.png)

![trickyurls](./img/5-tricky-urls.png)

Chrome shows the `&shy` character in the status bar. Some other programs/browsers may not display it at all. Spammers can register domains with `&shy` characters to manipulate users into clicking the links.

### Link #3  

Link #3 is straight-forward, but a bad practice. Legitimate emails often use this technique, but it conceals the true link and conditions users to click on such links. When sending out emails, avoid such practices.

### Link #4

Link #4 is very strange looking. You may examine the page source and still have no additional clues. Naively following the two rules of reading a URL from above, you may end up thinking that this is a `wellfargo.com` URL. But it is not!

![trickyurls](./img/7-tricky-urls.png)

If you hover over the link in Chrome, much to our surprise it turns out to be `google.com`!!!!

![trickyurls](./img/8-tricky-urls.png)

This URL uses two methods to trick users.
* Hex encode the URL letters. The full conversion table is available here: http://www.asciitable.com/index/asciifull.gif Using this table we can decode the letters as follows:
```
%67 = g
%6F = o
%6F = o
%67 = g
%6C = l
%65 = e
%2E = .
%63 = c
%6F = o
%6D = m
```
So the last part of Link #4 is `google.com`

* This URL also uses an arcane URL technique to specify the login and password as part of the link itself. Some insecure websites allow login requests in the following manner.   

	```text
	http://username:password@example.com

	For link #4:
	username = wellsfargo.com
	password = login
	website  = google.com

	http://wellfargo.com:login@google.com

	Tricky indeed!
	```

With these tricks uncovered, the previous two URL reading rules will suffice now to know what the true top-level domains are. Certainly not `wellsfargo.com`.

### Link #5

The next link is very mysterious as well. By hovering over it or examining the page source, you will notice that it is a **short URL**. A short URL is notoriously deceptive as you cannot tell where it will take you once clicked on.

To overcome this issue, we will use a service that expands the short URL and provides a preview of the final destination.

**Short URL expander**: http://checkshorturl.com/expand.php

Upon using the URL expander service, it is apparent that this short URL redirects to `google.com`.

![trickyurls](./img/9-tricky-urls.png)

### Link #6

At first glance, Link #6 is a short URL too. Let's just copy this link from the browser and check it using the URL expander service. You will determine that it is `google.com`.

But, now hover over the link or view the page source to examine the real link in the `href` attribute. It appears to be a slightly different short URL!

![trickyurls](./img/10-tricky-urls.png)

If you expand this different short URL, it leads you to `duckduckgo.com`.

Spammers may trick you by making such subtle modifications in the HTML page.

### Link #7

Hover over link #7 to examine its real destination. What happens?

Using JavaScript, the page automatically redirects you to `google.com` when your mouse hovers over the link! The script is triggered by a `onMouseOver` event.

When visiting questionable websites, it is prudent to turn off JavaScript or use JavaScript blocking extensions such as [No-Script](https://noscript.net) or [ScriptSafe](https://chrome.google.com/webstore/detail/scriptsafe/oiigbmnaadbkfbmpbfijlflahbdbdgdf?hl=en)

### Link #8

Hover over [link #8](http://faculty.ist.unomaha.edu/rgandhi/phishing-demo/phishing.html) to examine its real destination. What do you see?

Turns out you can register DNS names in any language using Unicode. Punycode is used to encode internationalized domain names (IDN). As a result, similar looking foreign alphabets can be used to register domains that are extremely close in appearance to english letters.

- Copy this URL http://гауthеоn.соm and use this site to check if it is internationalized or not.
https://www.punycoder.com/
	- You should see equivalent punycode


- Now try it with this URL: http://raytheon.com
	- This one is in english.

The previous one uses [Russian Cyrillic Characters](http://symbolcodes.tlt.psu.edu/bylanguage/cyrchart.html). This attack also fools browser inspection tool in Chrome.

Such attacks are similar to domain-squatting but also referred to as [homophone](http://blog.trendmicro.com/trendlabs-security-intelligence/soundsquatting-unraveled-homophone-based-domain-squatting/) (similar looking, sounding, spelling) attacks.

>![trickyurls](./img/punycode.png)

### Link #9

Click on Link #9. The destination appears to be wellsfargo.com. Even the URL appears to be wellsfargo.com. But a few things are off. The protocol is different and there are additional characters (`<`, `...` and `,`) that you would not normally see. Now click in the URL bar and navigate to the right of the URL using arrow keys. You will notice a bunch of text. Copy the entire URL (`crtl+a` and then `crtl+c`) and paste it in Notepad.

> ![trickyurls](./img/dataURL.png)

This is a [Data URL](https://en.wikipedia.org/wiki/Data_URI_scheme) that allows specifying small files inline within HTML documents. Typically this is used to includes images in HTML document. Turns out that browsers will also render this URL as an HTML page. All the content needed to render the html page is right within the URL itself!

In this link we have embedded enough spaces between the place holder text and the real content such that a user can be fooled into believing the website is being loaded from the displayed domain name. This URL was generated by scraping all the HTML from wellsfargo.com, including embedded images, and encoding it within the Data URL. We could have just as easily included some malicious javascript in here to steal any username and password entered.

Don't worry the game in the next section is safe 😎

## AntiPhishing Phil Game

Let's play a game to test your URL "Know-How". The game is called AntiPhishing Phil.

> Sometimes the game is slow to load between rounds. If you see a blank square box then be patient and click inside it to move through the game.

http://www.ucl.ac.uk/cert/antiphishing/

Here is a link to the commercial game site.
Registration is required to play the demo game :-(  
http://wombatsecurity.com/antiphishingphil

A free training course is available at OIT. This is free to play:  
https://oit.byuh.edu/help/anti-phishing

[Top](#table-of-contents)


## Additional Readings

* Infographic, Phishing: [How many take the bait?](http://www.getcybersafe.gc.ca/cnt/rsrcs/nfgrphcs/nfgrphcs-2012-10-11-en.aspx)
* [Reporting Phishing](https://www.consumer.ftc.gov/articles/0003-phishing), Federal Trade Commission

[Top](#table-of-contents)

## Teacher Developed Modules

* [Phishing Discussion @ GenCyber Camp 2016](https://dl.dropboxusercontent.com/u/4594444/Gencyber-teacher-modules/spear%20phishing.pptx)

[Top](#table-of-contents)

## Special Thanks

* A special thanks to Matt Hale, Aaron Vigal and Cade Wollcot for reviews of this module and thoughtful discussions.

[Top](#table-of-contents)


## License
[Nebraska GenCyber](https://github.com/MLHale/nebraska-gencyber) <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Overall content: Copyright (C) 2017  [Dr. Matthew L. Hale](http://faculty.ist.unomaha.edu/mhale/), [Dr. Robin Gandhi](http://faculty.ist.unomaha.edu/rgandhi/), and [Doug Rausch](http://www.bellevue.edu/about/leadership/faculty/rausch-douglas).

Lesson content: Copyright (C) [Robin Gandhi](http://faculty.ist.unomaha.edu/rgandhi/) 2017.  
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">This lesson</span> is licensed by the author under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
