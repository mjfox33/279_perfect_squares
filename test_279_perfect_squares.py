from code_279_perfect_squares import Solution

def test_example_1():
    s = Solution()
    n = 12
    output = 3
    assert s.numSquares_dp(n) == output

def test_example_2():
    s = Solution()
    n = 13
    output = 2
    assert s.numSquares_dp(n) == output