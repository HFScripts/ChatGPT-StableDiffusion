import openai
import json
import base64
import requests

openai.api_key = "sk-APIKEY"
txt2img_url = 'http://127.0.0.1:7861/sdapi/v1/txt2img'
user_input = input("Enter your text: ")
how_many_prompts = 5

example_prompt_list = [
    "example Prompt: Iron Man, (Arnold Tsang, Toru Nakayama), Masterpiece, Studio Quality, 6k , toa, toaair, 1boy, glowing, axe, mecha, science_fiction, solo, weapon, jungle , green_background, nature, outdoors, solo, tree, weapon, mask, dynamic lighting, detailed shading, digital texture painting",
    "example Prompt: Iron Man, (Arnold Tsang, Toru Nakayama), Masterpiece, Studio Quality, 6k , toa, toaair, 1boy, glowing, axe, mecha, science_fiction, solo, weapon, jungle , green_background, nature, outdoors, solo, tree, weapon, mask, dynamic lighting, detailed shading, digital texture painting",
    "example Prompt: (Pope Francis) wearing leather jacket is a DJ in a nightclub, mixing live on stage, giant mixing table, 4k resolution, a masterpiece",
    "example Prompt: portrait Anime black girl cute-fine-face, pretty face, realistic shaded Perfect face, fine details. Anime. realistic shaded lighting by Ilya Kuvshinov Giuseppe Dangelico Pino and Michael Garmash and Rob Rey, IAMAG premiere, WLOP matte print, cute freckles, masterpiece",
    "example Prompt: young Disney socialite wearing a beige miniskirt, dark brown turtleneck sweater, small neckless, cute-fine-face, anime. illustration, realistic shaded perfect face, brown hair, grey eyes, fine details, realistic shaded lighting by ilya kuvshinov giuseppe dangelico pino and michael garmash and rob rey, iamag premiere, wlop matte print, 4k resolution, a masterpiece",
    "example Prompt: Cute small dog sitting in a movie theater eating popcorn watching a movie ,unreal engine, cozy indoor lighting, artstation, detailed, digital painting,cinematic,character design by mark ryden and pixar and hayao miyazaki, unreal 5, daz, hyperrealistic, octane render",
    "example Prompt: Cute small cat sitting in a movie theater eating chicken wiggs watching a movie ,unreal engine, cozy indoor lighting, artstation, detailed, digital painting,cinematic,character design by mark ryden and pixar and hayao miyazaki, unreal 5, daz, hyperrealistic, octane render",
    "example Prompt: crane buckskin bracelet with crane features, rich details, fine carvings, studio lighting",
    "example Prompt: fox bracelet made of buckskin with fox features, rich details, fine carvings, studio lighting",
    "example Prompt: Parisian luxurious interior penthouse bedroom, dark walls, wooden panels",
    "example Prompt: houses in front, houses background, straight houses, digital art, smooth, sharp focus, gravity falls style, doraemon style, shinchan style, anime style",
    "example Prompt: cute girl, crop-top, blond hair, black glasses, stretching, with background by greg rutkowski makoto shinkai kyoto animation key art feminine mid shot",
    "example Prompt: High quality 8K painting impressionist style of a Japanese modern city street with a girl on the foreground wearing a traditional wedding dress with a fox mask, staring at the sky, daylight",
    "example Prompt: the street of amedieval fantasy town, at dawn, dark, 4k, highly detailed",
    "example Prompt: a highly detailed matte painting of a man on a hill watching a rocket launch in the distance by studio ghibli, makoto shinkai, by artgerm, by wlop, by greg rutkowski, volumetric lighting, octane render, 4 k resolution, trending on artstation, masterpiece | hyperrealism| highly detailed| insanely detailed| intricate| cinematic lighting| depth of field",
    "example Prompt: electronik robot and ofice ,unreal engine, cozy indoor lighting, artstation, detailed, digital painting,cinematic,character design by mark ryden and pixar and hayao miyazaki, unreal 5, daz, hyperrealistic, octane render",
    "example Prompt: Cute small Fox sitting in a movie theater eating popcorn watching a movie ,unreal engine, cozy indoor lighting, artstation, detailed, digital painting,cinematic,character design by mark ryden and pixar and hayao miyazaki, unreal 5, daz, hyperrealistic, octane render",
    "example Prompt: cute toy owl made of suede, geometric accurate, relief on skin, plastic relief surface of body, intricate details, cinematic"
]


def generate_gpt_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].message['content'].strip()

messages = []

GPT_prompt = f"\n{example_prompt_list} \n\n\nbased on the stable diffusion prompts, create {how_many_prompts} different stable diffusion prompts for: '{user_input}' following the same format."
messages.append({"role": "user", "content": GPT_prompt})

stable_diffusion_command = generate_gpt_response(messages)
print(f"{GPT_prompt}\n")
responses = stable_diffusion_command.split('\n')  # Split the text based on new lines

# Remove empty lines and leading/trailing whitespace
responses = [response.split('. ', 1)[-1].strip() for response in responses if response.strip()]


def submit_post(url: str, data: dict):
    return requests.post(url, data=json.dumps(data))

def save_encoded_image(b64_image: str, output_path: str):
    with open(output_path, "wb") as image_file:
        image_file.write(base64.b64decode(b64_image))

# Print the separated responses
for i, response in enumerate(responses, 1):
    print(f"{response}\n")
    data = {f"'promt:' {response}"}
    response = submit_post(txt2img_url, data)
    save_encoded_image(response.json()['images'[0], 'dog.png'])
