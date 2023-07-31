python3 -m venv venv
source venv/bin/activate
python3 -m pip install notebook
# python3 -m pip install ipykernel
python3 -m ipykernel install --user --name=myproject
jupyter-notebook
