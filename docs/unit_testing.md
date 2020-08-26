#### ecosystem
- `unittest` is included in pyhton standard distribution and based on junit
- `pytest` is a library with nice syntactic sugar and the preffered way (https://docs.pytest.org/en/stable/contents.html)

#### cheatsheet
- skip test `@pytest.mark.skip("WIP")`
- parametrize test `@pytest.mark.parametrize`
- setup & teardown 
```python
@pytest.fixture
def resource():
    a = Resource()
    yield a
    a.close()
```
- doctest meh
```
def large_straight(dice):
    """Score the given roll in the 'Large Straight' Yatzy category.

    >>> large_straight([2,3,4,5,6])
    20
    >>> large_straight([1,2,3,4,5])
    0

    """
```
- mocking with DI
```python
from unittest.mock import Mock
def test_normal_pressure_alarm_stays_off():
    stub_sensor = Mock(Sensor)
    stub_sensor.sample_pressure.return_value = 18
    alarm = Alarm(stub_sensor)
    alarm.check()
    assert not alarm.is_alarm_on
```
- monkey patching without DI 
```python
from unittest.mock import patch
def test_alarm_with_high_pressure_value():
    with patch('alarm.Sensor') as test_sensor_class:
        test_sensor_instance = Mock()
        test_sensor_instance.sample_pressure.return_value = 22
        test_sensor_class.return_value = test_sensor_instance
        alarm = Alarm()
        alarm.check()
        assert alarm.is_alarm_on
```





