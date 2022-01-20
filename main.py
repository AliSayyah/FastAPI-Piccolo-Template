if __name__ == "__main__":
    import uvicorn
    from settings import RELOAD

    kwargs = {
        "reload": RELOAD,
        "host": "0.0.0.0"
    }

    uvicorn.run("app:app", **kwargs)
