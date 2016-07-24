from flask import Flask, render_template, request, redirect, flash, url_for
#from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""



   # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")

@app.route("/application-form")
def application_form():
    """ Displays the application form that the user fills in 
    """

    return render_template("application-form.html")


@app.route("/application-response", methods=["POST"])
def application():
    """ Processes the application form and returns user to the homepage
    with a confirmation that the form has been submitted """

    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    salary = request.form.get("salary")
    position = request.form.get("position")
    email = request.form.get("email")


    # *** This is for later when I want to redirect the user back to homepage 
    #       and flash them a success message ***


    # flash("Thank you for applying to be our future %s, %s %s. We will check".format(
    #     position, firstname, lastname) +
    #     " with accounting to see if we have enough funds to pay you the %d".format(
    #         salary) + " you are asking for.")
    # return redirect(url_for("/"))
    if firstname == "" or lastname == "" or salary == "":
        flash("The form is incomplete. Try again.")
        return render_template("application-form.html")
    else:    
        return render_template("application-response.html",
                                firstname=firstname,
                                lastname=lastname,
                                salary=salary,
                                position=position,
                                email=email)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    #DebugToolbarExtension(app)

    app.run(host="0.0.0.0", port=8081)

