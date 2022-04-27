# Chatbot API


For init the API:

>
> uvicorn main:app --host 0.0.0.0 --port 8000
>

You can set the pytest with the following command:

>
> python -m pytest
>

# Kill process 



find the process using the port
>
> lsof -i :8000
>

and kill it
>
>kill -9 process_id
>