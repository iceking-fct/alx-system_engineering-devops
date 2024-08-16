# Overview #

## Background Context ##
Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.

I love this!!!
---

## Learning Objectives ##
At the completion of this project, we are expected to have full understanding of thefollowing:

- How to read API documentation to find the endpoints you’re looking for
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value


## Folder Details ###

-Author: MIRACLE AMAJAMA (https://github.com/iceking-fct)

-Date Created: Wednesday 14 August, 2024.

-Project Timeline:
	- Project will start Aug 13, 2024 6:00 AM, must end by Aug 14, 2024 6:00 AM
	- Checker was released at Aug 13, 2024 12:00 PM
	- An auto review will be launched at the deadline



## General Requirements ##
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all  files should be exactly #!/usr/bin/python3
- Libraries imported in your Python files must be organized in alphabetical order
- A README.md file, at the root of the folder of the project, is mandatory
- Code should use the pycodestyle (version 2.8.*)
- All files must be executable
- The length of files will be tested using wc
- All modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- Must use `get` to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- All code should not be executed when imported (by using if __name__ == "__main__":)~


## Reference Resources ##
- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Query String](https://en.wikipedia.org/wiki/Query_string)




## Files ###
- *Here is a detailed list of all files in the repo and their description*.

| SN | File | Description                                   |
|----|------|-----------------------------------------------|
| 1. | [0-subs.py](https://www.github.com) | A function that queries the **Reddit API** and returns the number of subscribers (not active users but total subscribers) for a given subreddit. If an invalid subreddit is given, the function returns 0.<br>**Hint:* *No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.* <br/><br/>Requirements:<br/><ul><li>Prototype: def number_of_subscribers(subreddit)</li><li>If not a valid subreddit, return 0.<br/>**NOTE:** *Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.*|
