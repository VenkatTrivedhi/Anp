from django.shortcuts import render
from Web.models import Input


import os
import sys
import glob



def Txt_handler(request):

    if request.method=='POST':
        got = request.POST
        input_txt = got['editor']


        return render(request,'web.html',{"input": input_txt })


    else:
        return render(request,'web.html',)
