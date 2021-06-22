# @Author: Matthew Hale <matthale>
# @Date:   2021-06-16T17:00:03-05:00
# @Email:  mlhale@unomaha.edu
# @Filename: servicelib.py
# @Last modified by:   matthale
# @Last modified time: 2021-06-22T00:03:55-05:00
# @Copyright: Copyright (C) 2019 Matthew L. Hale



import requests

class IFTTTLib:
    """
    This library allows for easy triggering of IFTTT maker endpoints (aka WebHooks). 
    
    Attributes:
        secretkey (string) : The key value is the shared secret key provided by the IFTTT webhook service
    
    Sample invocation:
        ifttt = IFTTTLib()
        ifttt.setKey("your_key")
        ifttt.invokeWebhookTrigger("your_event_name","21")
    """
    
    secretkey = ""
    
    def setKey(self,keyval):
        """
        This method sets a private secret key to be used with requests to the maker endpoint. Find your key at https://ifttt.com/maker_webhooks/settings
        
        Parameters:
        keyval (string) : This is the secret key provided by the maker endpoint
        """
        self.secretkey = keyval
        
    def invokeWebhookTrigger(self, event, val1=None, val2=None, val3=None, debug=True):
        """
        This method triggers a webhook endpoint on IFTTT.
        
        Parameters:
        event (string)  :   This is the name of the webhook endpoint defined on IFTTT
        val1 (string)   :   This is an optional data field that can be included in the IFTTT request. 
                            Passed data is provided to the triggered IFTTT service.
        val2 (string)   :   This is an optional data field that can be included in the IFTTT request. 
                            Passed data is provided to the triggered IFTTT service.
        val3 (string)   :   This is an optional data field that can be included in the IFTTT request. 
                            Passed data is provided to the triggered IFTTT service.
        debug (boolean) :   Setting debug to true displays additional detail about requests and responses.
        """
        send_data = {}
        if (val1):
            send_data["value1"] = val1
        if (val2):
            send_data["value2"] = val2
        if (val3):
            send_data["value3"] = val3
            
        target = "https://maker.ifttt.com/trigger/"+event+"/with/key/"+self.secretkey
        if debug:
            print ('Request sent to ====> ', target)
            print ('With data ==========>  Value1=', val1,', Value2=',val2, ', Value3=', val3, "\n")
            
        result = requests.post(target, data=send_data)    # sends data to IFTTT and stores the response msg
        if debug:
            print ('Received ===========> ', result)
            print ('====================> ',result.content)
        
    def sendWeather(self, event, temp=None, barometer=None, humidity=None, debug=True):
        """
        This method sends weather data to a webhook endpoint on IFTTT.
        
        Parameters:
        event (string)      :   This is the name of the webhook endpoint defined on IFTTT
        temp (float)        :   This is temperature data to be sent as value1 on IFTTT
        barometer (float)   :   Barometer data is sent as value2 to IFTTT
        humidity (float)    :   Humidity data is sent as value3 to IFTTT
        debug (boolean)     :   Setting debug to true displays additional detail about requests and responses.
        """
        if temp:
            val1 = "Temperature: " + str(temp) + " °F"
        else:
            val1 = "Temperature: N/A"
        if barometer:
            val2 = "Barometer: " + str(barometer) + " atm"
        else:
            val2 = "Barometer: N/A" 
        if humidity:
            val3 = "Humidity: " + str(humidity) + " %"
        else:
            val3 = "Humidity: N/A"
        self.invokeWebhookTrigger(event, val1, val2, val3, debug=debug)
        
