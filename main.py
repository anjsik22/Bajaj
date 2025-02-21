from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# ✅ This should be present
app = FastAPI()  

class InputData(BaseModel):
    data: List[str]

@app.post("/bfhl")
async def process_data(input_data: InputData):
    user_id = "john_doe_17091999"
    email = "john@xyz.com"
    roll_number = "ABCD123"

    numbers = [item for item in input_data.data if item.isdigit()]
    alphabets = [item for item in input_data.data if item.isalpha()]
    highest_alphabet = [max(alphabets, key=lambda x: x.lower())] if alphabets else []

    return {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }

@app.get("/bfhl")
async def get_operation_code():
    return {"operation_code": 1}
