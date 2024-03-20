from queue import Queue
def register_patients(queue):
    name = input("Enter patient name: ")
    queue.put(name)
    print("patient", name, "registered.")

def remove_patient(queue):
    if queue.empty():
        print("No patients in the queue.")
    else:
        name = queue.get()
        print("patient",name, "removed after meeting the doctor.")
def display_queue(queue):
    if queue.empty():
        print("patient Queue:", list(queue.queue))
def main():
    patient_queue = Queue()
    while True:
        print("\nDesk Manager Patient Registration and appointment system")
        print("1. Register patient")
        print("2.Remove patient after meeting Doctor")
        print("3. Display patient Queue")
        print("4.Exit")

        choice = input("Enter your choice (just enter the option number): ")
        if choice == '1':
          register_patients(patient_queue) 
        elif choice == '2':
            remove_patient(patient_queue)
        elif choice == '3':
            display_queue(patient_queue)
        elif choice == '4':
            print("Existing the program.")  
            break
        else:
            print("Invalid choice.please enter a valid option number. ")


print(main())