python -m pip install --upgrade setuptools wheel
python setup.py sdist bdist_wheel
python -m pip install --upgrade twine
touch ~/.pypirc
echo [distutils] \\n index-servers= \\n\\t pypi \\n\\t pypitest\\n [pypi] \\n username = $1 \\n password = $2 \\n [pypitest]\\n repository = https://test.pypi.org/legacy/ \\n username = $1 \\n password = $2 > ~/.pypirc
python setup.py sdist && twine upload dist/* -r pypitest