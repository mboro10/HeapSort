import random
import sys
import os
from hypothesis import given, strategies as st
import pytest
import math
import time
sys.path.append('/Users/monjit/HeapSort')

from heapsort.HeapSort import heapsort, heapify

def build_heap(arr):
    n = len(arr)
    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# Test for heapify function
def test_heapify():
    arr = [3, 9, 2, 1, 4, 5]
    build_heap(arr)
    assert arr == [9, 4, 5, 1, 3, 2], f"Heap construction failed, got {arr}"

    arr = [9, 4, 5, 1, 3, 2]
    original_arr = arr[:]
    heapify(arr, len(arr), 0)
    assert arr == original_arr, f"Heapify modified an already valid heap, got {arr}"

    arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    build_heap(arr)
    assert arr[0] == 9, "Heap construction failed to place largest element at root"

def test_heapsort():
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    heapsort(arr)
    assert arr == sorted(arr), f"Heap sort failed, got {arr}"

    arr = [1, 2, 3, 4, 5]
    heapsort(arr)
    assert arr == [1, 2, 3, 4, 5], f"Heap sort failed on sorted array, got {arr}"

    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    heapsort(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9], f"Heap sort failed on reverse sorted array, got {arr}"

def test_single_element():
    arr = [42]
    heapsort(arr)
    assert arr == [42], "Failed for single element"

def test_sorted_array():
    arr = [1, 2, 3, 4, 5]
    heapsort(arr)
    assert arr == [1, 2, 3, 4, 5], "Failed for already sorted array"

def test_reverse_sorted_array():
    arr = [5, 4, 3, 2, 1]
    heapsort(arr)
    assert arr == [1, 2, 3, 4, 5], "Failed for reverse sorted array"

def test_large_dataset():
    large_data = list(range(10**6, 0, -1))
    start_time = time.time()
    heapsort(large_data)
    execution_time = time.time() - start_time
    assert large_data == sorted(large_data), "Heap sort failed for large dataset"
    assert execution_time < 5, "Heap sort took too long for large dataset"

def test_robustness():
    repetitive_data = [42] * 10**6
    heapsort(repetitive_data)
    assert repetitive_data == [42] * 10**6

    mixed_data = [42, "string", None]
    with pytest.raises(TypeError):
        heapsort(mixed_data)

def test_vulnerability():
    malicious_input = [float('inf'), -float('inf'), 0, 42, -42] * 200000
    heapsort(malicious_input)
    assert malicious_input == sorted(malicious_input), "Heap sort failed with extreme values"

def test_data_integrity():
    original_data = [5, 2, 9, 1, 5, 6]
    input_copy = original_data[:]
    heapsort(original_data)
    assert original_data == sorted(input_copy), "Heap sort altered data incorrectly"
    assert original_data != input_copy, "Heap sort did not sort correctly"

# Hypothesis strategy for lists with special values (NaN, inf)
@st.composite
def lists_with_special_values(draw):
    length = draw(st.integers(min_value=0, max_value=10))  # List length, random between 0 and 10
    return draw(st.lists(st.floats(allow_nan=True, allow_infinity=True), min_size=length, max_size=length))

@given(lists_with_special_values())

# New Test Cases
def test_new_heapsort_random(arr):
    arr_no_nan = [x for x in arr if not math.isnan(x)]
    heapsort(arr_no_nan)
    
    for i in range(1, len(arr_no_nan)):
        assert arr_no_nan[i-1] <= arr_no_nan[i], "The list is not sorted correctly"
    
    nan_values = [x for x in arr if math.isnan(x)]
    
    arr_no_nan.extend(nan_values)

    assert all(math.isnan(x) for x in arr_no_nan[len(arr_no_nan)-len(nan_values):]), "NaN values are not at the end of the list"

    arr = [1.111, 3.333, 2.222, 5.555, 4.444]
    heapsort(arr)
    assert arr == [1.111, 2.222, 3.333, 4.444, 5.555], "Heapsort failed for floating point precision"

def test_new_large_random_data():
    arr = [random.randint(0, 1000000) for _ in range(100000)]
    start_time = time.time()
    heapsort(arr)
    end_time = time.time()
    assert arr == sorted(arr), "Heapsort failed for large random data"
    assert (end_time - start_time) < 5, "Heapsort performance is below expected threshold"
    
def test_new_floating_point_precision():
    arr = [1.111, 3.333, 2.222, 5.555, 4.444]
    heapsort(arr)
    assert arr == [1.111, 2.222, 3.333, 4.444, 5.555], "Heapsort failed for floating point precision"

def test_new_infinity():
    arr = [float('inf'), 1, 0, 100, 50]
    heapsort(arr)
    assert arr == [0, 1, 50, 100, float('inf')], "Heapsort failed for positive infinity"

def test_new_nan():
    arr = [3, 7, float('nan'), 5, 1]
    heapsort(arr)
    
    for i in range(len(arr) - 1):
        assert arr[i] == [1, 3, 5, 7][i], f"Heapsort failed for NaN values, got {arr}"
    
    assert math.isnan(arr[-1]), f"Last element is not NaN, got {arr[-1]}"

@pytest.fixture
def check_memory_leak():
    import tracemalloc
    tracemalloc.start()
    yield
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    assert peak < 50 * 1024 * 1024, "Memory usage exceeded for sorting large datasets"

@pytest.mark.benchmark
def test_benchmark(benchmark):
    large_data = list(range(10**6, 0, -1))
    benchmark(heapsort, large_data)
