# Cron parser 

A command line application or script which parses a cron string and expands each field
to show the times at which it will run.



## First time setup

Clone the repository
```
    git clone https://github.com/theNullP0inter/cron-parser.git
```

There are 2 ways to run this code on your system


### Using Python

* Install Python3

* Install poetry
    ```
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
    ```
* Install `virtualenv` using `pip3 install virtualenv`
* Create a new virtual environment `virtualenv .venv`
* Activate virtual environment `source .venv/bin/activate`
* Install dependencies
    ```
        cd cron-parser && poetry install
    ```
* Run the script to describe the cronjob
    ```
        poetry run describe "<your_cron_string>"
        
        # poetry run describe "*/15 0 1,15 * 1-5 /usr/bin/find"

    ```

* Run unit tests using
    ``` 
        poetry run pytest
    ```



### Using Docker

* Build a new image
    ```
        cd cron-parser && docker build -t cron-parser .
    ```
* Run the script to describe the cronjob
    ```
        docker run cron-parser poetry run describe "<your_cron_string>"

        # docker run cron-parser poetry run describe "*/15 0 1,15 * 1-5 /usr/bin/find"
    ```

* Run unit tests using
    ```
        docker run cron-parser poetry run pytest
    ```