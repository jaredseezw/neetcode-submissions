class TimeMap:

    def __init__(self):
        self.hashtable = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashtable:
            self.hashtable[key] = [(timestamp, value)]
        else:
            self.hashtable[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashtable:
            return ""
        else:
            array = self.hashtable[key]
            low = 0 
            high = len(array) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if array[mid][0] == timestamp:
                    return array[mid][1]
                elif array[mid][0] < timestamp:
                    low = mid + 1
                else:
                    high = mid - 1
            return array[high][1] if high >= 0 else ""

