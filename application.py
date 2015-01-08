# coding=utf-8
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
    "(,,,)=(^.^)=(,,,)",
    "/\o.o/\\",
"""
    /\___/\\
   (  o o  )
   /   *   \\
   \__\_/__/ meow!
     /   \\
    / ___ \\
    \/___\/
""",
"""
|\---/|
| o_o |
 \_^_/
""",
"""
   A_A
  (-.-)
   |-|
  /   \\
 |     |  __
 |  || | |  \___
  \_||_/_/
""",
"""
              a          a
             aaa        aaa
            aaaaaaaaaaaaaaaa
           aaaaaaaaaaaaaaaaaa
          aaaaafaaaaaaafaaaaaa
          aaaaaaaaaaaaaaaaaaaa
           aaaaaaaaaaaaaaaaaa
            aaaaaaa  aaaaaaa
             aaaaaaaaaaaaaa
  a         aaaaaaaaaaaaaaaa
 aaa       aaaaaaaaaaaaaaaaaa
 aaa      aaaaaaaaaaaaaaaaaaaa
 aaa     aaaaaaaaaaaaaaaaaaaaaa
 aaa    aaaaaaaaaaaaaaaaaaaaaaaa
  aaa   aaaaaaaaaaaaaaaaaaaaaaaa
  aaa   aaaaaaaaaaaaaaaaaaaaaaaa
  aaa    aaaaaaaaaaaaaaaaaaaaaa
   aaa    aaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaa
     aaaaaaaaaaaaaaaaaaaaaaaaa
"""
]

@application.route('/')
def index():
    cat = get_random_cat()
    return """
    <html>
      <head><meta charset="UTF-8"></head>
    <body>
    <pre>{0}</pre>
    </body></html>
    """.format(cat)

def display_all_cats():
    for c in ascii_cats:
        print c

def get_random_cat():
    """ get a random cat from our ascii_cats collection """
    if ascii_cats:
        i =random.randint(0, len(ascii_cats)-1)
        return ascii_cats[i]
    else:
        return None

if __name__ == '__main__':
#    display_all_cats()
    application.run(host='0.0.0.0')
