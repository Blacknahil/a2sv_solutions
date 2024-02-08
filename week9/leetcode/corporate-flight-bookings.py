class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr=[0]*(n)
        for first,last,seats in bookings:
            arr[first-1]+=seats
            if last<n:
                arr[last]-=seats
        return accumulate(arr)

        