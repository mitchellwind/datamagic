# coding: utf-8
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Mydata
import pandas as pd


def index(request):

    return render(request, "databoard/index.html")

def highcharts(request):

    return render(request, "databoard/highcharts.html")

def d3(request):

    return render(request, "databoard/d3.html")


def plotly(request):

    return render(request, "databoard/plotly.html")

@csrf_exempt
def list_query(request):

    user_input=request.POST["Myinput"]

    s=pd.read_excel('z:\国内经济数据\指标列表1.xlsm',sheetname='结果',parse_cols=[0])

    sl=list(s['指标名称'])

    sg_list=search_suggest(user_input,sl)

    return JsonResponse(sg_list, safe=False)


@csrf_exempt
def data_query(request):

        item_name=request.POST.getlist('SelectedItem[]')
        myfreq=request.POST["freq"]
        mymethod=request.POST["sample_method"]
        startTime=request.POST["start_time"]
        endTime=request.POST["end_time"]
        if startTime=="":
            startTime=None
        if endTime=="":
            endTime=None
        df= datamagnet(item_name,myfreq,mymethod,startTime,endTime)
        df.to_clipboard(excel=True)
        df_out=pd.DataFrame(df.T).to_json(orient='split')
        print(item_name)
        return JsonResponse(df_out, safe=False)

def search_suggest(user_input, search_list, split_char=" "):

    match_list = []
    for search_string in search_list:
        match_flag = 1
        for char in user_input.split(split_char):
            if char not in search_string:
                match_flag = 0
        if match_flag == 1:
            match_list.append(search_string)

    return match_list

def digger(item_name, item_info, freq=None, method='last'):

    # get data from excel files

    import pandas as pd

    [wbname, shtname, time_column, time_s_row, item_column]=item_info
    df_item = pd.read_excel(wbname, sheetname=shtname, parse_cols=[time_column-1, item_column-1],
                            header=None, skiprows=time_s_row-1, index_col=0)
    df_item.columns = [item_name]

    if freq is None:
        return df_item
    else:
        return df_item.resample(freq).agg(method)


def sniffer(item_name):

    # get item information from item list

    import pandas as pd

    df_list = pd.read_excel('z:\国内经济数据\指标列表1.xlsm',sheetname='结果', index_col=0)

    item_info = df_list.loc[item_name].values

    return item_info


def datamagnet(item_name, freq=None, method='last',start=None, end=None):

    # combine sniffer and digger

    import pandas as pd

    if type(item_name)==list:
        df = []
        for item in item_name:
            item_info = sniffer(item)
            df.append(digger(item, item_info, freq, method))
        df_combine= pd.concat(df, axis=1)
    else:
        item_info = sniffer(item_name)
        df_combine= digger(item_name, item_info, freq, method)
    return df_combine[start:end]
