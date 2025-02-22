class SnapshotArray:

    def __init__(self, length: int):
        self.data = [{} for _ in range(length)]  # Dictionary per index to store snapshots
        self.snap_id = 0  # Tracks snapshot ID

    def set(self, index: int, val: int) -> None:
        self.data[index][self.snap_id] = val  # Store value at the latest snap ID

    def snap(self) -> int:
        self.snap_id += 1  # Increment snap ID
        return self.snap_id - 1  # Return previous snap ID

    def get(self, index: int, snap_id: int) -> int:
        # If exact snap_id exists, return value
        if snap_id in self.data[index]:
            return self.data[index][snap_id]
        # Otherwise, find the closest previous snap using binary search
        keys = sorted(self.data[index].keys())  # Get all available snapshots
        for i in reversed(keys):
            if i <= snap_id:
                return self.data[index][i]  # Return the closest valid snapshot
        return 0  # Default value if no snapshots exist


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index, val)
# param_2 = obj.snap()
# param_3 = obj.get(index, snap_id)
