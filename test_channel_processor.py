import pytest
from channel_processor import channel_processor as CP

cp = CP(channels_dir="test_files/", parameters_dir="test_files/")

def test_having_initial_channel_processor_with_test_params():
    assert cp.X == [1, 2]
    assert cp.m == 3.0
    assert cp.c == 4.0

def test_func1():
    cp.func1()
    assert cp.Y == [7.0, 10.0]

def test_func3():
    cp.func3()
    assert cp.A == [1.0, 0.5]

def test_func2():
    cp.func2()
    assert cp.B == [8.0, 10.5]
    assert cp.b == (8.0 + 10.5) / 2 #test b = mean(B) = 9.25

def test_func4():
    cp.func4()
    assert cp.C == [1 + 9.25, 2 + 9.25]




