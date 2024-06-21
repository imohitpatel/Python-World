class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient_id, name, age, gender, condition):
        patient = {
            'patient_id': patient_id,
            'name': name,
            'age': age,
            'gender': gender,
            'condition': condition
        }
        self.patients.append(patient)
        print(f"Patient {name} added successfully.")

    def add_doctor(self, doctor_id, name, specialty):
        doctor = {
            'doctor_id': doctor_id,
            'name': name,
            'specialty': specialty
        }
        self.doctors.append(doctor)
        print(f"Doctor {name} added successfully.")

    def add_appointment(self, appointment_id, patient_id, doctor_id, date, time):
        appointment = {
            'appointment_id': appointment_id,
            'patient_id': patient_id,
            'doctor_id': doctor_id,
            'date': date,
            'time': time
        }
        self.appointments.append(appointment)
        print(f"Appointment {appointment_id} added successfully.")

    def view_patients(self):
        for patient in self.patients:
            print(f"ID: {patient['patient_id']}, Name: {patient['name']}, Age: {patient['age']}, Gender: {patient['gender']}, Condition: {patient['condition']}")

    def view_doctors(self):
        for doctor in self.doctors:
            print(f"ID: {doctor['doctor_id']}, Name: {doctor['name']}, Specialty: {doctor['specialty']}")

    def view_appointments(self):
        for appointment in self.appointments:
            patient = next((p for p in self.patients if p['patient_id'] == appointment['patient_id']), None)
            doctor = next((d for d in self.doctors if d['doctor_id'] == appointment['doctor_id']), None)
            print(f"Appointment ID: {appointment['appointment_id']}, Patient: {patient['name'] if patient else 'Unknown'}, Doctor: {doctor['name'] if doctor else 'Unknown'}, Date: {appointment['date']}, Time: {appointment['time']}")

def main():
    hms = HospitalManagementSystem()
    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Add Appointment")
        print("4. View Patients")
        print("5. View Doctors")
        print("6. View Appointments")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            patient_id = input("Enter patient ID: ")
            name = input("Enter patient name: ")
            age = input("Enter patient age: ")
            gender = input("Enter patient gender: ")
            condition = input("Enter patient condition: ")
            hms.add_patient(patient_id, name, age, gender, condition)
        elif choice == '2':
            doctor_id = input("Enter doctor ID: ")
            name = input("Enter doctor name: ")
            specialty = input("Enter doctor specialty: ")
            hms.add_doctor(doctor_id, name, specialty)
        elif choice == '3':
            appointment_id = input("Enter appointment ID: ")
            patient_id = input("Enter patient ID: ")
            doctor_id = input("Enter doctor ID: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            hms.add_appointment(appointment_id, patient_id, doctor_id, date, time)
        elif choice == '4':
            hms.view_patients()
        elif choice == '5':
            hms.view_doctors()
        elif choice == '6':
            hms.view_appointments()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
