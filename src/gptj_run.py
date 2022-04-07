#!/usr/bin/env python3


from transformers import GPTJForCausalLM, AutoTokenizer
import torch
import sys

model = GPTJForCausalLM.from_pretrained(
    "EleutherAI/gpt-j-6B",

)

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")

prompt = (
    "In a shocking finding, scientists discovered a herd of unicorns living in a remote, "
    "previously unexplored valley, in the Andes Mountains. Even more surprising to the "
    "researchers was the fact that the unicorns spoke perfect English."
)

print(len(sys.argv))

if len(sys.argv) > 1:
    prompt = [sys.argv[i] for i in range(1,len(sys.argv))]
    prompt = ' '.join(prompt)

print (prompt)

while True:

    input_ids = tokenizer(prompt, return_tensors="pt").input_ids

    gen_tokens = model.generate(
        input_ids,
        do_sample=True,
        temperature=0.9,
        max_length=100,
    )
    gen_text = tokenizer.batch_decode(gen_tokens)[0]

    print(gen_text)

    prompt = input("> ")
