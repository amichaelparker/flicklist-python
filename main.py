import webapp2


# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>FlickList</title>
</head>
<body>
    <h1>FlickList</h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""
movie_list = ['Star Wars', 'The Princess Bride']

class Index(webapp2.RequestHandler):
    """ Handles requests coming in to '/' (the root of our site)
        e.g. www.flicklist.com/
    """

    def get(self):

        movies = "<select name='old-movie'>"
        for movie in movie_list:
            movies += "<option>" + movie + "</option>"
        
        movies += "</select>"

        edit_header = "<h3>Edit My Watchlist</h3>"

        # a form for adding new movies
        add_form = """
        <form action="/add" method="post">
            <label>
                I want to add
                <input type="text" name="new-movie"/>
                to my watchlist.
            </label>
            <input type="submit" value="Add It"/>
        </form>
        """

<<<<<<< HEAD
        # TODO 1
        # Include another form so the user can "cross off" a movie from their list.
        remove_form = """
        <br><form action="/remove" method="post">
            <label>
                I want to remove """ + movies + """
                from my watchlist.
            </label>
            <input type="submit" value="Remove It"/>
        """

        # TODO 4 (Extra Credit)
        # modify your form to use a dropdown (<select>) instead a
        # text box (<input type="text"/>)

        to_watch = ""
        for title in movie_list:
            to_watch += "<li>" + title + "</li>"

        watchlist = """
        <br><h1>Current Watchlist:</h1>
            <ul>""" + to_watch + """</ul>
        """

        content = page_header + edit_header + add_form + remove_form + watchlist + page_footer
        self.response.write(content)


class AddMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/add'
        e.g. www.flicklist.com/add
    """

    def post(self):
        # look inside the request to figure out what the user typed
        new_movie = self.request.get("new-movie")
        movie_list.append(new_movie)
        # build response content
        new_movie_element = "<strong>" + new_movie + "</strong>"
        sentence = new_movie_element + " has been added to your Watchlist!"
        back = "<a href=\"/\"><button>Return to FlickList</button></a>"

        content = page_header + "<p>" + sentence + "</p>" + back + page_footer
        self.response.write(content)

=======
    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"
>>>>>>> ee0680d4f01c596f269cb7115563342042b763bd

# TODO 2
# Create a new RequestHandler class called CrossOffMovie, to receive and
# handle the request from your 'cross-off' form. The user should see a message like:
# "Star Wars has been crossed off your watchlist".
class CrossOffMovie(webapp2.RequestHandler):
    def post(self):
        old_movie = self.request.get("old-movie")
        old_movie_element = "<strike>" + old_movie + "</strike>"
        back = "<a href=\"/\"><button>Return to FlickList</button></a>"
        content = page_header + "<p>" + old_movie_element + \
                  " has been removed from your Watchlist!</p>" + back + page_footer

        self.response.write(content)
<<<<<<< HEAD
        movie_list.remove(old_movie)
=======
>>>>>>> ee0680d4f01c596f269cb7115563342042b763bd

# TODO 3
# Include a route for your cross-off handler, by adding another tuple to the list below.
app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/remove', CrossOffMovie)
], debug=True)
