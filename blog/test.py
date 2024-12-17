from forms import CommentForm


data = {
    "username": "canldleman",
    "user_email": "canldlemangmail.com",
    "text": "canldlemangmail",
}
print(
    CommentForm(
        data=data,
    )
)
