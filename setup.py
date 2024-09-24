import cx_Freeze

executables = [cx_Freeze.Executable("programa_final.py", base="Win32GUI")]

cx_Freeze.setup(
    name="Nota Fiscal",
    version="1.0",
    description="Nota Fiscal",
    executables=executables
)