from flask import Flask,render_template, request, flash, redirect, url_for, send_file

import sys
from FuncMile36 import return_csv

app = Flask(__name__)

@app.route('/test')
def hello_world():
    return 'Hello, World!'

@app.route("/",  methods=('GET', 'POST'))
def viewentries():
     #url =''
    if request.method == 'POST':
        url = request.form['inp_url']

        if not url:
            flash('URL is required!')
        else:
            print('url entered is ', url)
            file_nm = return_csv(url)
            print('called function return_csv - check for created csv file', file_nm)
            redirect_url=file_nm+"/getCSV"
            return redirect(redirect_url)

    return render_template('index.html')  #variable=usernames_list

@app.route("/<int:ofile>/getCSV")
def getPlotCSV(ofile):
    outfile = str(ofile) +".csv"
    with open(outfile) as fp:  #outputs/Adjacency.csv
        csv = fp.read()
    return render_template('excel.html', inp_url = " ", csv = outfile)


@app.route("/<int:ofile>/downloadCSV")
def downloadCSV(ofile):
    outfile = str(ofile) + ".csv"
    # with open("outputs/Adjacency.csv") as fp:
    #     csv = fp.read()
    # return render_template('excel.html', inp_url = "this is test", csv = "Mile3/363500.csv")
    return send_file(outfile,
                     mimetype='text/csv',
                     attachment_filename=outfile,
                     as_attachment=True)


#{{ request.form['inp_url'] }}
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# @app.route('/')
# def student():
#     return render_template('yourfile.html')
#
# @app.route('/urlinput',methods = ['POST', 'GET'])
# def url_results():
#     if request.method == 'POST':
#         result = request.form['Curtain_OPENTIME']
#         print(result)
#         return "thank you for filling out this form"
    # if request.method =='GET':
    #     inputurl = 'get url from website to run it in the function'
        #run thr url in program
        #output = output.csv
# if 'Mile6' == '__main__':
#     app.run(debug = True)

# <div class="container-fluid">
#     <label class="form-label" for="inp_url">URL Input:</label><br>
#     <textarea class="form-control" type="text" id="inp_url" name="inp_url">{{inp_url}}</textarea><br>
# </div>


# <form class="form-horizontal inputForm" method = "post">
#
#     <div class="form-group">
#         <label class="control-label col-sm-2" for="inp_url">URL Input:</label>
#         <div class="col-sm-2">
#             <input class="form-control" type="text" id="inp_url" name="inp_url"
#                    placeholder="Enter the url"
#                    value=""/><br>
#             <button class = "btn btn-primary" type="submit"> Submit </button>
#         </div>

# <script>
#         loc = {{csv}}+"/downloadCSV"
#     </script>
