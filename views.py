from models import Game, Player, Message
from django.http import HttpResponse
import json

def api(request):
    q = json.loads(request.POST['json'])
    action = q['action']
    response = {'success': False}
    if action == 'create':
        g = Game(name=q['name'], max_players=q['max_players'])
        g.save()
        response['id'] = g.pk
        response['success'] = True
    if action == 'list':
        pass
    if action == 'join':
        pass
    if action == 'ready':
        pass
    if action == 'leave':
        pass
    if action == 'send':
        pass
    if action == 'poll':
        pass
    return HttpResponse(json.dumps(response))