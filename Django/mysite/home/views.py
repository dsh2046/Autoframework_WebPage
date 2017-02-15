from django.shortcuts import render
from django.http import *
from django.db import connection
from django.db import models
import psycopg2
import json

def dbConn(username):
    conn = psycopg2.connect(database=username, user="postgres", password="12345678", host="10.10.31.6", port="5432")
    cur = conn.cursor()
    return cur

def index(request):
    if request.method == 'GET' and 'remember' in request.GET:
        request.session['remember'] = request.GET['remember']
    username = request.session.get('username', 'anybody')
    if username=='anybody':
        return HttpResponse("<h2>Please login again!!</h2>")
    else:
        cur = dbConn(username)
        cur.execute('select * from functional_test_run')
        result = cur.fetchall()
        return render(request, 'home/pages/tables.html', {'result': result, 'username': username})

def detail(request):
    username = request.GET['username']
    cur = dbConn(username)
    job_id = request.GET['id']
    cur.execute('select functional_results.id, functional_testcase.test_name, functional_results.start_time, functional_results.end_time, functional_results.test_result, functional_results.log_file from functional_results, functional_testcase where functional_results.test_id=functional_testcase.id and functional_results.job_id='+job_id)
    result = cur.fetchall()
    return HttpResponse(json.dumps(result))

def login(request):
    if request.session.get('remember') == '1':
        return HttpResponseRedirect('/index/')
    else:
        return render(request, 'home/pages/login.html')
    # del request.session['remember']
    # return HttpResponse(request.session.get('remember'))


def login_validate(request):
    username = request.GET['username']
    password = request.GET['password']
    request.session['username'] = username
    request.session['test'] = 'testname'
    conn = psycopg2.connect(database="User_Info", user="postgres", password="12345678", host="10.10.31.6", port="5432")
    cur = conn.cursor()
    cur.execute("select * from account where Username="+"'"+username+"'"+" and Password="+"'"+password+"'")
    if cur.fetchall():
        return HttpResponse('1')
    else:
        return HttpResponse("Doesn't exist")

def logout(request):
    del request.session['username']
    if 'remember' in request.session:
        del request.session['remember']
    return HttpResponseRedirect('/login/')