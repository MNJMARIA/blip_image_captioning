import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image):
    if image.mode != "RGB":
        image = image.convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=30,
        num_beams=5,
        repetition_penalty=1.2,
        no_repeat_ngram_size=2,
        early_stopping=True
    )
    return processor.decode(outputs[0], skip_special_tokens=True)

def caption_image(image):
    try:
        return generate_caption(image)
    except Exception as e:
        return f"Error: {str(e)}"

interface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Image Captioning with BLIP",
    description="Upload an image to generate a caption"
)

if __name__ == "__main__":
    interface.launch(server_name="127.0.0.1", server_port=7070)