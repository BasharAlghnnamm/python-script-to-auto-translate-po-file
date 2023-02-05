Save the code in a file with a .py extension, 
Install the required libraries by running the following command in your terminal or command prompt:

    pip install polib requests

Navigate to the directory where the translate_po.py file is located.

Run the script by entering the following command in your terminal or command prompt:
    
    python translate_po.py path/to/file.po ar

Replace path/to/file.po with the path to your PO file and ar with the target language code (in this case, Arabic).

The script will read the PO file, translate each message using the Google Translate API, and save the translated PO file in the same location.

test on Debian 10, debian 11 , ubunut 20.04 
