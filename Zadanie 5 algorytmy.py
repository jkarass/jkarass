from flask import Flask, request, jsonify

app = Flask(__name__)

def count_characters(text):
    char_counts = [0] * 256  # Stworzenie listy o długości 256 (zakładając ASCII)
    
    # Liczenie wystąpień każdego znaku w tekście
    for char in text:
        char_counts[ord(char)] += 1
    
    # Stworzenie słownika zawierającego wystąpienia znaków
    characters_count = {}
    for i in range(256):
        if char_counts[i] > 0:
            characters_count[chr(i)] = char_counts[i]
    
    return characters_count

def count_words(text, target_words):
    text = text.lower()
    words_count = {word: 0 for word in target_words}
    
    # Podział tekstu na słowa
    text_words = text.split()
    
    # Liczenie wystąpień każdego słowa
    for word in text_words:
        if word in words_count:
            words_count[word] += 1
    
    return words_count

@app.route('/count_characters', methods=['GET'])
def calculate_character_count():
    if request.method == 'GET':
        input_text = request.args.get('text')
        input_words = request.args.get('words')  # Dodanie pobierania drugiego parametru
        
        if input_text and input_words:
            character_count = count_characters(input_text)
            sorted_characters = dict(sorted(character_count.items()))
            
            words_list = input_words.split(',')
            words_count = count_words(input_text, words_list)
            sorted_words = dict(sorted(words_count.items()))
            
            return jsonify({"characters_count": sorted_characters, "words_count": sorted_words})
        else:
            return jsonify({'error': 'Brak tekstu lub słów w zapytaniu GET lub tekst jest pusty'})
    else:
        return jsonify({'error': 'Metoda HTTP nieobsługiwana'})

if __name__ == '__main__':
    app.run(debug=True)
