# Put your app in here.
#Calc
# Build a simple calculator with Flask, which uses URL query parameters to get the numbers to calculate with.

# Make a Flask app that responds to 4 different routes. Each route does a math operation with two numbers, a and b, which will be passed in as URL GET-style query parameters.

# /add
# Adds a and b and returns result as the body.
# /sub
# Same, subtracting b from a.
# /mult
# Same, multiplying a and b.
# /div
# Same, dividing a by b.
# For example, a URL like http://localhost:5000/add?a=10&b=20 should return a string response of exactly 30.

# Write the routes for this but don’t hardcode the math operation in your route function directly. Instead, we’ve provided helper functions for this in the file operations.py:
from flask import Flask, request

from operations import add, sub,mult,div
app = Flask(__name__)

@app.route('/<operator>')
    

def result_num(operator):

    num1 = int(request.args.get("a"))
    num2 = int(request.args.get("b"))
    
    return str(eval(operator)(num1,num2))

# Further Study
# You probably have a lot of code duplication in your calc routes, given that you’re doing such similar things in each.

# Make a single route/view function that can deal with 4 different kinds of URLs:

# /math/add
# /math/sub
# /math/mult
# /math/div
# You can write this in one function with one route by using a route parameter for the actual operation (“add”, “sub”, etc).

# As an extra-bonus, see if you can find a way to do this in the route without a whole series of if/elif statements. One good way is to use a dictionary to map operation names to the functions that do the underlying math.

@app.route('/math/<operator>')
def result2_num(operator):
    """For the sake of passing all the tests"""

    num1 = int(request.args.get("a"))
    num2 = int(request.args.get("b"))
    
    return str(eval(operator)(num1,num2))
