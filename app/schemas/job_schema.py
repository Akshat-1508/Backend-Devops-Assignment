from pydantic import BaseModel


class JobResponse(BaseModel):

    id: int

    filename: str

    status: str

    class Config:
        from_attributes = True