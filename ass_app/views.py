from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
import os
from django.conf import settings



def Index(request):
    if request.method == 'POST':    
        csv_file = request.FILES.get('csv_file')
        
        if csv_file:
            try:
                df = pd.read_csv(csv_file)
                numeric_columns  = df.select_dtypes(include=['number']).columns.tolist()
                categorical_columns  = df.select_dtypes(include=['object']).columns.tolist()
                # coloumns = {numeric_columns, categorical_columns}
                # print('--------------')
                # print(df.describe())
                # print('--------------')
                # print('Null Values Present in Data : ')
                # print(df.isnull().sum())
                null_values =  df.isnull().sum().to_dict()
                statistics = {}
                for i in numeric_columns: 

                # ==============mean=================   
                    n = len(df[i])
                    Sum = df[i].sum()
                    mean = Sum/n
                
                # ===============median================
                 
                    sorted_col = df[i].dropna().sort_values().reset_index(drop=True)
                    n = len(sorted_col)
                    if (n%2==1):
                        # for odd number
                        median = sorted_col[n // 2]                       
                       
                    else:
                        # for even number
                        median = (sorted_col[n // 2 - 1] + sorted_col[n // 2]) / 2
                # ===================Standard Deviation=====================
                    data = df[i].dropna().tolist()
                    variance = sum((x - mean) ** 2 for x in data) / (n - 1) if n > 1 else float('nan')
                    std_deviation = math.sqrt(variance)
                    # print('std === ',std_deviation)


                #===================Missing Values====================

                    statistics[i] = {
                        'mean': mean,
                        'median': median,
                        'std_deviation': std_deviation
                    }
                
                    # df[i].fillna(df[i].mean(),inplace=True)
                    df[i].fillna(int(df[i].mean()), inplace=True)
                
                
                for i in categorical_columns:
                    mode_value = df[i].mode()[0]

                    df[i].fillna(mode_value,inplace=True)
                    
                # print('Null Values Present in Data : ')
                # print('===============================')
                # print(df.isnull().sum())
                

                #Data Visualization

                plt.figure()
                df.hist()
                hist_plot = os.path.join(settings.MEDIA_ROOT, 'histogram.png')
                plt.savefig(hist_plot)

                # Visualization
                plt.figure()
                sns.pairplot(df)
                pairplot_path = os.path.join(settings.MEDIA_ROOT, 'pairplot.png')
                plt.savefig(pairplot_path)
                first_rows = df.head(5).to_html(classes='table table-bordered')
                null_values_after = df.isnull().sum().to_dict()
                context = {
                    # 'coloumns': coloumns,
                    
                    'statistics': statistics,
                    'hist_plot': settings.MEDIA_URL + 'histogram.png',
                    'pairplot': settings.MEDIA_URL + 'pairplot.png',
                    'first_rows': first_rows,
                    'numeric_columns': numeric_columns,
                    'categorical_columns': categorical_columns,
                    'null_values':null_values,
                    'null_values_after':null_values_after
                }
                # return redirect('/Result')
                return render(request, 'result.html', context)
            except pd.errors.ParserError as e:
                return HttpResponse(f"Error parsing CSV file: {str(e)}")
            except Exception as e:
                return HttpResponse(f"An error occurred: {str(e)}")
        else:
            return HttpResponse('No File Uploaded')

    else:
        return render(request, 'index.html')
    




def Result(request):
    return render(request, 'Result.html')