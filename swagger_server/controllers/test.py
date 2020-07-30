from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.pymongo_test
posts = db.posts
post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'Scott'
}
post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
}
new_result = posts.insert_many([post_1, post_2, post_3])
print('Multiple posts: {0}'.format(new_result.inserted_ids))
bills_post = posts.find_one({'author': 'Bill'})
print(bills_post)
print('hello!!')
bills_post = posts.find_one({'author': 'Bill'})
print(bills_post)
scotts_posts = posts.find({'author': 'Scott'})
print(scotts_posts)
for post in scotts_posts:
    print(post)