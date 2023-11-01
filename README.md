# Clipboard Text-to-Speech

Clipboard Text-to-Speech is a simple desktop application that reads the text from the clipboard and vocalizes it.

## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine:
<pre>
   git clone https://github.com/andriangashper/clipboard-text-to-speech.git
</pre>

2. Create a python virtual environment:
<pre>
    python -m venv "venv_name"
</pre>

3. Activate the environment:

On Windows:
<pre>
    "venv_name"/Scripts/activate
</pre>

On Linux:
<pre>
    source "venv_name"/bin/activate
</pre>

4. Install the required packages:
<pre>
    pip install -r requirements.txt
</pre>

5. Run the app.py file:
<pre>
    python app.py
</pre>

This will start the application, which will monitor your clipboard for changes and read out the copied text using text-to-speech conversion.


**Note**:  One can use PyInstaller to create a standalone executable (e.g., app.exe on Windows or app on Linux/macOS), it includes the Python interpreter and any necessary packages and dependencies within the executable itself. This means that the Python interpreter and required libraries are bundled into the single executable file.

To do this, you'd first install pyinstaller, and then run a command to create the executable. Here's a general idea of the steps (you may need to adjust them based on your specific script and environment):

First, install pyinstaller:
<pre>
pip install pyinstaller
</pre>

Then, create the executable:
<pre>
pyinstaller --onefile app.py
</pre>

This will create a standalone executable file in the dist directory. You can run this executable without opening a terminal window.