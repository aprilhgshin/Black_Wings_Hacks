# Black_Wings_Hacks
<img src="./images/GapShift_01.png">
## Inspiration
The gender wage gap still exists in the US (and beyond). According to Business Insider, on average a woman working full time in 2018 made 81.6 cents for every dollar a man working full time made. The wage gap is even wider when accounting for race; Black women make just 66% of what white men make and Hispanic women make just 58%. The pay gap is also more severe in certain locations.
https://www.businessinsider.com/gender-wage-pay-gap-charts-2017-3

## What it does
Our webapp combats the wage gap by providing salary info that takes into account demographic information as well as job title, location, level of experience, and company. People can come to the site to identify what companies and locations have balanced wages. Additionally, they can use the information from the site to help with negotiating their salary, especially if they see discrepancies that may be the result of demographic bias. Our users will be able to _pay it forward_ (pun intended) by anonymously reporting their salary, employment, and demographic info whenever they have a new job or promotion. 

## How we built it
The front end was built using React.js and the backend was built using python, Django, and CockroachDB.

## Challenges we ran into
Everyone on the team was new to CockroachDB so that took some getting used to. It was also challenging to connect the front end and back end.

## Accomplishments that we're proud of
We initiated the CockroachDB with sample data and set it up to receive future form input. The UI has a very inviting, clean look.

## What we learned
We learned how to use django dataframes with CockroachDB. 

## What's next for GapShift
We would like to import/scrape any existing databases that have salary information to include more data for our users. We will deploy the website and connect with individuals to grow the GapShift community. Many companies thrive off the taboo about discussing salary, but we are here to end that and make sure people are being paid according to their work ethic and talent.

## Domain names for GapShift:
ClosingTheGapIn.Tech
PayItForward.Online


### For DEVELOPERS
### Django with CockroachDB
*cockroach_example* directory is set up to work with CockroachDB.
It has a model with the fields mentioned in the doc.
If you run the web page, you can navigate to home, about, and user page.

I followed the steps in https://www.cockroachlabs.com/docs/stable/build-a-python-app-with-cockroachdb-django.html to set up cockroachDB and connect with django.

You may have to modify _settings.py_ in _cockroach_example_ directory to match your port number and username/password that is generated when you run

```
$ cockroach demo
```

(this is explained in detail in the link)
