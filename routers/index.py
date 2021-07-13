from models.word import Word
from flask import Blueprint, jsonify, request, send_from_directory

router = Blueprint("url", __name__, static_url_path="")


@router.route("/word", methods=["GET"])
def getWord():
    w = Word()
    limit = request.args.get("limit", 100,  type=int)
    words = w.getAll(limit)
    return jsonify(
        [{"word": word, "weight": weight} for word, weight in words]
    )


@router.route("/word", methods=["POST"])
def postWord():
    w = Word()
    data = request.get_json(force=True)
    if(data.get("text")):
        w.add(data.get("text"))
    return jsonify({
        "message": "OK"
    })


@router.route("/")
def index():
    return send_from_directory("templates", "index.html")


@router.route("/<path:path>")
def main(path):
    return send_from_directory('templates', path)
