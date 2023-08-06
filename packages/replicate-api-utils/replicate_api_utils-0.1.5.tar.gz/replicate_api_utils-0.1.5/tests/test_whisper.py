import os
import pytest
from unittest.mock import MagicMock
from tempfile import NamedTemporaryFile, TemporaryDirectory
from replicate_api_utils.whisper import transcribe

def test_transcribe_file_exists():
    # Test that transcribe raises an error if the file does not exist
    with pytest.raises(ValueError):
        version = MagicMock()
        version.predict.return_value = {"transcription": "hello world"}
        transcribe("nonexistent.wav", version=version)

def test_transcribe_dir_exists():
    # Test that transcribe raises an error if the directory does not exist
    with pytest.raises(ValueError): # Create a mock Version object
        version = MagicMock()
        version.predict.return_value = {"transcription": "hello world"}
        transcribe("nonexistent_directory/", version=version)

def test_transcribe_file():
    # Test that transcribe can transcribe a single file and return the result
    with NamedTemporaryFile(suffix=".wav") as test_file:
        # Create a mock Version object
        version = MagicMock()
        version.predict.return_value = {"transcription": "hello world"}

        # Call the transcribe function
        result = transcribe(test_file.name, version=version)

        # Verify that the mock Version object was called
        assert version.predict.called

        # Verify that the correct result was returned
        assert result == ["hello world"]

def test_transcribe_files():
    # Test that transcribe can transcribe multiple files and return the results
    with TemporaryDirectory() as output_dir:
        with NamedTemporaryFile(suffix=".wav") as test_file1, NamedTemporaryFile(suffix=".wav") as test_file2:
            # Create a mock Version object
            version = MagicMock()
            version.predict.side_effect = [{"transcription": "hello"}, {"transcription": "world"}]

            # Call the transcribe function
            result = transcribe([test_file1.name, test_file2.name], dest=output_dir, version=version)

            # Verify that the mock Version object was called twice
            assert version.predict.call_count == 2

            # Verify that the output files were created
            assert os.path.exists(os.path.join(output_dir, os.path.basename(test_file1.name).replace(".wav", ".txt")))
            assert os.path.exists(os.path.join(output_dir, os.path.basename(test_file2.name).replace(".wav", ".txt")))

            # Verify that the correct results were returned
            assert result == ["hello", "world"]

def test_transcribe_dir():
    # Test that transcribe can transcribe all files in a directory and return the results
    with TemporaryDirectory() as test_dir, TemporaryDirectory() as output_dir:
        with NamedTemporaryFile(suffix=".wav", dir=test_dir) as test_file1, NamedTemporaryFile(suffix=".wav", dir=test_dir) as test_file2:
            # Create a mock Version object
            version = MagicMock()
            version.predict.side_effect = [{"transcription": "hello"}, {"transcription": "world"}]

            # Call the transcribe function
            result = transcribe(test_dir, dest=output_dir, version=version)

            # Verify that the mock Version object was called twice
            assert version.predict.call_count == 2

            # Verify that the output files were created
            assert os.path.exists(os.path.join(output_dir, os.path.basename(test_file1.name).replace(".wav", ".txt")))
            assert os.path.exists(os.path.join(output_dir, os.path.basename(test_file2.name).replace(".wav", ".txt")))

            # Verify that the correct results were returned
            assert result == ["hello", "world"]

def test_transcribe_duplicate_skip():
    # Test that transcribe skips files with the same name in the output directory
    with TemporaryDirectory() as output_dir:
        with NamedTemporaryFile(suffix=".wav") as test_file:
            # Create a mock Version object
            version = MagicMock()
            version.predict.return_value = {"transcription": "hello world"}

            # Call the transcribe function twice on

def test_transcribe_duplicate_skip():
    # Create a temporary test file and directory
    with NamedTemporaryFile(suffix=".wav") as test_file, TemporaryDirectory() as output_dir:
        # Create a mock Version object
        version = MagicMock()
        version.predict.return_value = {"transcription": "hello world"}

        # Call the transcribe function twice with the same file and the `duplicate="skip"` option
        result_1 = transcribe(test_file.name, dest=output_dir, version=version, duplicate="skip")
        result_2 = transcribe(test_file.name, dest=output_dir, version=version, duplicate="skip")

        # Verify that the mock Version object was called twice
        assert version.predict.call_count == 2

        # Verify that the output file was created once
        assert os.path.exists(os.path.join(output_dir, os.path.basename(test_file.name).replace(".wav", ".txt")))

        # Verify that the correct result was returned both times
        assert result_1 == ["hello world"]
        assert result_2 == ["hello world"]

def test_transcribe_create_dirs_true(monkeypatch):
    # Create a mock Version object
    version = MagicMock()
    version.predict.return_value = {"transcription": "hello world"}
    # Create a temporary test file and directory
    with NamedTemporaryFile(suffix=".wav") as test_file, TemporaryDirectory() as output_dir:
        # Call the transcribe function with create_dirs=True
        transcribe(test_file.name, dest=os.path.join(output_dir, "subdir", "subsubdir"), version=version, create_dirs=True)

        # Verify that the output file was created in the correct directory
        assert os.path.exists(os.path.join(output_dir, "subdir", "subsubdir", os.path.basename(test_file.name).replace(".wav", ".txt")))

def test_transcribe_create_dirs_false(monkeypatch):
    # Create a mock Version object
    version = MagicMock()
    version.predict.return_value = {"transcription": "hello world"}
    # Create a temporary test file and directory
    with NamedTemporaryFile(suffix=".wav") as test_file, TemporaryDirectory() as output_dir:
        # Call the transcribe function with create_dirs=False
        with pytest.raises(ValueError):
            transcribe(test_file.name, dest=os.path.join(output_dir, "subdir", "subsubdir"), version=version, create_dirs=False)
