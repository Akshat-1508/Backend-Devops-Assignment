import os
import uuid


def save_uploaded_file(upload_file, upload_folder):
    """
    Save uploaded CSV to uploads folder and
    return the saved filename.
    """

    os.makedirs(upload_folder, exist_ok=True)

    filename = f"{uuid.uuid4()}_{upload_file.filename}"

    filepath = os.path.join(upload_folder, filename)

    with open(filepath, "wb") as buffer:
        buffer.write(upload_file.file.read())

    return filename, filepath