
_original_file_lines = []
_modified_file_lines = []

_method_for_automatic_code = "apply_knowledge"

def was_any_code_modified():
    global _original_file_lines
    global _modified_file_lines
    return _original_file_lines == _modified_file_lines


def add_code_line_at_start(code):
    global _modified_file_lines

    for k, line in enumerate(_modified_file_lines):
        if line.startswith("def " + _method_for_automatic_code):
            _modified_file_lines.insert(k+1, "    " + code + "\n")


def set_content(lines):
    global _original_file_lines
    global _modified_file_lines

    _original_file_lines = lines
    _modified_file_lines = _original_file_lines


def get_content():
    global _modified_file_lines

    return _modified_file_lines