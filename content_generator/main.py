from transformers import GPT2LMHeadModel, GPT2Tokenizer

class ContentGenerator:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")

    def generate_content(self, prompt, max_length=200):
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=max_length, num_return_sequences=1)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    generator = ContentGenerator()
    content = generator.generate_content("Write a blog post about AI in healthcare.")
    print(content)
