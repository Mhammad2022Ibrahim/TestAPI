import json
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from appTest.models import People, Resource


# Create your views here.
@csrf_exempt
def users(request):
    if request.method == "GET":
        message = json.loads(request.body)
        email = message["email"]
        first_name = message["first_name"]
        last_name = message["last_name"]
        avatar = message["avatar"]
        url = message["url"]
        text = message["text"]

        user = People(email=email, first_name=first_name, last_name=last_name, avatar=avatar, url=url, text=text)
        user.save()
        my_message = {"data": user.datas(), "support": user.supports()}

    if request.method == "POST":
        message = json.loads(request.body)
        name = message["name"]
        job = message["job"]
        create_user = People(first_name=name, job=job)
        create_user.save()
        my_message = create_user.create()

    return JsonResponse(my_message)


def listUsers(request):
    data = list(People.objects.all().values("id", "email", "first_name", "last_name", "avatar"))
    support = list(People.objects.all().values("url", "text"))
    my_message = {"data": data, "support": support}
    return JsonResponse(my_message)


@csrf_exempt
def userID(request, ID):
    if request.method == "PUT":
        message = json.loads(request.body)
        name = message["name"]
        job = message["job"]
        update_user = People(first_name=name, job=job)
        update_user.save()
        my_message = update_user.update()
    elif request.method == "PATCH":
        message = json.loads(request.body)
        name = message["name"]
        job = message["job"]
        patch_user = People(first_name=name, job=job)
        patch_user.save()
        my_message = patch_user.patch()
    elif request.method == "DELETE":
        People.objects.all().delete()
        my_message = {}

    elif People.objects.filter(id=ID).exists():
        getId = People.objects.get(id=ID)
        my_message = {"data": getId.datas(), "support": getId.supports()}
    else:
        my_message = {}
    return JsonResponse(my_message)


@csrf_exempt
def resource(request):
    if request.method == "GET":
        resources = json.loads(request.body)
        name = resources["name"]
        year = resources["year"]
        color = resources["color"]
        pantone_value = resources["pantone_value"]
        url = resources["url"]
        text = resources["text"]
        id_user = resources["id_user"]


        user_res = Resource(name=name, year=year, color=color, pantone_value=pantone_value, url=url, text=text
                            , id_user=id_user)
        user_res.save()
        my_resource = {"data": user_res.res(), "support": user_res.supports()}

    return JsonResponse(my_resource)


def listunknown(request):
    data = list(Resource.objects.all().values("id", "name", "year", "color", "pantone_value"))
    support = Resource.objects.values("url", "text")
    my_resource = [{"data": [data], "support": support}]
    return JsonResponse(my_resource)


def unknownID(request, ID):
    if Resource.objects.filter(id=ID).exists():
        getId = Resource.objects.get(id=ID)
        message = {"data": getId.res(), "support": getId.supports()}
    else:
        message = {}
    return JsonResponse(message)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data["username"]
        password = data["password"]

        if not password:
            my_token = {'error': 'Missing password'}

        else:
            user = User.objects.create_user(username=username, password=password)
            token, created = Token.objects.get_or_create(user=user)
            user.save()
            my_token = {'id': user.pk, 'token': token.key}

    return JsonResponse(my_token)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            token = Token.objects.get(user=user)
            my_token = {'token': token.key}
        else:
            my_token = {'error': 'Missing password'}

    return JsonResponse(my_token)


@csrf_exempt
def sendResource(request):
    if request.method == "POST":
        data = json.loads(request.body)
        id_user = data["id_user"]
        if Resource.objects.filter(id_user=id_user).exists():
            message = Resource.objects.get(id_user=id_user)
            mydata = {"data": message.res()}
        else:
            mydata = {}
        return JsonResponse(mydata)


@csrf_exempt
def sendPeople(request):
    if request.method == "POST":
        data = json.loads(request.body)
        id_user = data["id_user"]
        if People.objects.filter(id=id_user).exists():
            message = People.objects.get(id=id_user)
            mydata = {"data": message.datas()}
        else:
            mydata = {}
        return JsonResponse(mydata)
