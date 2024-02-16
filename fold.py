import sys
from pathlib import Path


def fold(base_path: Path, output_file):
    files = [p for p in base_path.rglob('*') if p.is_file()]
    result = []

    with open(output_file, 'w+') as out:
        print(f'@@@@@ fold {len(files)} files', file=out)

        for file in files:
            rp = file.relative_to(base_path)

            line_count = 0

            try:
                with open(file, 'r') as f:
                    for line in f:
                        line_count += 1
            except UnicodeDecodeError:
                # Fond non-text data
                print(f'skip binary file {file}')
                continue

            print(f'@@@@@ {line_count} {rp}', file=out)

            with open(file, 'r') as g:
                # Add a trailing newline, in case there is no newline in file end
                print(g.read(), file=out)

            result.append(file)

        print('@@@@@ end', file=out)

    return result


if __name__ == '__main__':
    path = Path(sys.argv[1])
    filename = path.absolute().name + '.fold'
    files = fold(path, filename)
    print(f'Fold {len(files)} files to {filename}')
