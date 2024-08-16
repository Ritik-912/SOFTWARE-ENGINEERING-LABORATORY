# Unit Testing with Pytest

### Write and execute unit tests for python functions using pytest framework, covering diferent test cases and assertions

1. First created the folder for project that has 2 subdirectories `src` and `test`.

2. Inside `src` folder created `source_code.py` that contaions the functions that are to be tested.

3. Inside `test` folder created `test_code.py` (it is recommended that naming of test file should be `test_` followed by the filename which is to be tested) written functions and testing codes inside the files.

4. Created an virtual python environment activated it and install `pytest` library.

5. The output of below is stored in `install.out`

```python
pip install -U pytest > install.out
```
6. Then run the following command in `test` subdirectory and got the following result.
```python
pytest test_code.py
```

![Output Image of successfull pytest completion.](output.png)
