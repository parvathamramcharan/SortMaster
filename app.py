from flask import Flask, request, render_template, redirect, url_for
import os
import shutil

app = Flask(__name__)

# Define the upload folder path
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        path = request.form['path'].strip()
        
        if not os.path.exists(path):
            return render_template('index.html', error="The provided path does not exist.", message=None)
        
        list_of_file = os.listdir(path)
        if not list_of_file:
            return render_template('index.html', error=None, message="The directory is empty.")

        moved_files = 0
        for file in list_of_file:
            name, extension = os.path.splitext(file)
            extension = extension[1:]  # Remove the dot from the extension
            folder_path = os.path.join(path, extension)
            
            if os.path.exists(folder_path):
                shutil.move(os.path.join(path, file), os.path.join(folder_path, file))
                moved_files += 1
            else:
                os.makedirs(folder_path)
                shutil.move(os.path.join(path, file), os.path.join(folder_path, file))
                moved_files += 1
        
        return render_template('index.html', error=None, message=f"Successfully moved {moved_files} files.")
    
    return render_template('index.html', error=None, message=None)

if __name__ == '__main__':
    app.run(debug=True)
