==> Chatbot_api is not working in docker so first remove that folder from docker-compose.yml and that run command
    CMD: docker-compose up --build

==> After that you can start FastAPI in locally like this:

    1. go to chatbot_api/src  # or where your FastAPI app is write.
    2. Than run CMD => uvicorn main:app --reload

==> If you complete this step your frountend is show on http://localhost:8501/ that is run from docker not your local system.

==> But the backend(FastAPI) is run on locally. That is show on http://localhost:8000/ if you dont change port. Because otherwise if you chnage the port than in this URL you add your port instead of 8000.

