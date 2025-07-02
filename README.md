# custom_skill_api
custom skill api for chatbot

# Activate the virtual environment.
source .venv/bin/activate
# Run Server
python -m app.main
uvicorn app.main:app --host 192.168.3.204 --port 8010 --reload
# Update Dependences
pip freeze | grep -v "python-apt" > requirements.txt
pip install -r requirements.txt
# Install playwright
playwright install-deps
playwright install

deactivate

