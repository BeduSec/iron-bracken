class NoiseFilter:
    @staticmethod
    def filter_traffic(packets, threshold=100):
        return [p for p in packets if len(p) < threshold]
