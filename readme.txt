pip install virtualenv


python -m virtualenv <env name>


env\Scripts\activate




deactivate [for deactivating]



pip freeze > requirements.txt


python -m uvicorn main:app --reload