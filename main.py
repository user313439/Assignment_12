from typing import List

def path_to_file_list(path: str) -> List[str]:
    with open(path, 'r') as f:
        return f.read().split('\n')


def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        if '\\' in file:
            file = file.replace('\\', '\\')
        if '/' or '"' in file:
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file

    # Template for json file
    template_start = '{\"German\":\"'
    template_mid = '\",\"German\":\"'
    template_end = '\"}'

    # Can this be working?
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        english_file = process_file(german_file)

        processed_file_list.append(template_mid + english_file + template_start + german_file + template_start)
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'r') as f:
        for file in file_list:
            f.write('\n')
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = train_file_list_to_json(german_path)

    processed_file_list = path_to_file_list(english_file_list, german_file_list)

    write_file_list(processed_file_list, path+'concated.json')
