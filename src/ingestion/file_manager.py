from pathlib import Path

class FileManager:
    @staticmethod
    def exists(path: Path)->bool:
        return path.exists()

    @staticmethod
    def validate_csv(path: Path)->None:
        if not path.exists():
            raise FileNotFoundError(f"{path} not found")
        if path.suffix.lower()!=".csv":
            raise ValueError("Expected a CSV file")
