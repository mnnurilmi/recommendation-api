from uuid import uuid4
from fastapi import FastAPI, Response
from models import *
from helper import genreConcat, getDetails
import tensorflow as tf
import json
"""
{
  "user_request": [
    "string"
  ],
  "ids": [
    1,2,3,4,5,6,7,8,9,10
  ],
  "genres": [
    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
  ],
  "ratings": [
    1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0
  ]
}

"""
app = FastAPI()
tflite_model_path = "model.tflite"
# Create TFLite interpreter.
interpreter = tf.lite.Interpreter(tflite_model_path)
interpreter.allocate_tensors()
model = Model(
    input_details = interpreter.get_input_details(),
    output_details = interpreter.get_output_details()
)
# Find indices.
names = [
  'serving_default_context_movie_id:0',
  'serving_default_context_movie_genre:0',
  'serving_default_context_movie_rating:0',
]
indices = {i['name']: i['index'] for i in model.input_details}

@app.get("/")
def root():
    return {"message": [tf.constant(10)]}

@app.get("/api/v1/users")
async def fetch_users():
    return

@app.get("/api/v1/model")
def model_info():
    # info = {
    #     "input": model.input_details,
    #     "output": model.output_details
    # }
    return str({ \
        "input": model.input_details, \
        "output": model.output_details \
    })

@app.post("/api/v1/genre")
def getvideo(data:Genre):
  ids = tf.constant([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
  switcher = {
    "Kuliner": 2,
    "Homecare": 3,
    "Healthcare": 4,
    "Tutorial": 1,
    "Ecommerce": 5,
    "Marketing": 7,
    "Review": 6
  }
  genre = switcher.get(data.genre, 0)
  genres = []

  for i in range(20):
    genres.append(genre)

  genreTensor = tf.constant(genres)
  interpreter.set_tensor(indices[names[0]], ids)
  interpreter.set_tensor(indices[names[1]], genreTensor)

  # Run inference
  interpreter.invoke()

  top_prediction_scores = interpreter.get_tensor(model.output_details[1]['index'])

  return Response(content=getDetails(top_prediction_scores), media_type="application/json")

@app.post("/api/v1/inference")
def inference(data:Datas):
  print(data)
  ids = tf.constant(data.ids)
  genreData = genreConcat(data.ids)
  print(ids)
  interpreter.set_tensor(indices[names[0]], ids)
  genres = tf.constant(genreData)
  print(genres)
  interpreter.set_tensor(indices[names[1]], genres)
  # ratings = tf.constant(data.ratings)
  # interpreter.set_tensor(indices[names[2]], ratings)

  # Run inference.
  interpreter.invoke()
  # # Get outputs.
  top_prediction_ids = interpreter.get_tensor(model.output_details[0]['index'])
  top_prediction_scores = interpreter.get_tensor(model.output_details[1]['index'])
  print('Predicted results:')
  # print('Top ids: {}'.format(top_prediction_ids))
  print('Top scores: {}'.format(top_prediction_scores))
  return Response(content=getDetails(top_prediction_scores), media_type="application/json")


# @app.delete("/api/v1/users/{user_id}")
# async def delete_user(user_id: UUID):
#     for user in db:
#         if user.id == user_id:
#             db.remove(user_id)
#             return

# @app.put("/api/v1/users/{user_id}")
# async def update_user(user_update: UserUpdateRequest, user_id: UUID):
#     for user in db:
#         if user.id == user_id:
#             if user_update.first_name is not None:
#                 user.first_name = user_update.first_name
#             if user_update.last_name is not None:
#                 user.last_name = user_update.last_name
#             if user_update.middle_name is not None:
#                 user.middle_name = user_update.middle_name
#             if user_update.roles is not None:
#                 user.roles = user_update.roles
#             return