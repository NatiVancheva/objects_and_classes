class Comment:
    def __init__(self, username, contest, likes=0):
        self.username = username
        self.contest = contest
        self.likes = likes
comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.contest)
print(comment.likes)
