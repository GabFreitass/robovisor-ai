from flask import Blueprint, request, jsonify
import utils

transcribe = Blueprint("transcribe", __name__, url_prefix="/transcribe")


@transcribe.route("/file", methods=["POST"])
def transcribe_audio():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    if file:
        text = utils.transcribe(audio_file=file)
