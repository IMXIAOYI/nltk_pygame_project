**Read all of these instructions carefully before beginning!**

For this assignment, you will make a simple game that does the following:
* accepts a search term on the command line (e.g., a user should be able to run your game with `$ python mygame.py "Harry Potter"`)
* performs a search on wikipedia using that search term (e.g. "Harry Potter")
* takes the content of the top 5 pages returned by the search, and determines the most common adjectives across those pages
* draws a "ball" representing each of the top 6 adjectives
* allows the user to "pop" each balls by typing the first letter in the word contained in the ball

For a demo of how the game should work when it's complete, see [the demo video](https://www.youtube.com/watch?v=o7XdEKSpxEM).

Yes, that's a pretty arbitrary game. But it's a GREAT exercise to help us find out if 507 would be redundant for you. 

In order to complete this assignment, you will need to (probably quickly) figure out how to install and use three Python libraries that you most likely have never used (though if you have, it's somewhat likely that 507 is overkill for you): `wikipedia`, `nltk`, and `pygame`. 

You will also need to be reasonably conversant with Python data structures and be able to map a high-level program description into a working (relatively small) program design.

We have provided some starter code that demonstrates how to render stuff using pygame. You will have to add the following functionality:

* accepting command line arguments
* searching wikipedia
* using nltk to parse the contents of wikipedia pages
* drawing balls with the most common adjectives extracted from wikipedia pages
* allowing the user to delete balls using the keyboard
* when all balls are deleted, display game over screen

**Some pointers to get you started:**
* Use Python 3 (our solution uses Python 3.5.1; newer versions may also be OK)
* Use the latest NLTK (3.0) (see <http://www.nltk.org>)
* Use the latest wikipedia api for pytyon (1.4.0) (see <https://pypi.python.org/pypi/wikipedia/>)
* Use the latest pygame (1.9.1) (see <http://pygame.org/download.shtml>)
	* Note that on my MacBook Pro I was able to just `pip install pygame` and had no issues. I gather that Windows users may have a bit more of a struggle, but rest assured that pygame is popular enough that you ought to be able to find a solution online for your particular configuration. I would definitely recommend not waiting til the last minute on this; solving installation quandaries is part of what you will address in SI507, so if this is so hard as to be terrible, 507 is likely a good course for you to take! (If you have never heard of some of the concepts addressed here, you may want to consider enrolling in [SI 506]().)

**Notes:**
* Please don't use any *other* third-party libraries (our solution didn't need any others, so we know it should be possible). We need to run and grade many of these and expect to do so automatically, without going through other installations.
* If you already have a python installation on your machine with a bunch of libraries, etc., I strongly recommend you set up a [virtualenv](https://virtualenv.pypa.io/en/stable/) for this assignment to avoid any possible library conflicts.

**How to complete and submit this assignment:**
* *Fork* the repository that GitHub Classroom created for you.
* Edit the `wikipop-starter.py` Python file/add other files if needed. You should make at least 3 git commits to your project.
* Push all of your changes to your GitHub repository that you forked. 
* [Fill out the submission form](https://goo.gl/forms/5KhgvETRZG8dlZhM2) ONLY after you have completed your assignment and are ready for it to be graded. Your assignment will only be graded if you submit the form, and it can be graded any time after you submit the form.



