from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate,PostResponse


app = FastAPI()

text_posts={
    1:{'title':'new post',"content":"some trash"},
    2:{'title':'old post',"content":"old trash"},
    3:{'title':'new post',"content":"some trash"},
    4:{'title':'old post',"content":"old trash"},
}

@app.get("/posts")
def get_all_posts(limit:int=None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="post not found")
    return text_posts.get(id)

@app.post('/posts')
def create_post(post:PostCreate)->PostResponse:
    new_post = {'title':post.title,'content':post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post

