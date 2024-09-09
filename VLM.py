from flask import Flask, request, jsonify, render_template
from PIL import Image
from transformers import AutoModelForCausalLM, AutoProcessor
from torch import bfloat16
import transformers
import io

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

# Load the model and processor
model_id = 'DysfunctionalHuman/TestCaseGenerationVLM'

# Define the quantization configuration
bnb_config = transformers.BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type='nf4',
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=bfloat16
)

# Load the model and processor
model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-3-vision-128k-instruct",
                                             device_map="cuda",
                                             trust_remote_code=True,
                                             quantization_config=bnb_config,
                                             torch_dtype="auto",
                                             _attn_implementation="eager")

processor = AutoProcessor.from_pretrained("microsoft/Phi-3-vision-128k-instruct", trust_remote_code=True)

def generate_test_instructions(screenshots, context):
    # Load the image
    image = Image.open(screenshots)

    # Define the messages (including any provided context)
    messages = [
        {
            "role": "user", 
            "content": "<|image_1|>\nYou are an AI designed to generate detailed test cases for web applications. The image provided is a screenshot of a web application. Based on this image, generate a test case that includes:\n\n1. **Description:** A brief overview of what is being tested.\n2. **Pre-conditions:** The setup required before testing.\n3. **Testing Steps:** A clear, step-by-step guide on how to execute the test.\n4. **Expected Result:** What the expected outcome should be if the feature works correctly."
        }
    ]

    # Prepare the prompt using the processor
    print(type(image))
    print(type(screenshots))
    prompt = processor.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    # Process the image and prepare the input tensors
    inputs = processor(prompt, [image], return_tensors="pt").to("cuda:0")

    # Set generation parameters
    generation_args = {
        "max_new_tokens": 500,
        "temperature": 0.0,
        "do_sample": False,
    }

    # Generate the test case based on the image and prompt
    generate_ids = model.generate(**inputs, eos_token_id=processor.tokenizer.eos_token_id, **generation_args)
    generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:]  # Trim the prompt part from the output

    # Decode the generated IDs to get the text output
    response = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    print('hi')
    return response


@app.route('/generate-instructions', methods=['POST'])
def generate_instructions():
    context = request.form.get('context')
    screenshot = request.files['screenshots']  # Single file input
    
    # Convert the uploaded file to a format compatible with PIL
    image_bytes = io.BytesIO(screenshot.read())
    
    # Generate the test case
    test_case = generate_test_instructions(image_bytes, context)

    return render_template('index.html', test_case=str(test_case).replace('**',''))


if __name__ == '__main__':
    app.run(debug=True)
