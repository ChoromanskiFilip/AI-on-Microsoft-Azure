import logging
import azure.functions as func
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import pyrebase
import json
import uuid


FIREBASE_CONFIG = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "storageBucket": "",
    "serviceAccount": "firebase_service_account_key.json"
}

# Azure Text Analytics API 
key = ""
endpoint = ""

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

textanalytics_client = authenticate_client()

firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
db = firebase.database()

def get_product_categories():
    categories = []
    for prod in db.child("products").child("categories").get().each():
        categories.append(prod.val()["name"])
    return categories

def get_products(category):
    products_names = []
    for prod in db.child("products").child("categories").get().each():
        if prod.val()["name"] == category:
            products = prod.val()["models"]
            for model in products:
                products_names.append(model.get("name"))
            break
    return products_names

def get_model_variant(category, model_name, variant_type):
    for prod in db.child("products").child("categories").get().each():
        if prod.val()["name"] == category:
            products = prod.val()["models"]
            for model in products:
                if model.get("name") == model_name:
                    return model.get(variant_type)
            break
    return []

def create_order(body):
    price = 0
    for prod in db.child("products").child("categories").get().each():
        if prod.val()["name"] == body['product']['category']:
            products = prod.val()["models"]
            for model in products:
                if model.get("name") == body['product']['name']:
                    price = model.get('price')
                    break
    order_id = str(uuid.uuid4())
    body['product']['price'] = price
    body['order_id'] = order_id
    body['state'] = "Collecting"
    db.child("orders").push(body)
    return body

def get_order_by_id(ord_id):
    for order in db.child("orders").get().each():
        if order.val()["order_id"] == ord_id:
            return order.val()


def sentiment_analysis(text):
    response = textanalytics_client.analyze_sentiment(documents=[text])[0]
    sentiment = response.sentiment
    new_sent = dict(db.child("bot_sentiment").get().val())
    new_sent[sentiment] += 1
    new_sent["votes"] += 1
    new_sent["score"] = 100 * new_sent["positive"] / (new_sent["votes"] - new_sent["neutral"])
    db.child("bot_sentiment").update(new_sent)
    return sentiment

def get_sentiment():
    current_sentiment = db.child("bot_sentiment").get().val()["score"]
    return {"answer": round(current_sentiment, 1)}


def main(req: func.HttpRequest) -> func.HttpResponse:
    action = req.params.get('action')
    if action:
        if action == "GetCategories":
            return func.HttpResponse(
                json.dumps(get_product_categories()),
                mimetype="application/json", 
                status_code=200
            )
        elif action == "GetProducts":
            return func.HttpResponse(
                json.dumps(get_products(req.params.get('category'))),
                mimetype="application/json", 
                status_code=200
            )
        elif action == "GetVariants":
            return func.HttpResponse(
                json.dumps(get_model_variant(req.params.get('category'), req.params.get('model'), req.params.get('variant'))),
                mimetype="application/json",
                status_code=200
            )
        elif action == "NewOrder":
            return func.HttpResponse(
                json.dumps(create_order(req.get_json())),
                mimetype="application/json",
                status_code=200
            )
        elif action == "FindOrder":
            return func.HttpResponse(
                json.dumps(get_order_by_id(req.params.get("order_id"))),
                mimetype="application/json",
                status_code=200
            )
        elif action == "GetBotRating":
            return func.HttpResponse(
                json.dumps(get_sentiment()),
                mimetype="application/json",
                status_code=200
            )
        elif action == "NewBotRating":
            return func.HttpResponse(
                json.dumps(sentiment_analysis(req.get_json().get("answer"))),
                mimetype="application/json",
                status_code=200
            )
        elif action == "Hello":
            name = req.params.get('name')
            if name:
                return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
            else:
                return func.HttpResponse("No name given :(")
        else:
            return func.HttpResponse("Default action!")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )