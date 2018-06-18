## Windows Firewall and Docker

In this lesson we examine how a firewall can be configured for services that are hosted in a docker container.

With outbound traffic blocked from the firewall lesson, the firewall status page should look like this:

> ![Windows firewall](./img/default-deny.png)

Now, Let's test with docker. Open a Powershell terminal:

```bash
# Try to pull this docker image
# If you already have a local copy
# this command will attempt to update it
docker pull gists/lighttpd
```
> ![Windows firewall](./img/outbound-fail.png)

The pull fails. Why?

> The request can not pass through the firewall (outgoing direction) to reach docker servers

Docker for Windows uses ```vpnkit``` module to provide virtual networking. So we need to allow this program through our firewall in the Outbound direction.
We want to be very specific to the Program, Ports, and Protocol in our Rule (Cybersecurity First principle: Minimization).

Let's start to author a new Outbound rule. Select ```Custom``` rule to provide the most flexibility:

> ![Windows firewall](./img/outbound-rule.png)

Next, we locate the program that we want to allow through the firewall in the outbound direction.

> ![Windows firewall](./img/outbound-program.png)

Click ```Next```. That brings us to ```Protocols and Ports```.   
We want docker to be able to contact docker hub webservers (```Remote```) to access HTTP (Port ```80```) and HTTPS (Port ```443```) services using the ```TCP``` protocol.    
So adjust the settings as shown:

> ![Windows firewall](./img/outbound-ports.png)

Click ```Next```. We will not limit the connection to specific IP addresses, so we will leave ```Scope``` as is.   
Click ```Next``` again.

Now for ```Action```. Select ```Allow the connection``` since we are whitelisting this application.

> ![Windows firewall](./img/outbound-action.png)

Next, for ```Profile``` select all profiles so that the rule applies to all network types.  
Finally, provide the rule a Name and Description as shown below:

> ![Windows firewall](./img/outbound-name.png)

Click ```Finish```. The rule is now active and should be listed in the Outbound rules listing.

Now use similar steps as above to add a rule for the same program (vpnkit), but allowing protocol ```UDP``` for remote port ```53```. This allows DNS requests to go through. DNS helps with domain name discovery.

Once the UDP rule is added, we are ready to try the `pull` command again.

```bash
# Try to pull this docker image
docker pull gists/lighttpd
```

It should work this time. Call the instructor to troubleshoot if the command fails.

> ![Windows firewall](./img/outbound-allowed.png)

### Inbound Connection Filtering

The default policy for Inbound connections is ```Block```. So at installation time, programs insert very broad ranging rules to avoid later connection issues. Docker does the same. Locate inbound rules named ```vpnkit```. You should see two of them.

> ![Windows firewall](./img/inbound-vpnkit.png)

Examine the properties of both. Properties for the TCP rule are shown below.

> ![Windows firewall](./img/inbound-properties.png)

Here is a summary of properties from both rules:

> 1. Program: `%ProgramFiles%\Docker\Docker\resources\vpnkit.exe`
> 2. Protocol: ```TCP```
> 3. Local Port: ```any```
> 4. Remote Ports: ```any```

and

> 1. Program: `%ProgramFiles%\Docker\Docker\resources\vpnkit.exe`
> 2. Protocol: ```UDP```
> 3. Local Port: ```any```
> 4. Remote Port: ```any```

If you only wanted to host a webserver container or a DNS server container, this rule allows unnecessary exposure to all other ports. By applying the minimization principle we can reduce the attack surface. What we need is the following configuration, if all we want to do is expose web services and perhaps allow incoming DNS requests:

> 1. Program: `%ProgramFiles%\Docker\Docker\resources\vpnkit.exe`
> 2. Protocol: ```TCP```
> 3. Local Port: ```80, 443```
> 4. Remote Ports: ```any```

and (2nd rule is optional for the `cloudbit` container app, rule may be just disabled)

> 1. Program: `%ProgramFiles%\Docker\Docker\resources\vpnkit.exe`
> 2. Protocol: ```UDP```
> 3. Local Port: ```53```
> 4. Remote Port: ```any```

Here is the change illustrated for the TCP rule.
> ![Windows firewall](./img/inbound-updated.png)

This change minimizes the attack surface and enforces least privilege.

Now check if your `Cloudbit` application still works after making these changes.

Check other programs in the Inbound rules list that you think might be allowing more exposure (Protocol and Ports) than necessary for operation.

That's it for Firewalls in this Unit. Happy Surfing.

## Special Thanks

* A special thanks to Matt Hale for reviews of this module and thoughtful discussions.

[Top](#table-of-contents)

# License
[Nebraska GenCyber](https://github.com/MLHale/nebraska-gencyber) <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Overall content: Copyright (C) 2017  [Dr. Matthew L. Hale](http://faculty.ist.unomaha.edu/mhale/), [Dr. Robin Gandhi](http://faculty.ist.unomaha.edu/rgandhi/), and [Doug Rausch](http://www.bellevue.edu/about/leadership/faculty/rausch-douglas).

Lesson content: Copyright (C) [Robin Gandhi](http://faculty.ist.unomaha.edu/rgandhi/) 2017.  
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">This lesson</span> is licensed by the author under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
