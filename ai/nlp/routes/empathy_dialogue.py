# from flask import Flask, render_template, request, jsonify, make_response, Blueprint, redirect, url_for
# from transformers import AutoTokenizer
# import torch

# emphathy = Blueprint('emphathy', __name__, url_prefix='/emphathy')

# # 모델 불러오기
# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")

# empathy_model = torch.load('model/model_2c.pt')
# empathy_model.eval()

# # Define a dictionary to store chat history for each user
# emphathy_histories_ids = {}

#@empathy.route('/predict', methods=['POST'])
#def predict():
#    user_id = request.form['user_id'] 
#    user_input = request.form['user_input']

#   # Check if user ID exists in emphathy_histories_ids, if not, create a new chat history
#   if user_id not in emphathy_histories_ids:
#       emphathy_histories_ids[user_id] = []

#   # Encode user input and add eos_token to create new_user_input_ids
#   new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

#   # Concatenate chat history for the user and generate response
#   bot_input_ids = torch.cat([emphathy_histories_ids[user_id], new_user_input_ids], dim=-1) if len(emphathy_histories_ids[user_id]) >0 else new_user_input_ids
  
#   # Decode and return bot's response
#   emphathy_histories_ids[user_id] = emphathy_model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
  
#   # Decode and return bot's response
#   bot_response = tokenizer.decode(emphathy_histories_ids[user_id][:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)    

#   return make_response(bot_response, 200)

# # 이전 대화 기록 초기화
# @emphathy.route('/', methods=['DELETE'])
# def delete_user_history():
#   user_id = request.form['user_id'] 
#   if user_id in emphathy_histories_ids:
#     emphathy_histories_ids[user_id]=[]
#   return make_response('', 200)
  