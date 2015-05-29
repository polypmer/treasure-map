###########################################################################
# Copyright (C) 2015 Fenimore Love <fenimore@polypmer.com>
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# See https://github.com/polypmer/things
###


# import the Flask class from the flask module
from flask import Flask, render_template
import stuff, mappify

# create the application object
app = Flask(__name__)

stuffs = []
        
# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('accueil.html')

@app.route('/<location>/<int:quantity>')
def welcome(location, quantity):
    stuffs = stuff.gather_stuff(location, quantity)
    # Somehow iterate the dict construction? Yeah.. that.
    things = [ # Array of first five Dicts
        {
            'url': stuffs[0].url, 
            'image': stuffs[0].image, 
            'place': stuffs[0].location,
            'title': stuffs[0].thing
        },
        {
            'url': stuffs[1].url,
            'image': stuffs[1].image,
            'place': stuffs[1].location,
            'title': stuffs[1].thing
        },
        {
            'url': stuffs[2].url, 
            'image': stuffs[2].image,
            'place': stuffs[2].location,
            'title': stuffs[2].thing
        },
        {
            'url': stuffs[3].url, 
            'image': stuffs[3].image,
            'place': stuffs[3].location,
            'title': stuffs[3].thing
        },
        {
            'url': stuffs[4].url, 
            'image': stuffs[4].image,
            'place': stuffs[4].location,
            'title': stuffs[4].thing
        },
                {
            'url': stuffs[5].url, 
            'image': stuffs[5].image,
            'place': stuffs[5].location,
            'title': stuffs[5].thing
        },
        {
            'url': stuffs[6].url, 
            'image': stuffs[6].image,
            'place': stuffs[6].location,
            'title': stuffs[6].thing
        },
        {
            'url': stuffs[7].url, 
            'image': stuffs[7].image,
            'place': stuffs[7].location,
            'title': stuffs[7].thing
        },
        {
            'url': stuffs[8].url, 
            'image': stuffs[8].image,
            'place': stuffs[8].location,
            'title': stuffs[8].thing
        },
    ]
    ### Not quite worked out yet ^^^
    
    # Pass the thing snippets into five different instances
    # of the same template with respective var
    return render_template('view_template.html', things=things, location=location)  # render a template
    # location = location... brilliant
    
@app.route('/<location>/map')
def show_map(location):
    place = location
    stuffs = stuff.gather_stuff(location, 9)
    try:
        mappify.post_map(stuffs)
    except:
        print("something when wrong")
    return render_template('map_template.html', location=place)

@app.route('/<location>/map/<int:quantity>')
def show_more_map(location, quantity):
    place = location
    quantity -= 1
    stuffs = stuff.gather_stuff(location, quantity)
    mappify.post_map(stuffs)
    return render_template('map_template.html', location=place)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run()
    
    
    
""" 
HTML snippets for future reference:
          {% for thing in things %}
          <div>
            <h4>{{ thing.place.title() }}</h4>
            <img href ={{ thing.url }} 
                src= {{ thing.image }} width="160" height=auto>
          </div>
          {% endfor %}
"""

