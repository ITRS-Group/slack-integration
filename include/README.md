# Slack Integration Include file
The ability to automated geneos alert messages into your Slack environment.

### Overview

##### Slack Webhook url

Generated your Slack webhook url. Which can be found [here](https://api.slack.com/incoming-webhooks). Should be in the `https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/xxxxxxxxxxxxxxxxx` format.

##### Geneos Framework (4.0 or higher)

You may need to FTP the script. Just be sure to have the script somewhere that is accessible on the server for your Gateway to execute.

  + Step 1 - Right click on the desired gateway for your script, and click on “Configure”.

  + Step 2 - With the Gateway Setup Editor opened, with in the Actions section, configure your path to the script. Here you can supply Slack’s `webhook_url` as a command-line option.

  + Step 3 - Configure your rule to use `Slack_Call` example

  + Step 4 - Configure the `Slack` Environment table to your slack webhook settings
