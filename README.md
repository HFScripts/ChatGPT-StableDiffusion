# ChatGPT-StableDiffusion

This repository contains the code for running stable diffusion prompts using OpenAI's GPT-3.5 model. The `stablegpt.py` file provided in this repository allows you to generate multiple stable diffusion prompts based on example prompts and user input.

## Requirements

To run the code, make sure you have the following requirements fulfilled:

- Python 3.x
- OpenAI Python library

## Installation

1. Clone this repository to your local machine or download the `stablegpt.py` file directly.

2. Install the required dependencies by running the following command:

```pip install openai```


## Usage

1. Open the `stablegpt.py` file.

2. Set your OpenAI API key by replacing `"APIKEYHERE"` with your actual API key. If you don't have an API key, you can obtain one from the [OpenAI website](https://platform.openai.com/signup).

3. Modify the `example_prompt_list` variable to include your desired example prompts. Each prompt should be a string enclosed in double quotes (`"`), and they should be comma-separated. You can add or remove example prompts as needed.

4. Run the script by executing the following command:

```python stablegpt.py```


5. You will be prompted to enter your text. Provide the desired input and press Enter.

6. The script will generate stable diffusion prompts based on the example prompts and your input. The generated prompts will be displayed in the console.

## Contributing

Contributions to this repository are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
Will look at implementing a proper StableDiffusion setup in the future for the 'for loop' left at the bottom of the script.

## License

This project is licensed under the [MIT License](LICENSE).
