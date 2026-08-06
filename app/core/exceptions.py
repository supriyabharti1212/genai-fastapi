from fastapi import HTTPException


class LLMException(HTTPException):
    def __init__(self, detail="LLM is unavailable"):
        super().__init__(
            status_code=500,
            detail=detail
        )