#!/usr/bin/env bash

deploy() {

  
  echo "Deploying slackYeezy cloud function."
  gcloud beta functions deploy slackYeezy --source functions/slackYeezy/ --runtime python37 --trigger-http --entry-point=handleRequest --project $APP_PROJECT

  echo "all the things deployed!!! _o/"
}

main() {
  deploy
}

main
