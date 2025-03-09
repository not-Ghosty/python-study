import os

def start():
    os.system("uvicorn server:app --port 3000 --reload")

if __name__ == "__main__":
    start()
