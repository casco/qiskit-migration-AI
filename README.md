# Initial steps

python3 -m venv venv

source venv/bin/activate

pip install openai

pip freeze > requirements.txt
 
# To recreate after clone

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Usage
export OPENAI_API_KEY="your-api-key"
python one-shot-prompt.py case-x/prompt.txt case-x/response.txt