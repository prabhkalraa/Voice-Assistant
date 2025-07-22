import requests
import webbrowser


API_KEY = "sk-56hItCInQDVyyDFZlEzZp6i4EROXBfm1C5q84GVtoaxtk462"


def generate_and_open_image(prompt):
    print("⏳ Generating Image... Please wait...")

    response = requests.post(
        "https://api.stability.ai/v2beta/stable-image/generate/ultra",
        headers={
            "authorization": f"{API_KEY}", 
            "accept": "image/*"
        },
        files={"none": ''},
        data={
            "prompt": prompt,
            "output_format": "webp",
        },
    )

    if response.status_code == 200:
   
        image_path = "generated_image.webp"
        with open(image_path, 'wb') as file:
            file.write(response.content)
        
        print(f"✅ Image saved as {image_path}")

       
        webbrowser.open(image_path)
    
    else:
        print("❌ Error:", response.status_code, response.text)



