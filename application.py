import flask
import random

application = flask.Flask(__name__)

#Set application.debug=true to enable tracebacks on Beanstalk log output. 
#Make sure to remove this line before deploying to production.
application.debug=True

ascii_cats=["=^.^=",
    "=^..^=",
    ",,,^..^,,,~",
    "~(=^..^)",
    "(,,,)=(^.^)=(,,,)"
]

@application.route('/')
def index():
    return get_random_cat()

def get_random_cat():
    """ get a random cat from our ascii_cats collection """
    if ascii_cats:
        i =random.randint(0, len(ascii_cats)-1)
        return ascii_cats[i]
    else:
        return None

if __name__ == '__main__':
    application.run(host='0.0.0.0')
