# Mexico states API
## _A Trie to search_



[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This API filter the different states from Mexico depending on your input. The filter is case insensitive and it even searches by suffix pattern.




## Dependency

The API works with the following libraries

- [Flask] - Micro web framework written in Python
- [suffix-tree] - A Generalized Suffix Tree for any Python iterable, with Lowest Common Ancestor retrieval.
- [pytest] - A testing tool that helps you write better programs.


## DEMO

If you want to test this API you can try by using this link and replacing the filter parameter with the string you want to search:

https://mexico-states-api.herokuapp.com/filter/***filter***

If you want to return all the states just enter this link:

https://mexico-states-api.herokuapp.com/

## Installation

You need [Python](https://nodejs.org/) 3.8 or above to run.

Install the dependencies that are in the requirement file

```sh
cd mexico-states-api
pip install requirements.txt
```



## Docker

It is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. In my case, I had to modify the port number by getting it from 
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
I deployed the application to Heroku. If you want to use the same platform create your account and execute the following commands. Deploying in Heroku is pretty straightforward.

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

To solve this problem I used Ukkonen's algorithm.
Ukkonen's algorithm is a method of constructing the suffix tree of a string in linear time. Suffix trees are useful because they can efficiently answer many questions about a string, such as how many times a given substring occurs within the string. The complexity of this algorithm is O(N) so it gives us the possibility to scale up the number of states without affecting the performance.
For this project, I used the suffix tree package.
If you want to hear a more detailed explanation of how the algorithm works you can read this [stackoverflow post](https://stackoverflow.com/questions/9452701/ukkonens-suffix-tree-algorithm-in-plain-english).

## License

MIT

**Free Software, holly **



   [Flask]: <https://github.com/pallets/flask>

   [suffix-tree]: <https://pypi.org/project/suffix-tree/>
   [pytest]: <https://github.com/pytest-dev/pytest>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
