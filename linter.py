from cuda_lint import Linter, util

class JSONNetLint(Linter):
    syntax = 'Jsonnet'
    name = 'jsonnet-lint'
    cmd = 'jsonnet-lint'
    tempfile_suffix = '.jsonnet'
    regex = r'(?P<filename>.*):(?P<line>[1-9][0-9]*):(?P<col>[1-9][0-9]*)-(?P<end_col>[1-9][0-9]*) (?P<message>.*)'
    error_stream = util.STREAM_STDERR
    multiline = False
