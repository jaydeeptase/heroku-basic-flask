from flask import Flask, send_from_directory
from datetime import datetime
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

@app.route('/canvas.html')
def canvaspage():
    return """
    <img src="/static/images/Portfolio.png" width="110%"/>
    """

@app.route('/pgimfact.html')
def pgimfactpage():
    return """
    <img src="/static/images/pgimfact.png" width="100%"/>
    """
# @app.route('/docs/<id>')
# def get_pdf(id=None):
#     if id is not None:
#         binary_pdf = get_binary_pdf_data_from_database(id=id)
#         response = make_response(binary_pdf)
#         response.headers['Content-Type'] = 'application/pdf'
#         response.headers['Content-Disposition'] = \
#             'inline; filename=%s.pdf' % 'yourfilename'
#         return response
    
@app.route('/s/file/<id>')
def show_static_pdf(id=None):
    # with open('files/1.pdf', 'rb') as static_file:
    #     return send_file(static_file, attachment_filename='1.pdf')
    return send_from_directory('files', id+'.pdf')

    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port=5000, host="localhost")

