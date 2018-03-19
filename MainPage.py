import inverted_indexing
import pickle

from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/")
def first_page():
    return render_template("index.html")


@app.route("/result", methods=["GET","POST"])
def result_page():
    doc_data = request.form["doc_data"]
    # inverted_index = inverted_indexing.create_inverted_index()
    # with open("my_index.txt", "wb")as my_index:
    #     pickle.dump(inverted_index, my_index)
    with open("my_index.txt", "rb") as myFile:
        inverted_index = pickle.load(myFile)
    label, confidence = inverted_indexing.get_doc_label(inverted_index, doc_data.strip())
    return str(label+", "+str(confidence))


if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True)