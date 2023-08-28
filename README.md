# My First Flask Project
This is my first Flask project using Python. For any suggestions or comments, please email me at danisteelyart@gmail.com.


## Notes from tutorial
Below are the notes from the tutorial that I followed and from troubleshooting research that I intend to use as a reference for future projects
### Flask file structure and virtual environment
I followed [this tutorial][first tutorial] to troubleshoot some initial issues setting up the project, the virtual environment, and the file structure.

> In Flask you must know the basic file structure and for this we use single
> module file structure. When flask application gets complex the file 
> structure changes.

```
templates/
  - index.html
  - about.html
  - base.html
static/
  - css/
    - main.css
  - js/
    - main.js
app.py
requirements.txt
```

> In Flask templates is the folder where all the html files are included and
> static folder we can put our css and JavaScript files separately. app.py 
> file is the entry point or which starts the development server. 
> requirements.txt file will hold all the dependencies installed in the 
> project.

> Hint : To make the requirements.txt from installed dependencies

```
pip freeze > requirements.txt
```

[first tutorial]: https://yashodgayashan.medium.com/lets-make-a-flask-application-b4ba7a916cda