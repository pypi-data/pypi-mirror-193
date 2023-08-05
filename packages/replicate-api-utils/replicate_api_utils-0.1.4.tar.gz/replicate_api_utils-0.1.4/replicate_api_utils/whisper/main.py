import io
import os
from tqdm import tqdm

import replicate

def transcribe(target, to=None, duplicate="skip", **params):

    model = replicate.models.get("openai/whisper")
    version = model.versions.get("30414ee7c4fffc37e260fcab7842b5be470b9b840f2b608f5baa9bbef9a259ed")

    # Define a dictionary to map the input types to the corresponding functions
    transcribe_functions = {
        "file": transcribe_file,
        "dir": transcribe_dir,
        "file_list": transcribe_files,
        "dir_list": transcribe_dirs
    }

    # Determine the input type of the `target` parameter and call the corresponding function
    if isinstance(target, str) and os.path.isfile(target):
        input_type = "file"
    elif isinstance(target, str) and os.path.isdir(target):
        input_type = "dir"
    elif isinstance(target, list) and all([os.path.isfile(item) for item in target]):
        input_type = "file_list"
    elif isinstance(target, list) and all([os.path.isdir(item) for item in target]):
        input_type = "dir_list"
    else:
        raise ValueError("Invalid input type for `target`")

    return transcribe_functions[input_type](version, target, to=to, duplicate=duplicate, **params)

def transcribe_file(version, filepath, **params):
    # Transcribe the audio
    try:
        result = version.predict(
            audio=open(f'{filepath}', 'rb'), **params)['transcription']
    except Exception as e:
        print("Error: ", e)
        result = None

    # Return the result
    return result

def transcribe_files(version, filepaths, to=None, duplicate_options="skip", **params):
    results = []
    for filepath in tqdm(filepaths, total=len(filepaths), desc="Transcribing files"):
        # Transcribe the file
        result = transcribe_file(version, filepath, **params)
        results.append(write_or_return(filepath, result, to))
    return results

def transcribe_dir(version, folder, to=None, duplicate_options="skip", **params):
    # Get the list of filepaths in the folder
    filepaths = [os.path.join(folder, filename) for filename in os.listdir(folder)]
    return transcribe_files(version, filepaths, to, duplicate_options, **params)

def transcribe_dirs(version, folders, to=None, duplicate_options="skip", **params):
    results = []
    for folder in tqdm(folders, total=len(folders), desc="Transcribing folders"):
        result = transcribe_dir(version, folder, to, duplicate_options, **params)
        results.extend(result)
    return results


# Define a helper function to write the results to a file or return them as a string
def write_or_return(filename, result, folder=None):
    if filename is None:
        raise ValueError("Transcribed filename must be specified")
    elif result is None:
        return None
    elif folder is None:
        return result
    else:
        file_path = os.path.join(folder, filename)
        with open(file_path, "w") as f:
            f.write(result)
        print(f"Transcribed file saved to {file_path}")