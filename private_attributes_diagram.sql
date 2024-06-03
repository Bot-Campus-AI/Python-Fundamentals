+------------------+
|      Car         |
+------------------+
| - _make          |
| - _model         |
| - _year          |
+------------------+
| + __init__()     |
| + get_year()     |
| + set_year()     |
| + show_details() |
+------------------+

Object: my_car
Access: my_car._make         (not recommended)
        my_car._model        (not recommended)
        my_car._year         (not recommended)
        my_car.get_year()    (recommended)
        my_car.set_year()    (recommended)
