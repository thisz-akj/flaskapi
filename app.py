from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [
    {
        "id": 0,
        "author": "Azad Kumar",
        "language": "English",
        "Title": "Things Fall Apart"
    },
    {
        "id": 1,
        "author": "Kushal",
        "language": "English",
        "Title": "Fairy Tales"
    }
]

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == "GET":
        if len(books_list) > 0:
            return jsonify(books_list), 200
        else:
            return jsonify({"error": "No books found"}), 404

    if request.method == "POST":
        # Ensure we're expecting JSON
        data = request.get_json()
        
        # Return error if no JSON is provided
        if not data:
            return jsonify({"error": "Bad request. Expected JSON format"}), 400
        
        new_author = data.get('author')
        new_lan = data.get('language')
        new_title = data.get('title')
        
        # Return error if fields are missing
        if not new_author or not new_lan or not new_title:
            return jsonify({"error": "Missing fields"}), 400
        
        # Create new book entry
        iD = books_list[-1]['id'] + 1
        new_obj = {
            'id': iD,
            'author': new_author,
            'language': new_lan,
            'title': new_title
        }
        
        books_list.append(new_obj)
        return jsonify(books_list), 201

if __name__ == '__main__':
    app.run(debug=True)
