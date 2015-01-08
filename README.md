# cats
An Web Application providing the world with ASCII Cats.

I wanted to play around with AWS, Elastic Beanstalk, and deploying web applications to The Cloud. Sure, I could do the 
typical 'hello world' example... but I wanted something difference.

## Example App

So, fine then. Here's a [flask](http://flask.pocoo.org/) web application that responds to requests with an ascii cat, 
picked at random from a list. The app is deployed using elastic beanstalk, which sets up an auto-scaling, fault-tolerant, 
cloud-based, 21st century application environment using all the latest in metrics, notification, and all those bells and whistles.
All quite ridiculous, really.

To see this amazing app in action, there's a deployment at [cats.meancat.com](http://cats.meancat.com), at least until I get bored and shut the
EB environment down.

## Inspiration

The [Pushbullet API](https://docs.pushbullet.com/http/) returns a JSON response if an error has occurred:
> * type - A machine-readable code to refer to this type of error. Either invalid_request for client side errors or server for server side errors.
> * message - A (mostly) human-readable error message.
> * param - (OPTIONAL) Appears sometimes during an invalid_request error to say which parameter in the request caused the error.
> * cat - Some sort of ASCII cat to offset the pain of receiving an error message.

Example:

    {
      "error": {
          "message": "The resource could not be found.",
          "type": "invalid_request",
          "cat": "~(=^‥^)"
      }
    }

And I thought, 'if only there was a web service to generate all those ascii cats....' which is a ridiculous thought to have..
but there you go.
