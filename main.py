from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from speechToText import convert_audio_format, run_medConnect_application
import os

app = Flask(__name__)
CORS(app, origins="*")


@app.route('/api/data', methods=['GET', 'POST'])
@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        audio_file = request.files.get('audio')
        source_language = request.form.get('sourceLanguage')  # Modificat aici
        target_language = request.form.get('targetLanguage')  # Modificat aici

        print(source_language, target_language)

        if audio_file:
            print("WORKSSS")
            print(audio_file)
            audio_file.save("recording.wav")

            if os.path.exists("recording.wav"):
                print("File saved successfully.")
                print("File size:", os.path.getsize("recording.wav"))  # Print the file size
            else:
                print("File not saved.")

            convert_audio_format()
            input_audio = "output.wav"
            run_medConnect_application(input_audio, source_language, target_language)
            translated_audio_path = "translated_audio.mp3"

            if os.path.exists(translated_audio_path):
                return send_file(translated_audio_path, as_attachment=False, mimetype="audio/mpeg")
            else:
                return jsonify({"message": "Translated audio not found!"}), 404
        return jsonify({"message": "No audio received!"}), 400
    else:
        return jsonify({"message": "This is your data"}), 200



if __name__ == '__main__':
    app.run(debug=True)