# Clipboard Text-to-Speech

Clipboard Text-to-Speech is a simple desktop application that reads the text from the clipboard and vocalizes it.

## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine:
<pre>
   git clone https://github.com/andriangashper/clipboard-text-to-speech.git
</pre>

2. Create a Docker image for the project:
<pre>
    docker build -t clipboard-text-to-speech .
</pre>

3. Run the Docker image:
<pre>
    docker run clipboard-text-to-speech
</pre>

This will start the application, which will monitor your clipboard for changes and read out the copied text using text-to-speech conversion.

Make sure you have Docker installed on your system before running the application.

**Note**:  One can use PyInstaller to create a standalone executable (e.g., app.exe on Windows or app on Linux/macOS), it includes the Python interpreter and any necessary packages and dependencies within the executable itself. This means that the Python interpreter and required libraries are bundled into the single executable file.