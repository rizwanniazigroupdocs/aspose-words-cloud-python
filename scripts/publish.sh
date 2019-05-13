git reset --hard
pip install --upgrade pip
python -m pip install --upgrade setuptools wheel
python setup.py sdist bdist_wheel
python -m pip install --upgrade twine
touch ~/.pypirc
echo [distutils] \\n index-servers= \\n\\t pypi \\n\\t pypitest\\n[pypi] \\n username: $1 \\n password: $2 \\n[pypitest]\\n repository: https://test.pypi.org/legacy/ \\n username: $1 \\n password: $2 > ~/.pypirc
python setup.py sdist
twine upload dist/* -r pypitest
chmod 777 -R aspose_words_cloud.egg-info
chmod 777 -R dist
chmod 777 -R build