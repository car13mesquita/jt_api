from flask import Blueprint, request
import pandas as pd

companies = Blueprint('companies', __name__, url_prefix="/companies")

companies_filepath = "./dataset/file1.csv"

@companies.route("/", methods=["POST", "GET"])
def post():
    df = pd.read_csv(companies_filepath)
    if request.method == "POST":
        data = df.append({'_id': "new_ID", 'industries': "new_industry"}, ignore_index=True)
        data.to_csv(companies_filepath, encoding='utf-8')
        return 'complete', 200
    else:
        data = df.to_dict()
        return data, 200


@companies.route("/<id>", methods=["PUT", "DELETE", "GET"])
def put_delete(id):
    df = pd.read_csv(companies_filepath)
    if request.method == "PUT":
        # add stuff here
        return 200
    elif request.method == "DELETE":
        data = df.drop(index=df.index[df['_id'] == id], axis=0)
        data.to_csv(companies_filepath, encoding='utf-8')
        return 'complete', 200
    else:
        data = df.loc[df['_id'] == id].to_dict()
        return data, 200
