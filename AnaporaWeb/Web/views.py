from django.shortcuts import render
from Web.form import fileform
from Web.models import Input
import os
import sys
import glob
def Txt_handler(request):
    form = fileform()
    if request.method=='POST':
        got = request.POST
        txt= got['Upload_file']

        # you have do/copy nlp processing code here taking -> inst as your input txt file
        ########################
        #############
        ########
        # then assign your result in bellow respective varible


        # i am giving demo/facke result here
        annoted_words =['he','this','its','them']
        precision = 1.0
        recall = 1.0
        accurancy = 1.345

        return render(request,'web.html',{ "form":form,"precision" :precision,"recall":recall,"accurancy":accurancy,"txt":txt,"ant":annoted_words})

    else:

        return render(request,'web.html',{"form":form})
