Polls
-------
Polls is  a django app to conduct web-based polls. For each question,
visitors can choose between a fixed number of choices.

Detailed documentation is in the "docs" directory.

Quick Start
-----------

1. Add "polls" to your INSTALLED_APPS settings like this::

INSTALLED_APPS = [
    ...
    'polls'
]

2. Include polls URLconf in your project urls.py like this::
path('polls/', include('polls.urls')),

3. Run `` python manage.py migrate`` to crete the polls models.
4. Start the development server and visit http:// 127.0.0.1:8000/admin/
to create a poll (you'll need the admin app enabled).
5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.