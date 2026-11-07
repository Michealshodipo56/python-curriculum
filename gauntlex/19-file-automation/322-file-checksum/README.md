# Fingerprint a File

## Description
Large files should be hashed without loading all bytes into memory. Compute a content fingerprint from the exact raw byte stream.

## Requirements
- Implement `file_checksum(path)` in `starter/solution.py`.
- Read the file at `path` in bounded chunks.
- Compute SHA-256 over its raw bytes, without text decoding or newline changes.
- Return the lowercase hexadecimal digest.
- Do not modify the file.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Tips
- Why must binary file bytes be hashed without text conversion?

## Example Behavior
A file containing the bytes `abc` has SHA-256 digest `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`.
