import logging
import json
from json import JSONDecodeError
from pathlib import Path

logging.basicConfig(filename='json_Cherniai.log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    encoding='utf-8')

def validation_json_file(folder_path):
    folder_path = Path(folder_path)
    invalid_files = []

    for file in folder_path.iterdir():
        if file.is_file() and file.name.endswith(".json"):
            try:
                with open(file, "r", encoding="utf-8") as f:
                    json.load(f)
            except JSONDecodeError:
                invalid_files.append(file.name)

    if invalid_files:
        logging.info(f"Невалідні файли: {invalid_files}")
    else:
        logging.info("Всі файли валідні")

current_folder = Path(__file__).parent
validation_json_file(current_folder)
