def constant_sliding_window(sequence, window_size):
    """
    This function takes a sequence and a window size as input and returns a list of tuples,
    each containing the start and end indices of the sliding window.

    :param sequence: The input sequence (list, string, etc.)
    :param window_size: The size of the sliding window
    :return: A list of tuples containing the start and end indices of the sliding window
    """
    return [(i, i + window_size) for i in range(len(sequence) - window_size + 1)]