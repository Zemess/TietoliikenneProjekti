import mysql.connector
import asyncio
from bleak import BleakClient

# Tätä ei päästy täysin testailee että toimiiko kun pysähty tuohon connectaamis vaiheeseen.
# Elikkä ongelma oli todennäköisesti inserSensorData():n sisällä.

# Database configuration
db_config = {
    "host": "172.20.241.36",
    "user": "dbaccess_rw",
    "password": "Fasdjf23809w2c8343v4k29",
    "database": "measurements"
}

# BLE device info
DEVICE_ADDRESS = "C8:FS:2E:D2:51:31"
SERVICE_UUID = "00001323-1212-efde-1523-785feabcd123"
CHARACTERISTICS_UUID = "00001526-1212-efde-1523-785feabcd123"

def insertSensorData(direction, x, y, z):
    """Insert sensor data into the MySQL database."""
    print("Yhdistän tietokantaan...")
    connection = None
    try:
        print("Yhteyden luonti...")
        connection = mysql.connector.connect(**db_config)
        print("Yhteys luotu!")
        cursor = connection.cursor()
        print("Kursorin luonti...")
        query = "INSERT INTO sensorData (direction, x, y, z) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (direction, x, y, z))
        connection.commit()
        print("Data inserted:", direction, x, y, z)

    except mysql.connector.Error as err:
        print(f"Database error: {err}")

    finally:
        if connection:
            connection.close()

def decodePackedData(packed_data):
    """Decode the packed sensor data."""
    print("Tiedostoa dekoodataan...")
    x = ((packed_data >> 20) & 0x03FF) / 1000.0
    y = ((packed_data >> 10) & 0x03FF) / 1000.0
    z = (packed_data & 0x03FF) / 1000.0
    direction = ((packed_data >> 30) & 0x07)
    print("Dekoodattu:", direction, x, y, z)
    return direction, x, y, z

async def handle_ble_data(client):
    """Handle BLE data reading."""
    print("Yhdistin BLE-laitteeseen...")
    while True:
        # Read data
        data = await client.read_gatt_char(CHARACTERISTICS_UUID)
        if data:
            packed_data = int.from_bytes(data, byteorder="little")
            print(f"Paketista saatu data: 0x{packed_data:08X}")
            direction, x, y, z = decodePackedData(packed_data)
            print(f"Dekoodattu arvo: Direction={direction}, x={x}, y={y}, z={z}")
            await asyncio.to_thread(insertSensorData, direction, x, y, z)

async def main():
    """Connect to BLE device and start reading data."""
    try:
        async with BleakClient(DEVICE_ADDRESS) as client:
            print("Connected to BLE device.")
            await handle_ble_data(client)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
