# twitter-bot-skeleton

This github repo stands a simple starting point to get a twitter bot built on AWS Lambda started. It contains 3 main components:

1. A simple python function that will be used with AWS Lambda
1. A SAM template that defines an AWS Lambda function invoked on a schedule
1. A requirements.txt file that has all of the required dependencies needed to talk to twitter. We will be using the [python-twitter](https://python-twitter.readthedocs.io/en/latest/) library to read and respond to twitter message on the platform.
