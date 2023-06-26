from django.shortcuts import render
from celery import shared_task
import requests
import json
import csv
import io


@shared_task
def wa_queue(name, csv_data):
    csv_lines = csv_data.splitlines()
    reader = csv.reader(csv_lines)
    rows = [row for row in reader]
    camp_name = name
    for row in rows:
        # Perform operations on each row of the CSV data
        # Example: Access row data using row[index]
        url = "https://graph.facebook.com/v17.0/105070319074153/messages"

        payload = json.dumps({
        "messaging_product": "whatsapp",
        "to": row,
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": {
            "code": "en_US"
            }
        }
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer EAASTdXG5vwABADB2aLZAgjcxbfouGImnm9h9UfgP0ZAOUa1HbLOdv7mw9AdTvkD3F4ZCaILoS0lQLw0STquReYEJwcUFcMYZAzEerwSkklA3eRw9CXyktdHpZBrEpIsf4S1eyMIzBhK4nM8tl9lxA1f6LRTMqowlZApwV8CushZCcAGvFz0ZBZC3JwYO0rxWruN7dTZAiWMZBNhQgZDZD'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        file.write(response.content)
        
    print(name)