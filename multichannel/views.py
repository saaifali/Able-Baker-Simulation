# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .core.simulation import customerListGenerator
from .core.test import test
# Create your views here.


def getList(s):
    if s == 'n2':
        return [1, 2, 4, 8]
    elif s == 'n3':
        return [1, 3, 9, 27]
    elif s == 'kh1':
        return [1, 2, 3, 4]
    elif s == 'kh2':
        return [2, 4, 6, 8]
    elif s == 'kh3':
        return [7, 8, 9, 10]
    elif s == 'kh4':
        return [5, 7, 11, 13]

    return [1, 2, 3, 4]


class SimulateView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        data = {}
        return render(request, self.template_name, data)


    def post(self, request):
        name = request.POST.get("name")
        customers = int(request.POST.get("value"))
        customerInterArrivalTime = getList(request.POST['customerInterArrivalTime'])
        ableServiceTime = getList(request.POST['ableServiceTime'])
        bakerServiceTime = getList(request.POST['bakerServiceTime'])

        if request.POST['ableBakerPriority'] == 'able':
            ableBakerPriority = 0
        elif request.POST['ableBakerPriority'] == 'baker':
            ableBakerPriority = 1
        elif request.POST['ableBakerPriority'] == 'rand':
            ableBakerPriority = 2

        count = customers
        lili = customerListGenerator(customerInterArrivalTime, ableServiceTime, bakerServiceTime, ableBakerPriority, count)

        # printing output using django -> Mahdi

        array2dOFRow = test(lili)

        return render(request, 'simulation.html', {
            'name':name,
            'allData': array2dOFRow}
                      )
