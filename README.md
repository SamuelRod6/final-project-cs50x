# TranslateAll
#### Video Demo: <URL>
#### Description:
TranslateAll is a Spanish to English, and English to Spanish translator created with Flask, styled with Bootstrap 5, scripts with jQuery and deployed on Heroku using Git and Github. This is made up of different parts:

Templates (HTML files):

* index.html: On the main page of the application, there is the form for the text to be translated, a selection of the input language, a disabled text box for the translation of the text, and a submit button. Using Bootstrap 5 to style each of the components, Jinja blocks to be able to modify moving parts and a "flash" alert to explain the correct use. At the end of this, there is a jQuery script that modifies the DOM of the page and turns the submit button into a disabled upload button to avoid more requests while the form is being submitted.
* translated.html: This page is an extension of "index.html", in which the result of the previous request is shown using the Jinja syntax, it maintains the written text, the translated text and the previously selected language.

app.py:

In this file is the Flask Python application, making use of the "googletrans" library, it receives input from the user and translates it into the desired language.

It can be highlighted that a Flexbox method was used with Bootstrap 5, giving it a responsive design, capable of adapting to any screen and device resolution.

Application link: http://translateall.herokuapp.com/