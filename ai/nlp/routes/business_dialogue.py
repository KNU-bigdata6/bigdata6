from flask import Flask, render_template, request, jsonify, make_response, Blueprint, redirect, url_for
from transformers import AutoTokenizer
import torch

business = Blueprint('business', __name__, url_prefix='/business')

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
business_model = torch.load('/ai/nlp/model/business_small_model.pt')
business_model.eval()

# Define a dictionary to store chat history for each user
business_histories_ids = {}
sub_history = {}
user_cnt = {}

@business.route('/predict', methods=['POST'])
def predict():
  user_id = request.form['user_id']
  user_input = request.form['user_input']
  tmp = 0

  # Check if user ID exists in daily_histories_ids, if not, create a new chat history
  if user_id not in business_histories_ids:
      business_histories_ids[user_id] = []
      sub_history[user_id] = dict()
      user_cnt[user_id] = 0

  # Encode user input and add eos_token to create new_user_input_ids
  user_cnt[user_id] += 1
  new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

  if user_cnt[user_id]>1:
    tmp =-1*sub_history[user_id][user_cnt[user_id]-1]
  bot_input_ids = torch.cat([business_histories_ids[user_id][:, tmp:], new_user_input_ids], dim=-1) if len(business_histories_ids[user_id]) >0 else new_user_input_ids

  # 모델을 통해 챗봇 출력 생성
  business_histories_ids[user_id] = business_model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id,no_repeat_ngram_size=3,
      do_sample=True,
      top_k=10,
      top_p=0.7,
      temperature = 0.8)

  if user_cnt[user_id]>1:
    sub_history[user_id][user_cnt[user_id]] = len(business_histories_ids[user_id][0]) - sub_history[user_id][user_cnt[user_id]-1]
  else:
    sub_history[user_id][user_cnt[user_id]] = len(business_histories_ids[user_id][0])


  # 챗봇 출력 내역 출력
  bot_response = tokenizer.decode(business_histories_ids[user_id][:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

  return make_response(bot_response, 200)

# 이전 대화 기록 초기화
@business.route('/', methods=['DELETE'])
def delete_user_history():

  user_id = request.form['user_id']

  if user_id in business_histories_ids:
      business_histories_ids[user_id] = []
      sub_history[user_id] = dict()
      user_cnt[user_id] = 0

  return make_response('', 200)
