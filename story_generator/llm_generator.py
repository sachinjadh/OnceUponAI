"""Optional LLM-based generator using Hugging Face Transformers.

This file is optional and requires installing `transformers` and a suitable `torch`.
It uses the small `gpt2` model by default which can run on CPU but may be slow.
"""
from typing import Optional

try:
    from transformers import AutoTokenizer, AutoModelForCausalLM
    import torch
except Exception:
    AutoTokenizer = None
    AutoModelForCausalLM = None
    torch = None


class LLMGenerator:
    def __init__(self, model_name: str = "gpt2"):
        if AutoTokenizer is None:
            raise RuntimeError("transformers package not available. Install requirements.txt to use LLMGenerator")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate(self, prompt: str, max_length: int = 150, temperature: float = 1.0) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(
            **inputs,
            max_length=max_length,
            do_sample=True,
            temperature=temperature,
            top_k=40,  # Reduced for faster generation
            top_p=0.9,  # Slightly reduced for speed
            pad_token_id=self.tokenizer.eos_token_id,
            num_beams=1,  # Use greedy search for speed
            early_stopping=True,
        )
        text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return text
