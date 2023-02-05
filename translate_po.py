import polib
import requests

def translate_po_file(file_path, target_language):
    # Read the PO file
    po = polib.pofile(file_path)

    # Translate each message
    for entry in po:
        if entry.msgstr == '':
            # Translate the message using the Google Translate API
            text = entry.msgid
            url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={target_language}&dt=t&q={text}'
            response = requests.get(url)
            result = response.json()

            # Store the translated message back into the PO file
            entry.msgstr = result[0][0][0]

    # Save the PO file
    po.save()

# Example usage: translate a PO file from English to Arabic
translate_po_file('path/to/file.po', 'ar')
