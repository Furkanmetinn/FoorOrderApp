from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from account.schema_account import login_schema

@csrf_exempt
def graphql_view(request):
    if request.method == 'POST':
        result = login_schema.execute(request.body.decode('utf-8'))
        return JsonResponse(result.to_dict(), status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=400)
