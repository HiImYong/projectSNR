from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, "main.html")


# def rate_image(request):
#     if request.methos == 'POST':
#         el_id = request.POST.get('el_id')
#         val = request.POST.get('val')
#         obj = Rating.objects.get(id=el_id)
#         obj.score = val
#         obj.save()
#         return JsonResponse({'success':'true', 'score':val}, safe=False)
#     return JsonResponse({'success':'false'})