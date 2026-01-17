import subprocess
from datetime import datetime

import tokenize
import hashlib
from pathlib import Path
import base64

IGNORED_TOKENS = {
    tokenize.COMMENT,
    tokenize.NL,
    tokenize.NEWLINE,
    tokenize.ENCODING,
    tokenize.ENDMARKER,
    tokenize.INDENT,
    tokenize.DEDENT,
}

def hash_python_file(path: Path) -> str:
    hasher = hashlib.sha256()
    hasher.update(path.name.encode("utf-8"))

    with path.open("rb") as f:
        tokens = tokenize.tokenize(f.readline)
        for tok in tokens:
            if tok.type in IGNORED_TOKENS:
                continue
            hasher.update(tok.string.encode("utf-8"))

    return base64.urlsafe_b64encode(hasher.digest()).decode("ascii").rstrip("=")

test_folder = Path('../city-files/')
tests = tuple(map(lambda f: test_folder/Path(f), [
    "AISearchfile012.txt",
    "AISearchfile017.txt",
    "AISearchfile021.txt",
    "AISearchfile026.txt",
    "AISearchfile042.txt",
    "AISearchfile048.txt",
    "AISearchfile058.txt",
    "AISearchfile175.txt",
    "AISearchfile180.txt",
    "AISearchfile535.txt",
]))
files = [
    "AlgAbasic",
    "AlgAenhanced",
    "AlgBbasic",
    "AlgBenhanced",
]
alg_folder = Path("algorithms")
filepaths = tuple(map(lambda f: alg_folder/Path(f), [
    file + '.py' for file in files
]))
hashes = tuple(map(hash_python_file, filepaths))
print('\n'.join(f'{str(file.name)+":":<17}{hash}' for file, hash in zip(filepaths, hashes)))

output_folder = Path('output')
if not output_folder.exists():
    output_folder.mkdir()

def copy(src: Path, dest: Path):
    dest.write_text(src.read_text())

for file, path, hash in zip(files, filepaths, hashes):
    folder = output_folder / Path(file)
    if not folder.exists():
        folder.mkdir()
        link = folder / Path('city-files')
        link.symlink_to(Path("city-files").absolute())
        link = folder / Path('alg_codes_and_tariffs.txt')
        link.symlink_to(Path("alg_codes_and_tariffs.txt").absolute())


    version_folder = folder / Path(hash)
    if version_folder.exists():
        print(f"No changes for {file}.py")
        continue
    print(f"Changes for {file}.py, running code")
    version_folder.mkdir()

    now = datetime.now() # current date and time
    date_time = now.strftime("%Y:%d:%m:%H:%M:%S")

    link = folder / Path(date_time)
    link.symlink_to(version_folder.absolute())

    script_copy = Path(version_folder/Path(file+'.py'))
    copy(path, script_copy)

    for testfile in tests:
        print(file, testfile.name)
        subprocess.run(["python3", str(script_copy.absolute()), testfile.name], cwd=version_folder)

