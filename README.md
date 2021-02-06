# Black_Wings_Hacks

### Django with CockroachDB
*cockroach_example* directory is set up to work with CockroachDB.
It has a model with the fields mentioned in the doc.
If you run the web page, you can navigate to home, about, and user page.

I followed the steps in https://www.cockroachlabs.com/docs/stable/build-a-python-app-with-cockroachdb-django.html to set up cockroachDB and connect with django.

You may have to modify *settings.py* in *cockroach_example* directory to match your port number and username/password that is generated when you run
```
$ cockroach demo
```
(this is explained in detail in the link)
