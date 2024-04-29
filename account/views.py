import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from account.schema_account import login_schema


@csrf_exempt
def graphql_view(request):
    if request.method == "POST":
        body = request.body.decode("utf-8")
        operation = json.loads(body)
        query = operation.get("query")
        variables = operation.get("variables")
    return JsonResponse({"error": "Unsupported method."}, status=400)
