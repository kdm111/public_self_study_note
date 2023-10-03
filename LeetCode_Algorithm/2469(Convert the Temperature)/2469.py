class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        # sol1 32ms 57.68% 13.8MB 38%
        return [celsius + 273.15, celsius * 1.8 + 32]