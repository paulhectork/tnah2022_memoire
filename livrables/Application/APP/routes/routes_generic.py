from flask import render_template, request
import json
import glob
import os

from ..app import app
from ..utils.main_functions import *
from ..utils.constantes import TEMPLATES, TEST
from ..utils.reconciliator import reconciliator
from ..utils.figmaker import figmaker_idx, figmaker_cat


# The index is generated when the app is launched.
created_index = create_index()


@app.before_first_request
def make_figidx():
    """
    create the figures to be displayed
    :return:
    """
    created_index = create_index()
    fig = figmaker_idx()
    return None


# ============ MAIN ROUTES ============ #
@app.route("/")
def home():
    """
    route for the homepage
    :return: render_template for the homepage
    """
    return render_template("pages/Home.html")


@app.route("/About_us")
def about_us():
    """
    route to see the About Us html page
    :return: render_template for the About Us html page
    """
    return render_template("pages/AboutUs.html")


@app.route("/Publications")
def publications():
    """
    route to see the bibliography produced by the project
    :return: render_template for the publications page
    """
    return render_template("pages/Publications.html")


@app.route("/Search", methods=['GET', 'POST'])
def search():
    """
    route to search the database by author name and manuscript date and see the results.
    the results can be accessed by sale or by manuscript. the results are reconciliated
    using reconciliator()
    :return: render_template for the search page
    """
    author = request.args.get('author')
    date = request.args.get('date')
    if author:
        results = reconciliator(author, date)
        for CAT in results["filtered_data"]:
            file = validate_id(CAT)
            doc = open_file(file)
            results["filtered_data"][CAT]["metadata"] = get_metadata(doc)
            results["filtered_data"][CAT]["cat_id"] = validate_id(CAT)
            results["filtered_data"][CAT]["desc_id"] = CAT
            results["filtered_data"][CAT]["text"] = get_entry(id_to_item(doc, CAT))
        return render_template('pages/Search.html', results=results, author=author)
    return render_template('pages/Search.html')


@app.route("/Index")
def index():
    """
    route to see an index of all the catalogues in the database ; at the beginning of
    the html page, different figures created with plotly can be accessed through a dropdown
    menu
    :return: render_template for the index page
    """
    # check if figures exist (as they should)
    figs = glob.glob(os.path.join(TEMPLATES, "partials", "fig_IDX*.html"))
    if len(figs) > 0:
        figpath = True
    else:
        figpath = False
    return render_template("pages/Index.html", figpath=figpath, index=created_index)


@app.route("/Katapi_documentation")
def katapi_documentation():
    """
    route to the API's documentation.
    first, we parse the examples of the API output to include them inside the API
    documentation page using jinja.
    :return: render_template to the documentation in HTML format
    """
    examples = {}  # dict to contain all the examples
    for fpath in glob.glob(f"{TEST}/api_output_examples/*"):
        fname = os.path.basename(fpath)

        with open(fpath, mode="r") as fh:
            # if it's a json, save it as a pretty printed string
            # if it's a xml, escape the opening and closing brackets
            if re.search(r"\.*?$", fname) == "json":
                examples[fname.replace(".", "_")] = json.dumps(json.load(fh), indent=4)
            else:
                examples[fname.replace(".", "_")] = fh.read()

    return render_template("pages/KatAPI.html", examples=examples)


@app.route("/View/<cat_id>")
def view(cat_id):
    """
    route to see the main page of a catalogue : description, link to the encoded catalogue,
    description and price of each item
    :param id: the @xml:id of the catalogue
    :return: render_template for the main catalogue
    """
    figpath = figmaker_cat(cat_id)  # create the visualisations for the current catalogue ; if there is price
    #                                  info on that catalogue, figpath is True; else, it is False
    file = validate_id(cat_id)
    doc = open_file(file)
    return render_template("pages/View.html", metadata=get_metadata(doc), content=get_entries(doc),
                           file=file, figpath=figpath, cat_id=cat_id)


# ============ AUXILIAIRY ROUTES ============ #
@app.route("/fig/<key>")
def fig_grabber(key):
    """
    route to build a url pointing to a figure to render in iframe in an html page
    :param key: key for the figure to retrieve
    :return: a render_template object pointing to the figure
    """
    return render_template(f"partials/fig_{key}.html")


"""
# To check if there is any memory leak.
from pympler import muppy, summary
@app.after_request
def report_memory(req):
    all_objects = muppy.get_objects()
    sum1 = summary.summarize(all_objects)
    summary.print_(sum1)
    return req
"""