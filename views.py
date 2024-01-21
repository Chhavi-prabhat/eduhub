from django.http import HttpResponse
from django.shortcuts import render
# import pyrebase

config={
    'apiKey': "AIzaSyCbo4uTnMyWIZ-WArNq54cEg4so11MIA18",
    'authDomain': "eduhub-de75e.firebaseapp.com",
    'projectId': "eduhub-de75e",
    'storageBucket': "eduhub-de75e.appspot.com",
    'messagingSenderId': "764009909652",
    'appId': "1:764009909652:web:f0fc29c24b091b7abe5381",
    'measurementId': "G-74TSPVZ42E"
}

# firebase=pyrebase.initialize_app(config)
# auth=firebase.auth()

def HomePage(request):
    return render(request,"HomePage.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def profile(request):
    return render(request,"profile.html")

def class_display(request):
    return render(request,"class_display.html")

def class_first_row(request):
    return render(request,"class8to10_subject.html")

def class_second_row(request):
    return render (request, "class11to12.html")

def class_third_row(request):
    return render (request, "jee_neet.html")

def portal_first_row(request):
    return render(request,"portals_first_row.html")
    
def members(request):
    return render(request,"members.html")
