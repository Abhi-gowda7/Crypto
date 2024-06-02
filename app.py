from flask import Flask, request, render_template

app = Flask(__name__)

# Caesar Cipher function
def caesar_cipher(choice, text):
    mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    if choice == 1:  # Encryption
        name = text.lower()
        cipher = []
        for k in range(len(name)):
            if name[k] == " ":
                cipher.append(" ")
            else:
                for j in range(len(mylist)):
                    if name[k] == mylist[j]:
                        ans = (j + 3) % 26
                        cipher.append(mylist[ans])
                        break
        return ''.join(cipher)
    
    elif choice == 2:  # Decryption
        cipher_txt = text.lower()
        plain = []
        for k in range(len(cipher_txt)):
            if cipher_txt[k] == " ":
                plain.append(" ")
            else:
                for j in range(len(mylist)):
                    if cipher_txt[k] == mylist[j]:
                        if j >= 3:
                            ans = (j - 3) % 26
                        else:
                            ans = ((j - 3) + 26) % 26
                        plain.append(mylist[ans])
                        break
        return ''.join(plain)
    
    else:
        return "Choose correct option"

# Route for handling the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    result_text = None
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        choice = int(request.form['choice'])
        result_text = caesar_cipher(choice, text)
    return render_template('index.html', result_text=result_text)

if __name__ == '__main__':
    app.run(debug=True)
