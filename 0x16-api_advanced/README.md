# 0x16. API advanced
***

## General
***
* How to read API documentation to find the endpoints you’re looking for
* How to use an API with pagination
* How to parse JSON results from an API
* How to make a recursive API call
* How to sort a dictionary by value

## Requeriments
***
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* Libraries imported in your Python files must be organized in alphabetical order
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* You must use the Requests module for sending HTTP requests to the Reddit API

## Tasks
***
#### 0. How many subs?
Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.
Requirements:
* Prototype: def number_of_subscribers(subreddit)
* If not a valid subreddit, return 0.
* NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

#### 1. Top Ten
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
Requirements:
* Prototype: def top_ten(subreddit)
* If not a valid subreddit, print None.
* NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

#### 2. Recurse it!
Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.
Hint: The Reddit API uses pagination for separating pages of responses.
Requirements:
* Prototype: def recurse(subreddit, hot_list=[])
* Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.
* If not a valid subreddit, return None.
* NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)
