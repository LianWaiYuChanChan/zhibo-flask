==========================================
Zhibo web server based on Python and Flask
==========================================
.. sectnum::

.. contents:: Contents

Build Status
~~~~~~~~~~~~
.. image:: https://travis-ci.org/LianWaiYuChanChan/zhibo-flask.svg?branch=master
    :target: https://travis-ci.org/LianWaiYuChanChan/zhibo-flask

Introduction
~~~~~~~~~~~~
Use Python + Flask + Flask_restful to build a RESTful API servie.

Test
~~~~
- Test can use requests lib: http://flask-restful.readthedocs.io/en/0.3.5/quickstart.html#resourceful-routing
- post('http://localhost:5000/account', json = {"password":"123","username":"user_name"}).json()

References
~~~~~~~~~~
- https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful
- https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
- http://blog.luisrei.com/articles/flaskrest.html
- http://codehandbook.org/flask-restful-api-using-python-mysql/
- http://www.pythondoc.com/Flask-RESTful/quickstart.html
