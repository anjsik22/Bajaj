from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class InputData(BaseModel):
    name: str   # User's full name
    dob: str    # Date of Birth (DDMMYYYY)
    email: str  # User's email
    roll_number: str  # College roll number
    data: List[str]  # List of mixed inputs (numbers + alphabets)

@app.post("/bfhl")
async def process_data(input_data: InputData):
    # Generate user_id dynamically based on name and DOB
    user_id = input_data.name.replace(" ", "_").lower() + "_" + input_data.dob

    # Separate numbers and alphabets
    numbers = [item for item in input_data.data if item.isdigit()]
    alphabets = [item for item in input_data.data if item.isalpha()]

    # Find the highest alphabet (last in A-Z order)
    highest_alphabet = [max(alphabets, key=lambda x: x.lower())] if alphabets else []

    return {
        "is_success": True,
        "user_id": user_id,  
        "email": input_data.email,  
        "roll_number": input_data.roll_number,  
        "numbers": numbers,  
        "alphabets": alphabets,  
        "highest_alphabet": highest_alphabet
    }
