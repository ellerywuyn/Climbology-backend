from django.http import HttpResponse, JsonResponse
from django.db.models import F, FloatField, ExpressionWrapper
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
import openai
from openai import OpenAI
import os
import neo4j
import pandas as pd
import json
from neo4j import GraphDatabase


def connect_db():
    uri = "neo4j://0.0.0.0:7687"
    user = "neo4j"
    password = "password"
    driver = GraphDatabase.driver(uri, auth=(user, password))
    return driver

def run_commands(driver, commands):
    with driver.session(database="neo4j") as session:
        for command in commands:
            session.run(command)


@csrf_exempt
@api_view(['POST'])
def update_hold(request):
    data = json.loads(request.body)
    hold_id = data.get('holdId')
    property_to_update = data.get('property')
    new_value = data.get('value')
    driver = connect_db()

    with driver.session() as session:
        result = session.run(
            f"MATCH (h:Hold {{hold_id: {hold_id}}}) "
            f"SET h.{property_to_update} = '{new_value}' "
            f"RETURN h;"
        )
    print(result)
    return JsonResponse({'status': 'success'})

# @csrf_exempt
# @api_view(['POST'])
# def delete_hold(request):
#     data = json.loads(request.body)
#     hold_id = data.get('holdId')
#     driver = connect_db()
#     print(hold_id)
#     commands = (
#             "MATCH (h:Hold) WHERE h.hold_id = $hold_id DETACH DELETE h",
#         {"hold_id": hold_id}
#     )
#     run_commands(driver, commands)
#     return JsonResponse({'status': 'success'})

@csrf_exempt
@api_view(['POST'])
def delete_hold(request):
    data = json.loads(request.body)
    hold_id = data.get('holdId')
    driver = connect_db()
    with driver.session() as session:
        try:
            result = session.run(
                "MATCH (h:Hold {hold_id: $hold_id}) DETACH DELETE h",
                {"hold_id": hold_id}
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            print(f"An error occurred: {e}")
            return JsonResponse({'status': 'failed'})

    # Assuming run_commands takes a list of commands and their corresponding parameters
    # run_commands(driver, [(command, parameters)])

    # return JsonResponse({'status': 'success'})


@csrf_exempt
@api_view(['POST'])
def delete_move(request): 
    data = json.loads(request.body)
    route_id = data.get('routeId')
    driver = connect_db()

    with driver.session() as session:
        result = session.run(
            "MATCH (r:Route)-[rel:HAS_MOVE]->(m:Move) WHERE r.route_id = $route_id "
            "DETACH DELETE m",
            {"route_id": route_id}
         )
    print(result)
    return JsonResponse({'status': 'success'})

@csrf_exempt
@api_view(['POST'])
def find_holds_by_property(request):
    data = json.loads(request.body)
    property_to_find = data.get('property')
    value = data.get('value')
    driver = connect_db()

    with driver.session() as session:
        result = session.run(
            f"MATCH (h:Hold) "
            f"WHERE h.{property_to_find} = '{value}' "
            f"RETURN h"
        )
        holds = [record['h'].properties for record in result]
    print(result)
    return JsonResponse({'result': holds})

@csrf_exempt
@api_view(['POST'])
def find_routes_by_property(request):
    data = json.loads(request.body)
    property_to_find = data.get('property')
    value = data.get('value')
    driver = connect_db()

    with driver.session() as session:
        result = session.run(
            f"MATCH (start)-[r:{property_to_find}]->(end) "
            f"WHERE r.{property_to_find} = '{value}' "
            f"RETURN r"
        )
    print(result)
    return JsonResponse({'status': 'success'})