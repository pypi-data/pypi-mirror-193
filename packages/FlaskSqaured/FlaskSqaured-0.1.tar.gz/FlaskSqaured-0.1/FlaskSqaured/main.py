import flask
from flask import request, jsonify, render_template, redirect, url_for, session, flash, send_from_directory, send_file, abort, make_response, Response, stream_with_context

class ezFlask:
    
    def __init__(self, name):
        self.app = flask.Flask(name)
        self.app.config["DEBUG"] = True
    
    def createPage(self, htmlFile, path):
        try:
            @self.app.route(path)
            def page():
                return render_template(htmlFile)
        except Exception as e:
            print(e)
        
    def createPageWithData(self, htmlFile, path, data):
        try:
            @self.app.route(path)
            def page():
                return render_template(htmlFile, data = data)
        except Exception as e:
            print(e)
    
    def createPageWithPost(self, htmlFile, path):
        try:
            @self.app.route(path, methods = ['POST'])
            def page():
                return render_template(htmlFile)
        except Exception as e:
            print(e)
    def createPageWithPostWithData(self, htmlFile, path, data):
        try:
            @self.app.route(path, methods = ['POST'])
            def page():
                return render_template(htmlFile, data = data)
        except Exception as e:
            print(e)
    def createPageWithGet(self, htmlFile, path):
        try:
            @self.app.route(path, methods = ['GET'])
            def page():
                return render_template(htmlFile)
        except Exception as e:
            print(e)
    def createPageWithGetWithData(self, htmlFile, path, data):
        try:
            @self.app.route(path, methods = ['GET'])
            def page():
                return render_template(htmlFile, data = data)
        except Exception as e:
            print(e)
    def createPageWithGetAndPost(self, htmlFile, path):
        try:
            @self.app.route(path, methods = ['GET', 'POST'])
            def page():
                return render_template(htmlFile)
        except Exception as e:
            print(e)
    def createPageWithGetAndPostWithData(self, htmlFile, path, data):
        try:
            @self.app.route(path, methods = ['GET', 'POST'])
            def page():
                return render_template(htmlFile, data = data)
        except Exception as e:
            print(e)
    def serve(self, host, port):
        try:
            self.app.run(host = host, port = port)
        except Exception as e:
            print(e)
    def serveWithDebug(self, host, port):
        try:
            self.app.run(host = host, port = port, debug = True)
        except Exception as e:
            print(e)
    def createAPI(self, path, data):
        try:
            @self.app.route(path, methods = ['GET'])
            def api():
                return jsonify(data)
        except Exception as e:
            print(e)
    def changePage(self, path):
        try:
            return redirect(path)
        except Exception as e:
            print(e)
    def createSession(self, name, data):
        try:
            session[name] = data
        except Exception as e:
            print(e)
    def getSession(self, name):
        try:
            return session[name]
        except Exception as e:
            print(e)
    def deleteSession(self, name):
        try:
            session.pop(name)
        except Exception as e:
            print(e)
    def createFlash(self, message):
        try:
            flash(message)
        except Exception as e:
            print(e)
        