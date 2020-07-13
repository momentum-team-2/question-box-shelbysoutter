# QuestionBox

You want to make an application where people can crowdsource their questions and get answers. You are going to build a web application that has these goals:

- Users can view questions and answers
- Registered users can ask questions
- Registered users can add answers to any question
- The question's creator can mark answers as correct
- Registered users can "star" questions and answers they like

## Getting started

This project has already been created from the Momentum Django template. You still need to run the following commands:

```
poetry install
cp questionbox/.env.sample questionbox/.env
poetry shell
./manage.py migrate
```

You also need to create a Django app -- use `core` for the name.

This project requires the use of [PostgreSQL](https://www.postgresql.org/) as its database, and must be deployed to [Heroku](https://www.heroku.com/). I suggest setting both of those up first thing.

## How questions and answers work

Questions have a title and a body. Allow your users to use [Markdown](https://en.wikipedia.org/wiki/Markdown) for authoring question bodies. [Python-Markdown](https://python-markdown.github.io/) can turn Markdown into HTML for you. You will also want to prevent people from putting unauthorized HTML into your Markdown code. Using [Bleach](https://bleach.readthedocs.io/en/latest/clean.html) and [bleach-whitelist](https://github.com/yourcelf/bleach-whitelist) should help with that. Questions cannot be edited once they have been asked. A question can be deleted by its author. If it is deleted, all associated answers should also be deleted.

Answers just have a body and are connected to a question. Answers can also use Markdown.

Every question and every answer should be associated with a user. A user should be able to view all their questions on a user profile page.

Users can search the site for questions. When they search, this should search the questions and all answers for them. This should use [PostgreSQL full-text search](https://docs.djangoproject.com/en/3.0/ref/contrib/postgres/search/).

## How much of this is JavaScript and Ajax?

"Starring" questions and answers and marking answers as correct should happen via Ajax and you will need to build a view that handles JSON to do this.

The rest of the application can be plain old Django views, although you can use JavaScript and Ajax if you want to enhance things. Answering a question is an excellent place to use Ajax if you get a chance.

## Making this project your own

You should try something you don't already know how to do on your project. This could be a Python or JavaScript library you haven't used before or a feature of Django you haven't tried.

Some ideas:

- Use [Django class-based views](https://docs.djangoproject.com/en/3.0/topics/class-based-views/) for the majority of your views (See also [Class-Based Views vs. Function-Based Views](https://simpleisbetterthancomplex.com/article/2017/03/21/class-based-views-vs-function-based-views.html) and [Classy class-based views](https://ccbv.co.uk/))
- When a user answers a question, the question's author receives an email with a link to the answer
- [Allow users to authenticate via Google or other third-party auth](https://www.intenct.nl/projects/django-allauth/)
- Users can have a profile image
