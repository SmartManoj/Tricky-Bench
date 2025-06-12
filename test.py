import litellm

msg = '''
What weighs more: 20 pounds of bricks or 20 feathers?

Read the question carefully and repeat it exactly before
answering. Carefully work through the problem
'''
import os
model = 'openrouter/google/gemini-2.5-pro-preview'
model = 'openrouter/anthropic/claude-opus-4'
model = 'openrouter/x-ai/grok-3-beta'
model = 'openrouter/qwen/qwen3-235b-a22b:free'
completion = litellm.completion(
    model=model, 
    messages=[{"role": "user", "content": msg}], 
    stream=True, 
    seed=42, 
    temperature=0.0,
    )
for chunk in completion:
    data = chunk.choices[0].delta.content
    if data:
        print(data, end='', flush=True)
print()






