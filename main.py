from core.config import LOGGING_LEVEL, setup_logging, APP_PORT

if __name__ == "__main__":
    import uvicorn
    setup_logging(LOGGING_LEVEL)
    uvicorn.run("core.civitaekwondo:app", host="127.0.0.1", port=APP_PORT, reload=False)
