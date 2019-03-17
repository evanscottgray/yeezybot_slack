# yeezybot_slack

run locally:
```
git clone git@github.com:evanscottgray/yeezybot_slack.git
cd functions/slackYeezy/
python3 -m venv ./venv/
source venv/bin/activate
pip3 install -r requirements.txt
python3 main.py

curl 127.0.0.1:5000/kanye
{"attachments":[{"text":"I feel like I'm too busy writing history to read it."}],"response_type":"in_channel","text":"I miss the old kanye.","username":"KanyeBot"}
```

optionally publish a port with something like ngrok to test with slack:
```
ngrok http 5000
```

optinally publish to google cloud functions:
1. create new project by going to https://console.cloud.google.com/projectcreate
2. name project, setup billing (dont worry unless your slack is YUUUGE you'll be fine)
3. install gcloud cli using directions [here](https://cloud.google.com/sdk/docs/#install_the_latest_cloud_tools_version_cloudsdk_current_version)
4. use your project name to deploy the app with the deploy script: `APP_PROJECT=MY-PROJECT-NAME ./deploy.sh`, once command is done, note the https url, you'll need it

setup slack app:

1. visit https://api.slack.com/apps/new
2. name app, select your favorite workspace, and create app
3. go to "slash commands", create new command
4. add in url from ngrok, or from google cloud functions, add /command like /kanye or something, then save
5. go test.

optional: go to bot configuration and add a cool icon.

![slack](https://user-images.githubusercontent.com/1891697/54496375-960d0d00-48bc-11e9-9ed3-1a01dde75480.png)

special thanks to ajzbc who makes this possible with kanye.rest: https://github.com/ajzbc/kanye.rest
