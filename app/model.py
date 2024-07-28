from transformers import pipeline

class StoryGenerator:

    def __init__(self):
        self.generator = pipeline('text-generation', model='gpt2-large')

    def generate_story(self, keywords):
        prompt = f"Once upon a time, {', '.join(keywords)}, and they lived happily ever after."
        story = self.generator(prompt,max_length=200)[0]['generated_text']
        return story