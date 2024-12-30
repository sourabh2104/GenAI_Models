from transformers import T5Tokenizer, T5ForConditionalGeneration

class HashtagGenerator:
    def __init__(self):
        self.tokenizer = T5Tokenizer.from_pretrained("t5-small")
        self.model = T5ForConditionalGeneration.from_pretrained("t5-small")

    def generate_hashtags(self, content, max_length=20):
        input_text = f"generate hashtags: {content}"
        inputs = self.tokenizer.encode(input_text, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=max_length, num_return_sequences=1)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    generator = HashtagGenerator()
    hashtags = generator.generate_hashtags("Exploring the benefits of AI in modern healthcare.")
    print(hashtags)
