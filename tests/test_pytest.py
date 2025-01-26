import sys
import os
import pytest
import time
sys.path.append('/Users/monjit/HeapSort')

from heapsort.HeapSort import heapsort, heapify

# Test for heapify function: should turn an array into a valid max-heap
def test_heapify():
    arr = [3, 9, 2, 1, 4, 5]
    heapify(arr, len(arr), 0)  # Start heapify at root (index 0)
    # After heapifying, the largest element should be at the root (index 0)
    assert arr == [9, 4, 5, 1, 3, 2], f"Heapify failed, got {arr}"

    # Test an already valid max-heap
    arr = [9, 4, 5, 1, 3, 2]
    original_arr = arr[:]  # Make a copy to check for modifications
    heapify(arr, len(arr), 0)
    assert arr == original_arr, f"Heapify modified an already valid heap, got {arr}"

    # Test on an array that needs heapifying (unsorted)
    arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    heapify(arr, len(arr), 0)
    # After heapifying, the array should be a valid max-heap
    assert arr[0] == 9, "Heapify failed to place largest element at root"

# Test for heapsort function: ensures it uses heapify correctly to sort the array
def test_heapsort():
    # Test sorting of an unsorted array
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    heapsort(arr)
    assert arr == sorted(arr), f"Heap sort failed, got {arr}"

    # Test sorting of an already sorted array
    arr = [1, 2, 3, 4, 5]
    heapsort(arr)
    assert arr == [1, 2, 3, 4, 5], f"Heap sort failed on sorted array, got {arr}"

    # Test sorting of a reverse sorted array
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    heapsort(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9], f"Heap sort failed on reverse sorted array, got {arr}"

# Test for basic cases (single element, sorted, reverse sorted)
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

# Test for large datasets
def test_large_dataset():
    large_data = list(range(10**6, 0, -1))  # A large array in reverse order
    start_time = time.time()
    heapsort(large_data)
    execution_time = time.time() - start_time
    assert large_data == sorted(large_data), "Heap sort failed for large dataset"
    assert execution_time < 5, "Heap sort took too long for large dataset"

# Test for robustness with edge cases
def test_robustness():
    # Test with repetitive elements
    repetitive_data = [42] * 10**6
    heapsort(repetitive_data)
    assert repetitive_data == [42] * 10**6

    # Test with mixed data types (should raise a TypeError)
    mixed_data = [42, "string", None]
    with pytest.raises(TypeError):
        heapsort(mixed_data)

# Test for vulnerabilities
def test_vulnerability():
    malicious_input = [float('inf'), -float('inf'), 0, 42, -42] * 200000
    heapsort(malicious_input)
    assert malicious_input == sorted(malicious_input), "Heap sort failed with extreme values"

# Security check for data modification
def test_data_integrity():
    original_data = [5, 2, 9, 1, 5, 6]
    input_copy = original_data[:]
    heapsort(original_data)
    assert original_data == sorted(input_copy), "Heap sort altered data incorrectly"
    assert original_data != input_copy, "Heap sort did not sort correctly"

# Mocking memory usage and detecting data leaks
@pytest.fixture
def check_memory_leak():
    import tracemalloc
    tracemalloc.start()
    yield
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    assert peak < 50 * 1024 * 1024, "Memory usage exceeded for sorting large datasets"

# Benchmarking with pytest-benchmark plugin
@pytest.mark.benchmark
def test_benchmark(benchmark):
    large_data = list(range(10**6, 0, -1))
    benchmark(heapsort, large_data)
