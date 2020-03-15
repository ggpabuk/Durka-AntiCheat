from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('main.py', base=base)
]

setup(name='Durka Anti - Cheat',
      version = '2.2',
      description = 'Cheat detection on client',
      options = dict(build_exe = buildOptions),
      executables = executables)
