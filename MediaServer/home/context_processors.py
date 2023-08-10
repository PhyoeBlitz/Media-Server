def theme(request):
    if request.session.get('theme') == 'dark':
        return {'theme': 'dark'}
    else:
        return {'theme': 'light'}
