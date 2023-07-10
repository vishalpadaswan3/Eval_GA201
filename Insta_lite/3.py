from flask import Flask, jsonify, request

app = Flask(__name__)

id = 1
InstaPost = []

@app.route('/posts',methods=["POST"])
def createInstaPost():
    global id
    email = request.json.get('email')
    username = request.json.get('username')
    captionText = request.json.get('captionText')
    post = {'id':id,'email':email,"username":username,"captionText":captionText}
    id = id + 1
    InstaPost.append(post)
    return jsonify({"message":"Post created Successfully"})


@app.route('/posts',methods=["GET"])
def getInstaPost():
    return jsonify(InstaPost)


@app.route('/posts',methods=["DELETE"])
def createInstaPost(deleteID):
    for post in InstaPost:
        if post['id'] == deleteID:
        InstaPost.remove(post)
    return jsonify({"message":"Post deleted Successfully"})





