from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

class ParkingSlot:
    def __init__(self, slot_id, available=True):
        self.slot_id = slot_id
        self.available = available
        self.booking_id = None
        self.booking_details = {}

class ParkingLot:
    def __init__(self, num_slots):
        self.slots = [ParkingSlot(slot_id) for slot_id in range(1, num_slots + 1)]

    def display_available_slots(self):
        return [slot.slot_id for slot in self.slots if slot.available]

    def book_slot(self, slot_id, booking_id, name, vehicle_number, date, entry_time, exit_time):
        slot = self.get_slot_by_id(slot_id)
        if slot:
            if slot.available:
                slot.available = False
                slot.booking_id = booking_id
                slot.booking_details = {
                    'Name': name,
                    'Vehicle Number': vehicle_number,
                    'Date': date,
                    'Entry Time': entry_time,
                    'Exit Time': exit_time
                }
                return True
            else:
                return False
        else:
            return False

    def cancel_booking(self, booking_id):
        slot = self.get_slot_by_booking_id(booking_id)
        if slot:
            slot.available = True
            slot.booking_id = None
            slot.booking_details = {}
            return True
        else:
            return False

    def get_slot_by_id(self, slot_id):
        for slot in self.slots:
            if slot.slot_id == slot_id:
                return slot
        return None

    def get_slot_by_booking_id(self, booking_id):
        for slot in self.slots:
            if slot.booking_id == booking_id:
                return slot
        return None

parking_lot = ParkingLot(10)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        slot_id = int(request.form['slot_id'])
        name = request.form['name']
        vehicle_number = request.form['vehicle_number']
        date = request.form['date']
        entry_time = request.form['entry_time']
        exit_time = request.form['exit_time']

        # Generate a booking ID
        booking_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        # Book a slot
        booking_successful = parking_lot.book_slot(slot_id, booking_id, name, vehicle_number, date, entry_time, exit_time)

        if booking_successful:
            return render_template('booked.html', slot_id=slot_id, booking_id=booking_id)
        else:
            return render_template('book.html', available_slots=parking_lot.display_available_slots(), error_message="Slot not available")
    else:
        return render_template('book.html', available_slots=parking_lot.display_available_slots(), error_message=None)

@app.route('/cancel', methods=['GET', 'POST'])
def cancel():
    if request.method == 'POST':
        booking_id = request.form['booking_id']
        cancellation_successful = parking_lot.cancel_booking(booking_id)

        if cancellation_successful:
            return render_template('cancel.html', booking_id=booking_id, cancellation_message="Booking canceled successfully")
        else:
            return render_template('cancel.html', booking_id=None, cancellation_message=None, error_message="Invalid booking ID")
    else:
        return render_template('cancel.html', booking_id=None, cancellation_message=None, error_message=None)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

