# write_app {#sec-write_app}

`write_app(board, pin_name: str, version: str = None, file: str = 'app.py', overwrite=False)`

Write VetiverAPI app to a file

## Parameters

| Name       | Type   | Description                         | Default    |
|------------|--------|-------------------------------------|------------|
| `board`    |        | API to be written                   | required   |
| `pin_name` | string | Name of pin containing VetiverModel | required   |
| `version`  | str    | Pins version of VetiverModel        | `None`     |
| `file`     | str    | Name of file                        | `'app.py'` |

Example
-------
>>> import vetiver
>>> import tempfile
>>> import pins
>>> tmp = tempfile.TemporaryDirectory()
>>> board = pins.board_temp(allow_pickle_read=True)
>>> X, y = vetiver.get_mock_data()
>>> model = vetiver.get_mock_model().fit(X, y)
>>> v = vetiver.VetiverModel(model = model, model_name = "my_model", ptype_data = X)
>>> vetiver.vetiver_pin_write(board, v)
>>> vetiver.write_app(board,
...     "my_model",
...     file = tmp.name + "/app.py")