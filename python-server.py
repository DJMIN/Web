# -*- coding: utf-8 -*-
# !/usr/bin/python

from flask import Flask, request, render_template,send_from_directory,url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

r_path = 'C:\\Users\\Chen\\PycharmProjects\\Web'


def getfile():
    path1=r_path+'/uploadfile'
    path2=r_path
    #跳转目录 跳转到下载文件的目录，获得下载文件目录里面的ｌｉｓｔ之后，然后再跳转出来
    os.chdir(path1)
    flist=os.listdir()
    os.chdir(path2)
    return flist

def isHavefile(filename):
    # print (os.getcwd())
    path1=r_path+'/uploadfile'
    path2=r_path
    os.chdir(path1)
    flag=os.path.isfile(filename)
    os.chdir(path2)
    # print (os.getcwd())
    return flag

@app.route('/uploadfile', methods=['POST','get'])
def upload():
    if request.method=='GET':
        return '<h3>get 222 </h3>'
    if request.method=='POST':
        """
        path=os.getcwd()+'/uploadfile'
        upfilename=request.form['upfilename']
        f=request.files['file']
        fname=secure_filename(f.filename)
        f.save(os.path.join(path,fname))
        print(upfilename)
        print(fname)
        """
        relativepath='./uploadfile/'
        upfilename=request.form['upfilename']
        f=request.files['file']
        fname=secure_filename(f.filename)
        f.save(os.path.join(relativepath,fname))
        print(upfilename)
        print(fname)
        return render_template('uploadfile_ok.html')


#显示上传页面 同时也是主页面
@app.route('/up', methods=['POST','get'])
def up():
    mycss=url_for('static', filename='style.css')
    return render_template('upload.html',mycss=mycss)


@app.route('/file', methods=['POST','get'])
def file():
    mycss=url_for('static', filename='style.css')
    return render_template('upload.html',mycss=mycss)

#main页面
@app.route('/')
def hello():
    mycss=url_for('static', filename='style.css')
    return render_template('index.html',mycss=mycss)

#显示下载文件的界面
@app.route('/down', methods=['GET'])
def downloadpage():
    mycss=url_for('static', filename='style.css')
    flist=getfile()
    return render_template('downloadpage.html',mycss=mycss,fl=flist)


#下载要下载的文件，要下载的文件是通过get方法来传递的
@app.route('/downloadfile', methods=['GET'])
def downloadfile():
    if request.method=='GET':
        downloadfilename=request.args.get('filename')
        # flist=getfile()
        # print ()
        if downloadfilename and isHavefile(downloadfilename):
            return send_from_directory('uploadfile',downloadfilename,as_attachment=True)
        else:
            return '文件未找到', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5002)
