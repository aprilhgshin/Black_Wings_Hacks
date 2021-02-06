# Black_Wings_Hacks

### Django with default sqlite: 
Inside the *blackwingshacks* directory, the *user_data* directory is a demonstration of djanga framework that works with sqlite. 

For demonstration, feel free to manually add a few entries after running the command:
```
$ python3 manage.py shell
```
Then, if you run 
```
$python3 manage.py runserver
```
and navigate to *user_data* on the webpage, you'll see the user input example displayed. 


### Django with CockroachDB (in progress)
*cockroach_example* directory is set up to work with CockroachDB.

I followed the steps in https://www.cockroachlabs.com/docs/stable/build-a-python-app-with-cockroachdb-django.html 

You may have to modify *settings.py* in *blackwingshacks* directory to match your port number and username/password that is generated when you run 
```
$ cockroach demo 
```
(this is explained in detail in the link)

The problem I'm having now is that the command *makemigrations* runs indefinitely. There might be an issue with connecting to the cockroachdb server. 
