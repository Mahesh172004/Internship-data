class movieTheater:
    def __init__(self, movie_name, total_seats):
        self.movie_name = movie_name
        self.total_seats = ["A" + str(i+1) for i in range(total_seats)]
        self.booked_seats = []

    def __iter__(self):
        return SeatIterator(self)

class SeatIterator:
    def __init__(self, theater):
        self.theater = theater
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.theater.total_seats):
            seat = self.theater.total_seats[self.index]
            self.index += 1
            if seat not in self.theater.booked_seats:
                return seat
        raise StopIteration
    
movie = movieTheater("Avengers: Endgame", 5)
print(f"Welcome to {movie.movie_name} booking system!")
iterator= iter(movie)
try:
    while True:
        seat = next(iterator)
        print(f"Available seat: {seat}")
        book = input(f"Do you want to book seat {seat}? (yes/no): ").lower()

        if book == 'yes':

            movie.booked_seats.append(seat)
            print(f"Seat {seat} booked successfully!")
        else:
            print(f"skipped seat {seat}")

except StopIteration:
    print("No more seats available.")

print("Booking process completed. Thank you!")
