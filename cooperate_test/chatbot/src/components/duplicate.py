def ask_openai_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message')
            response = ask_openai(message, 'gpt-3.5-turbo')
            return JsonResponse({'success': True, 'response': response})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data in the request body.'})