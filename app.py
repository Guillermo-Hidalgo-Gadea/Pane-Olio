import random
import yaml
import flask



app = flask.Flask(__name__)

# get menu from yaml file
with open('templates/cookbook.yaml', 'r') as f:
    menu_list = yaml.safe_load(f)


@app.route("/", methods = ['GET','POST'])
# this is the menu page
# show header and title

def index():
    print(flask.request.method)
    if flask.request.method =='POST':
        if flask.request.form.get("Today's Special", False) =="Today's Special":
            return flask.redirect("specials")
        if flask.request.form.get("In Season", False) =="In Season":
            return flask.redirect('https://www.regional-saisonal.de/saisonkalender-gemuese')
        if flask.request.form.get("See Cookbook", False) =="See Cookbook":
            return flask.redirect('/menu/')
        if flask.request.form.get("About", False) =="About":
            return flask.redirect("about")
        else:
            pass
    else:
        pass

    return flask.render_template('home.html')


@app.route("/specials/", methods = ['GET','POST'])
def specials():
    print(flask.request.method)
    special = menu_list[random.choice(range(len(menu_list)))]
    image = special['photo']
    if flask.request.method =='POST':
        if flask.request.form.get("Next Special", False) == "Next Special":
            special = menu_list[random.choice(range(len(menu_list)))]
        if flask.request.form.get("See Cookbook", False) =="See Cookbook":
            return flask.redirect('/menu/')
        if flask.request.form.get("Back", False) == "Back":
            return flask.redirect("/")
    else:
        pass

    return flask.render_template("specials.html", special = special)

@app.route("/seasonal/", methods = ['GET','POST'])
def season():
    pass

@app.route("/menu/", methods = ['GET','POST'])
def menu():
    if flask.request.method =='POST':
        if flask.request.form.get("Back", False) == "Back":
            return flask.redirect("/")
    else:
        pass
    return flask.render_template('menu.html', specials = menu_list)

@app.route("/about/", methods = ['GET','POST'])
def about():
    if flask.request.method =='POST':
        if flask.request.form.get("Back", False) == "Back":
            return flask.redirect("/")
    else:
        pass
    return flask.render_template('about.html')