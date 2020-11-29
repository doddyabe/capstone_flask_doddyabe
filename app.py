from flask import Flask, request 
import pandas as pd 
app = Flask(__name__) 

# teset
#home root 
@app.route('/')
def homepage():
    return "hello world"

# mendapatkan buku 
@app.route('/ambil_buku')
def ambilbuku():
    data = pd.read_csv('data/books_c.csv')
    return data.to_json() # atau integer, atau string


# endpoint dinamis 1 untuk Pengarang (Contoh)
@app.route('/get_author/<name>')
def getauthor(name):
    author = name
    books = pd.read_csv('data/books_c.csv')
    condition = books['authors'] == author
    books = books[condition]
    return books.to_json()

# endpoint dinamis 1 untuk Judul Buku
@app.route('/get_title/<title>')
def gettitle(title):
    title = title
    books = pd.read_csv('data/books_c.csv')
    condition = books['title'] == title
    books = books[condition]
    return books.to_json()


# endpoint buku yang menghitung statistik buku
@app.route('/describe_book')
def describebook():
    books = pd.read_csv('data/books_c.csv')
    results = books.describe()
    return results.to_json()


# endpoint buku yang memiliki rating di atas 3
@app.route('/upperthree_rating_book')
def upperthreeratingbook():
    books = pd.read_csv('data/books_c.csv')
    condition = books['average_rating'] >= 3
    books = books[condition]
    return books.to_json()

# endpoint buku yang memiliki rating di bawah 3
@app.route('/underthree_rating_book')
def underthreeratingbook():
    books = pd.read_csv('data/books_c.csv')
    condition = books['average_rating'] <= 3
    books = books[condition]
    return books.to_json()

# endpoint yang menghasilkan buku dirating di atas 1000.000 rating
@app.route('/milion_rating_book')
def milionfreqratingbook():
    books = pd.read_csv('data/books_c.csv')
    condition  = books['ratings_count'] >= 1000000
    books = books[condition]
    return books.to_json()

# endpoint yang menunjukkan buku berbahasa Inggris
@app.route('/english_book')
def englishbook():
    books = pd.read_csv('data/books_c.csv')
    condition  = books['language_code'] == 'eng'
    books = books[condition]
    return books.to_json()

# endpoint yang menampilkan daftar buku dengan metode stack - unstack
@app.route('/list_book')
def listbook():
    books = pd.read_csv('data/books_c.csv')
    results = books.stack().unstack()
    return results.to_json()

# endpoint yang menunjukkan crosstab buku berdasarkan bahasa dengan metode group by
@app.route('/language_book')
def languagebook():
    books = pd.read_csv('data/books_c.csv')
    results = books.groupby('language_code').mean().sort_values(by='average_rating',ascending=False)
    return results.to_json()

# endpoint yang menunjukkan crosstab buku berdasarkan penulis dengan metode group by
@app.route('/author_rate')
def authorrate():
    books = pd.read_csv('data/books_c.csv')
    results = books.groupby('authors').mean().sort_values(by='average_rating',ascending=False)
    return results.to_json()


# mendapatkan keseluruhan data dari <data_name>
@app.route('/data/get/<data_name>', methods=['GET']) 
def get_data(data_name): 
    data = pd.read_csv('data/' + str(data_name))
    return (data.to_json())
 

# mendapatkan data dengan filter nilai <value> pada kolom <column>
@app.route('/data/get/equal/<data_name>/<column>/<value>', methods=['GET']) 
def get_data_equal(data_name, column, value): 
    data = pd.read_csv('data/' + str(data_name))
    mask = data[column] == value
    data = data[mask]
    return (data.to_json())

if __name__ == '__main__':
    app.run(debug=True, port=5000) 