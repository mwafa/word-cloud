from models.word import Word
from flask import Blueprint, jsonify, request

router = Blueprint("url", __name__)


@router.route("/")
def main():
    return jsonify({
        "error": False,
        "message": "OK"
    })


@router.route("/word", methods=["GET"])
def getWord():
    w = Word()
    words = w.getAll()
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
