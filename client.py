import requests

def get_all_data():
    try:
        url = 'http://192.168.100.99:5000/data'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json().get('data')
            if data:
                print("All Cities:")
                print("ID | City")
                print("---------------")
                for item in data:
                    print(f"{item['id']:2} | {item['city']}")
            else:
                print("No data received from server.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server: {e}")

def get_data_by_id(city_id):
    try:
        url = f'http://192.168.100.99:5000/databyid/{city_id}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"City ID: {data['id']}, City Name: {data['city']}")
        elif response.status_code == 404:
            print("City not found.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server: {e}")

if __name__ == '__main__':
    print("Menu:")
    print("1. Get all data")
    print("2. Get data by ID")
    choice = input("Enter your choice: ")

    if choice == '1':
        get_all_data()
    elif choice == '2':
        city_id = input("Enter city ID: ")
        get_data_by_id(city_id)
    else:
        print("Invalid choice.")

