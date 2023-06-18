from flask import Flask, render_template, request
import datetime
<<<<<<< HEAD
import csv
=======
>>>>>>> b0b574bab6676947b907ae22474e548cc0b728ec

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
<<<<<<< HEAD
        self.booking_details_file = 'booking_details.csv'
    
=======

>>>>>>> b0b574bab6676947b907ae22474e548cc0b728ec
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
<<<<<<< HEAD
                with open(self.booking_details_file, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([booking_id, slot_id, name, vehicle_number, date, entry_time, exit_time])

=======
>>>>>>> b0b574bab6676947b907ae22474e548cc0b728ec
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
<<<<<<< HEAD
            with open(self.booking_details_file, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                rows = list(reader)

            with open(self.booking_details_file, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for row in rows:
                    if row[0] != booking_id:
                        writer.writerow(row)

        
=======
>>>>>>> b0b574bab6676947b907ae22474e548cc0b728ec
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

<<<<<<< HEAD

def view_booked_slots():
    booking_details = []
    
    with open('booking_details.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
            
        for row in reader:
            booking_id, slot_id, name, vehicle_number, date, entry_time, exit_time = row
            booking_details.append({
                'BookingID': booking_id,
                'Name': name,
                'VehicleNumber': vehicle_number,
                'Date': date,
                'EntryTime': entry_time,
                'ExitTime': exit_time
            })
        
    return booking_details

=======
>>>>>>> b0b574bab6676947b907ae22474e548cc0b728ec
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

<<<<<<< HEAD
@app.route('/slot', methods=['GET', 'POST'])
def slot():
    if request.method == 'POST':
        key = "@dminonly@cce$$"
        password = request.form['admin_pass']
        if password == key:
            booking_details = view_booked_slots()
            return render_template('slots.html', booking_details=booking_details)
        else:
            return render_template('error.html')
    return render_template('slotlist.html')

=======
>>>>>>> b0b574bab6676947b907ae22474e548cc0b728ec
if __name__ == '__main__':
    app.run(debug=True, port=8000)

