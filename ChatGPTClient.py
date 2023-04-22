import openai

open_ai_api_key = <yourAPIKey>

while True:
  # select the model you want to use
  model = <model-name>
  user_input = input("Enter your query:)
  
  if 'quit' in user_input:
      break
  
  query_response = openai.Completion.create(engine=model, prompt = user_input, max_tokens = 2048, n=1, stop = None, temperature = 0.5)
  
  response = query_response.choices[0].text
  
  print(response) 
  
