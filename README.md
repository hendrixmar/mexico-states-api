# Mexico states API
## _A Trie to search_



[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This API filter the different states from Mexico depending your input. The filter is case insensitive and it even search by suffix pattern.




## Dependency

The API is works with the following libraries

- [Flask] - Micro web framework written in Python
- [suffix-tree] - A Generalized Suffix Tree for any Python iterable, with Lowest Common Ancestor retrieval.
- [pytest] -  Testing tool that helps you write better programs.


## DEMO

If you want to test this api you can try by using this link and replacing the filter parameter a location name

https://mexico-states-api.herokuapp.com/filter/***filter***


## Installation

You need [Python](https://nodejs.org/) 3.8 or above to run.

Install the dependencies that are the in the requirement file

```sh
cd MoscowRingRoad
pip install requirements.txt
```



## Docker

It is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. In my case I had to modify the port number by getting it from 
the environment variable in Heroku

````python
from flask import Flask
import os    

app = Flask(__name__)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
````



```shell
docker build -t <your username>/flask-docker .
```
```shell
docker run -it -p 2000:5000 <your username>/flask-docker
```
I deployed the application to Heroku. If you want to use the same platform create your account and execute the following commands. Deploying in heroku is pretty straightforward.

```shell
heroku login
```
```shell
heroku create <app-name>
```
```shell
heroku container:push web --app <app-name>
```
```shell
heroku container:release web --app <app-name>
```
If you want to access to the logs file of the Docker container use the following command.
```shell
heroku run bash
```

## How it works?

To solve this problems I used the Ukkonen's algorithm.
The Ukkonen's algorithm is a method of constructing the suffix tree of a string in linear time. Suffix trees are useful because they can efficiently answer many questions about a string, such as how many times a given substring occurs within the string. 
For this prooject I used the suffix tree package.
If you want to heard a more detailed explanatation of how the algorithm works you can read this [stackoverflow post](https://stackoverflow.com/questions/9452701/ukkonens-suffix-tree-algorithm-in-plain-english).

## License

MIT

**Free Software, holly **

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Flask]: <https://github.com/pallets/flask>
   [numpy]: <https://github.com/numpy/numpy>
   [suffix-tree]: <https://pypi.org/project/suffix-tree/>
   [pytest]: <https://github.com/pytest-dev/pytest>
   [requests]: <https://github.com/psf/requests>
   [python]: <>
   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
