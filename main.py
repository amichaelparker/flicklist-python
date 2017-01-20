import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movieList = ["The Big Lebowski", "The Matrix", "The Princess Bride", "Edge of Tomorrow", "Groundhog Day"]

        # TODO: randomly choose one of the movies, and return it
        pick = movieList[int(random.random() * len(movieList))]
        return pick

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        tomorrow = self.getRandomMovie()
        if tomorrow == movie:
            while tomorrow == movie:
                tomorrow = self.getRandomMovie()

        content += "<br><h1>Tomorrow's Movie</h1>"
        content += "<p>" + tomorrow + "</p>"

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
