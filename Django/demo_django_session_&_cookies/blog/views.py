from django.shortcuts import render
from django.http import HttpResponse

# for session
def set_session(request):
    request.session["username"] = 'mohit'
    request.session["course"] = 'Djnago full course'
    return HttpResponse("session data saved successfully")

def get_session(request):
    username = request.session.get("username", "Guest")
    course = request.session.get("course", "not entrolled")
    return HttpResponse(f"Welcome username:{username}, Course: {course}")

def delete_session(request):
    '''
    del request.session["username"]
    del request.session["course"]
    '''
    request.session.flush()
    return HttpResponse("All session data deleted successfully.")

# for cookie
def set_cookie(request):
    response = HttpResponse("Cookie set successfully")
    response.set_cookie("username", "mohit kumar", max_age=60*60*24) # cokkies saved for 1 day
    response.set_cookie('course', "Django Full Course", max_age=60*60*24)
    return response

def get_cookie(request):
    username = request.COKKIES.get('username', 'Guest')
    course = request.COKKIES.get('course', "No Course selected")
    if "username" in request.COKKIES:
        return HttpResponse(f"Username: {username}, Course: {course}")
    else:
        return HttpResponse("No Cookies found")

def delete_cookie(request):
    response = HttpResponse("Cookie Deleted successfully")
    response.delete_cookie("username")
    response.delete_cookie("course")
    return response


