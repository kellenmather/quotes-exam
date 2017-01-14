# Quotes Exam
This was a timed test which required the following:
  1. Login/registration with validation
  2. User creation of quotes with validation
  3. The ability to favorite / un-favorite quotes
  4. A bank of quotes which populates all quotes minus the ones already favorited
  5. A page for each user that lists all quotes created by them as well as a number count of created quotes

# Pylot MVC (beta)
Pylot MVC is a lightweight MVC framework built in Python leveraging flask.

This framework is currently still in development. If you want to play around with it read on or clone the stable version!

# Installation

First make sure you have pip installed. If you don't have it installed there are great instructions here: https://pip.pypa.io/en/latest/installing.html

Next install virtualenv
```
sudo pip install virtualenv
```

Clone pylot
```
PARENT
git clone -b stable https://github.com/Ketul-Patel/Pylot.git
```

cd into pylot (or rename and cd in) and source the setup file
```
cd Pylot
. setup
FOLLOW DIRECTIONS OUTLINED BY SETUP!
note: there might be some fixes needed here, feel free to send them as FAQ's for this Readme (see below)
```

Now you can start your development server like so:
```
python manage.py runserver
```

Enjoy! More details/features coming soon!
