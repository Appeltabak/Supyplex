Supyplex
========
Supyplex is a Python clone of famous video game [Supaplex][1]. The original 
game was created in 1991 by Philip Jespersen en Micheal Stopp. This clone is
more a project to learn from rather than being a full working clone.

Installation
-------------
This game uses Python 2.7.x. Install all dependecies in an virtualenv:

    virtualenv .env/
    source .env/bin/activate
    pip install -r requirements.txt

Usage
-----
Run it by:

    pynt run

If you want it run in it develop mode:

    pynt "run=[env=dev]"

Other options:

    $ pynt -l
    Tasks in build file build.py:
    build_doc                Build documentation with Sphinx. 
    run           [Default]  Run Supyplex. 
    tests                    Run unit tests. 

    Powered by pynt 0.8.0 - A Lightweight Python Build Tool.

ToDo
----
Everything, except writing [README.md].

[1]:http://en.wikipedia.org/wiki/Supaplex
[2]:README.md
