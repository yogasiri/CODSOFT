import os
import warnings

# 🔹 Hide warnings and logs
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["TRANSFORMERS_NO_ADVISORY_WARNINGS"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

warnings.filterwarnings("ignore")

from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer, logging
from PIL import Image
import torch

logging.set_verbosity_error()

# 🔹 Load model from local cache
model = VisionEncoderDecoderModel.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning",
    local_files_only=True
)

feature_extractor = ViTImageProcessor.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning",
    local_files_only=True
)

tokenizer = AutoTokenizer.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning",
    local_files_only=True
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

print("AI Image Captioning System Ready ✅")
print("Type image name (example: test.jpg)")
print("Type 'quit' to exit\n")

# 🔹 Continuous loop
while True:
    image_name = input("Enter image file name: ").strip()

    if image_name.lower() == "quit":
        print("Exiting program 👋")
        break

    if not os.path.exists(image_name):
        print("File not found ❌\n")
        continue

    try:
        image = Image.open(image_name).convert("RGB")
        pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values
        pixel_values = pixel_values.to(device)

        with torch.no_grad():
            output_ids = model.generate(pixel_values, max_length=50)

        caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)

        print("Description:", caption, "\n")

    except Exception:
        print("Error processing image ❌\n")
