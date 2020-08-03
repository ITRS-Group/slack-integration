#!/usr/bin/python
import requests, base64, json, sys, argparse, os, time
from argparse import RawTextHelpFormatter

if sys.version_info[0] < 3:
    import urllib2
else:
    import urllib3

#Loads the environment variable as JSON structure
#We will use this later
JSON_Data = json.dumps(dict(**os.environ), sort_keys=True, indent=4)
EnvData_dict = json.loads(JSON_Data)

# Variables needed
# EnvData_dict["_SLACK_CHANNEL"]
# EnvData_dict["_SLACK_BOTNAME"]
# EnvData_dict["_SLACK_HOOK"]
# EnvData_dict["_SLACK_MSG_RECEIPT"]
fdmgkojevfht43h8tbv54yn89540v6yj45t9utgf4e3vf6y-mgdfujhigretngkrednfdrged
hrt
rtyuytrjytjyrjihtrey7543vih9er5ydf
fdmgkojevfht43h8tbv54yn89540v6yj45t9utgf4e3vf6y-mgdfujhigretngkrednfdrgedhtr5b8yb954uhgbe

fudfsdfrdtv

parser = argparse.ArgumentParser( description = "Outbound SlackBot Integration" , formatter_class=RawTextHelpFormatter)

# Typical operations for PagerDuty
parser.add_argument( "-wh", "--webhook", help = "Webhook URL for sending message to",  type=str)
parser.add_argument( "-ch", "--channel", help = "Slack Channel or user for sending message to",  type=str)

# global args
args = parser.parse_args()

if (args.webhook):
    webhook_url =  (args.webhook)
else:
    webhook_url =  EnvData_dict["_SLACK_HOOK"]

if (args.channel):
    channel =  (args.channel)
else:
    channel =  EnvData_dict["_SLACK_CHANNEL"]

if "_SLACK_BOTNAME" in EnvData_dict:
    botname = EnvData_dict["_SLACK_BOTNAME"]
else:
    botname = 'Geneos_Slack_Alerts'

#Building a Slack Pre-Reqs and the message
Addressed_Channel_Msg = ("{\"channel\":\"" + channel + "\", "
"\"username\":\"" + botname + "\", "
"\"attachments\":[ ")

# Time should be handled as so, YYYY-MM-DD
# OK Bot Message
OK_Msg = ("{" + \
"\"fallback\": \"Alert - " + EnvData_dict["_SEVERITY"] + "\", " + \
"\"color\": \"good\", " + \
"\"fields\":" + \
"[" + \
"{" + \
"\"title\": \"Severity : " + EnvData_dict["_SEVERITY"] + " | Date : " + time.strftime("%Y-%m-%d") +  " | Time : " + time.strftime("%H:%M:%S") +  "\", " + \
"\"value\": \"Value : " + EnvData_dict["_VALUE"] + "\n" + "Row.Column : " + EnvData_dict["_VARIABLE"] + "\n" + "Gateway : " + EnvData_dict["_GATEWAY"] + "\n" + \
"Probe : " + EnvData_dict["_PROBE"] + "\n" + "Sampler : " + EnvData_dict["_SAMPLER"] + "\n" + "Managed Entity : " + EnvData_dict["_MANAGED_ENTITY"] + \
 "\", " + \
"\"short\": false " + \
"}" + \
"]" + \
"}")

# Warning Bot Message
WARNING_Msg = ("{" + \
"\"fallback\": \"Alert - " + EnvData_dict["_SEVERITY"] + "\", " + \
"\"color\": \"warning\", " + \
"\"fields\":" + \
"[" + \
"{" + \
"\"title\": \"Severity : " + EnvData_dict["_SEVERITY"] + " | Date : " + time.strftime("%Y-%m-%d") +  " | Time : " + time.strftime("%H:%M:%S") +  "\", " + \
"\"value\": \"Value : " + EnvData_dict["_VALUE"] + "\n" + "Row.Column : " + EnvData_dict["_VARIABLE"] + "\n" + "Gateway : " + EnvData_dict["_GATEWAY"] + "\n" + \
"Probe : " + EnvData_dict["_PROBE"] + "\n" + "Sampler : " + EnvData_dict["_SAMPLER"] + "\n" + "Managed Entity : " + EnvData_dict["_MANAGED_ENTITY"] + \
 "\", " + \
"\"short\": false " + \
"}" + \
"]" + \
"}")

# Critical Bot Message
CRITICAL_Msg = ("{" + \
"\"fallback\": \"Alert - " + EnvData_dict["_SEVERITY"] + "\", " + \
"\"color\": \"danger\", " + \
"\"fields\":" + \
"[" + \
"{" + \
"\"title\": \"Severity : " + EnvData_dict["_SEVERITY"] + " | Date : " + time.strftime("%Y-%m-%d") +  " | Time : " + time.strftime("%H:%M:%S") +  "\", " + \
"\"value\": \"Value : " + EnvData_dict["_VALUE"] + "\n" + "Row.Column : " + EnvData_dict["_VARIABLE"] + "\n" + "Gateway : " + EnvData_dict["_GATEWAY"] + "\n" + \
"Probe : " + EnvData_dict["_PROBE"] + "\n" + "Sampler : " + EnvData_dict["_SAMPLER"] + "\n" + "Managed Entity : " + EnvData_dict["_MANAGED_ENTITY"] + \
 "\", " + \
"\"short\": false " + \
"}" + \
"]" + \
"}")

# Close the message
Close_Msg = "]}"

#After grabbing the environment variables
#Check on the severity environment variable and
#form the message.
if (EnvData_dict["_SEVERITY"] == "WARNING"):
    Send_Msg = Addressed_Channel_Msg + WARNING_Msg + Close_Msg
if (EnvData_dict["_SEVERITY"] == "OK"):
    Send_Msg = Addressed_Channel_Msg + OK_Msg + Close_Msg
if (EnvData_dict["_SEVERITY"] == "CRITICAL"):
    Send_Msg = Addressed_Channel_Msg + CRITICAL_Msg + Close_Msg

# We're using Slack JSON API
# Doing our POST to the URL
# Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
# webhook_url =  EnvData_dict["_SLACK_HOOK"]
# webhook_url = 'https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/xxxxxxxxxxxxxxxxx'

#Here we will build the response
response = requests.post( webhook_url, data=Send_Msg, headers={'Content-Type': 'application/json'} )

# Writing the whole Env Vars to file for sanity checks
if "_SLACK_MSG_RECEIPT" in EnvData_dict:
    #We're grabbing attributes at a granular level
    # f = open('/export/home/epayano/geneos/scripts/environ.json', 'w')
    f = open(EnvData_dict["_SLACK_MSG_RECEIPT"], 'w')
    # f.write( EnvData_dict["App"] )
    f.write('\n')
    #Write out the metadata
    f.write(JSON_Data)
    #JSON Array Size
    f.write('\n')
    f.write('JSON array length is : ')
    #size of the array convert to string
    f.write(str(len(EnvData_dict)))
    f.write('\n')
    #Server Response
    f.write('server status_code : ')
    f.write(str(response.status_code))
    f.write('\n')
    f.write('server reason : ')
    f.write(str(response.reason))
    f.write('\n')
    f.write('server response text : ')
    f.write(str(response.text))
    f.write('\n')
    #Close the file up
    f.close()

if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
