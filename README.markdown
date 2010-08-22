# Convertly
This repo contains the source code for [Convertly](http://convertly.com/), a web based GUI for a DOCX to XHTML conversion library called [Zombie](http://github.com/kaptainlange/zombie/).

It's written in Python and uses Django. [requirements.txt](http://github.com/thomasw/convertly/blob/master/requirements.txt) lists the specific Python libraries that are required.

## Setting up Your Development Environment
Using [pip](http://pypi.python.org/pypi/pip) + [virtualenv](http://pypi.python.org/pypi/virtualenv) is a really good idea. If you're doing things that way already, setup a new virtual environment and use the [requirements.txt](http://github.com/thomasw/convertly/blob/master/requirements.txt) file to install the necessary libraries. If you're not, check out Eliot's [PIP + virtualenv crash course](http://www.saltycrane.com/blog/2009/05/notes-using-pip-and-virtualenv-django/).

If you don't want to use virtualenv, you can do things this way using only pip:

    > git clone git://github.com/thomasw/convertly.git
	> cd convertly/
    > sudo pip install -r requirements.txt
	> cp local_settings.template.py local_settings.py

Configure local_settings.py file to your liking and then do the following to fire up your development server:

	> ./manage.py runserver

After that, Convertly should be accessible to you [here](http://127.0.0.1:8000), but you probably already knew that.
    
## Everything else
Copyright (c) [Thomas Welfley](http://cyproject.net/) and [Jared Lang](http://github.com/kaptainlange/). See [LICENSE](http://github.com/thomasw/convertly/blob/master/LICENSE) for details.
