import streamlit as st
import sqlite3
import pandas as pd
import qrcode
from io import BytesIO
import numpy as np
from pyzbar.pyzbar import decode
import os
import cv2
from streamlit_option_menu import option_menu


# Set page configuration
st.set_page_config(page_title="Smart Surveillance System",page_icon="🛡️", layout="wide")
st.subheader("Inventory Management System - Visual Computing")


# Function to display the homepage
def home_page():
    st.title("VISUAL SYNDICATE PRESENTS YOU ")
    st.write("a smart surveillance system , explore our diverse website designed to meet customers needs . Our system uses advanced technology to help you monitor and protect your space . From real time CCTV footage and smart image processing ,facial recognition , we provide everything you need for reliable security . Our tailored solutions empower businesses to monitor their premises seamlessly while optimising inventory control . Explore our range of high-definition cameras and intuitive inventory tracking system designed to enhance security , streamline operations and maximise productivity .Trust our system to protect your assets and elevate your business operations to new heights")

    st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: red !important;
        color: white !important;
    }
    div.stButton > button {
        margin: 0 auto;
        display: block;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(r"files/boxes.png")
    with col2:
        st.markdown("---")
        st.button("Smart CCTV Surveillance", key='smart_cctv_surveillance_page')
        st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("---")
        st.button("QR Code Integration", key='qr_scanning')
        st.markdown("---")
        st.write("")
    with col2:
        st.image(r"files/bar code scanning.jpg")
    col1, col2 = st.columns(2)
    with col1:
        st.image(r"files/shelf monitoring.png")
    with col2:
        st.markdown("---")
        st.button("Shelf Monitoring", key='self_monitoring_page')
        st.markdown("---")
        st.write("")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("---")
        st.button("Facial Recognition", key='facial_recognition')
        st.markdown("---")
        st.write("")
    with col2:
        st.image(r"files/facial_monitoring.jpg")

# Function to display the Smart CCTV Surveillance page
def smart_cctv_surveillance_page():
    st.title("Smart CCTV Surveillance")
    st.write("Experience unparalleled efficiency and security with our smart CCTV surveillance solutions for warehouse inventory  management. Our advanced systems utilize AI-powered cameras strategically placed at entry and exit points to monitor the movement of boxes in real-time, in 2 dimension l as well as 3 dimension, From tracking inbound shipments to ensuring accurate outbound deliveries, our technology provides detailed insights and alerts for proactive management. Trust us to enhance operational visibility, optimize inventory control, and safeguard your assets with cutting-edge surveillance solutions tailored for warehouses.")
    st.subheader("Top-view of the Coveyor Belt, 2D Boxes")
    col1, col2 = st.columns(2)
    with col1:
        st.video(r"files/conveyorbelt_1.mp4")  
        st.write("Original Clip")    
    with col2:
        st.video(r"files/conveyor1.mp4")
        st.write("Processed Clip")
    st.subheader("Front-view of the Coveyor Belt, 3D Boxes")
    col1, col2 = st.columns(2)
    with col1:
        st.video(r"files/convoybelt_3D.mp4")  
        st.write("Original Clip")    
    with col2:
        st.video(r"files/conveyor2.mp4")
        st.write("Processed Clip")

def self_monitoring_page():
    st.title("Shelf Monitoring")
    st.write("Elevate warehouse efficiency and customer experience with our comprehensive monitoring solutions. Our advanced shelf monitoring technology ensures accurate inventory levels and optimal stock replenishment, minimizing stockouts and maximizing operational efficiency. Simultaneously, our trolley monitoring system provides real-time insights into customer behavior and preferences, allowing for personalized service and improved navigation within the warehouse. Trust us to transform your warehouse into a seamless operation that enhances both internal operations and customer satisfaction.")
    st.header("Shelf-front view, counting of items")
    col1, col2 = st.columns(2)
    with col1:
        st.video(r"files/original_bottles.mp4")
    with col2:
        st.video(r"files/counting_2.mp4")
    st.write("Optimize inventory accuracy and streamline operations with our shelf monitoring system equipped for precise counting and detection of miscounted objects in warehouses. Utilizing advanced  AI-powered technology, our system ensures real-time visibility of stock levels on shelves. By automatically detecting discrepancies and miscounts, we enhance inventory management efficiency and minimize errors. Trust our solution to provide reliable data insights that empower informed decision-making and improve overall warehouse productivity.")
    st.header("Cart view of the customer")
    col1, col2 = st.columns(2)
    with col1:
        st.video(r"files/original_basket.mp4")
    with col2:
        st.video(r"files/cart1.mp4")
    st.write("Enhance warehouse efficiency with our advanced shelf monitoring system that includes real-time counting of items in trolleys. Using  AI-driven technology, our system accurately tracks items as they are placed into trolleys during picking operations. This capability not only ensures precise inventory management but also facilitates streamlined order fulfillment processes. By providing instant updates on inventory levels and locations within trolleys, our solution empowers warehouses to optimize resource allocation and minimize stock discrepancies. Experience heightened productivity and accuracy with our tailored shelf monitoring solution designed to meet the dynamic demands of modern warehouse environments.")  
    st.header("items on and off shelf")
    col1, col2 = st.columns(2)
    with col1:
        st.video(r"files/original_self1.mp4")
    with col2:
        st.video(r"files/self.mp4")
    st.write("Enhance warehouse efficiency with our advanced shelf monitoring system that includes real-time counting of items in trolleys. Using  AI-driven technology, our system accurately tracks items as they are placed into trolleys during picking operations. This capability not only ensures precise inventory management but also facilitates streamlined order fulfillment processes. By providing instant updates on inventory levels and locations within trolleys, our solution empowers warehouses to optimize resource allocation and minimize stock discrepancies. Experience heightened productivity and accuracy with our tailored shelf monitoring solution designed to meet the dynamic demands of modern warehouse environments.")


def qr_scanning():
    st.title("QR-Code Scanning")
    st.write("Streamline warehouse operations with our versatile QR code scanning system designed for efficiency and accuracy. Our advanced technology supports simultaneous scanning across multiple scanners and boxes, ensuring seamless tracking and management of inventory at every stage. Whether you're receiving shipments, conducting internal transfers, or preparing orders for dispatch, our system provides real-time updates and inventory visibility. Experience enhanced productivity and reliability with our tailored QR code scanning solutions, tailored to meet the dynamic demands of modern warehouse environments.")

    st.header("Cardboard boxes 1")
    col1, col2 = st.columns(2)

    with col1:
        st.image(r"files/qr-scanning.png", caption="QR Code scanning", use_column_width=True)
    with col2:
        st.image(r"files/QR.png", caption="QR Code scanning", use_column_width=True)
    st.header("Cardboard boxes 2")
    col1, col2 = st.columns(2)

    with col1:
        st.image(r"files/qr-scanning2.jpg", caption="QR Code scanning", use_column_width=True)
    with col2:
        st.image(r"files/QR2.png", caption="QR Code scanning", use_column_width=True)
        


# Function to display the Facial Recognition page
def facial_recognition_page():
    st.title("Facial Recognition")
    st.write("Revolutionize warehouse security and efficiency with our advanced facial recognition system, tailored for seamless customer and employee management. Our state-of-the-art technology captures and stores facial data securely, allowing for quick and accurate identification at entry points and restricted areas. With integrated memory storage, our system learns and recognizes individuals over time, enhancing security protocols and streamlining access management. Experience heightened operational control and peace of mind with our facial recognition solution, designed to optimize security while improving workflow efficiency in warehouses.")
    st.header("Recognizing Customers")
    st.video(r"files/facial recognition.mp4")  # Ensure correct file path and extension


# Function to display the Query Database page
def query_database_page():
    conn = sqlite3.connect('inventory_software2.db')
    cursor = conn.cursor()

    def read_multiple_qr_codes_from_frame(frame):
        decoded_objects = decode(frame)
        decoded_info = []

        for obj in decoded_objects:
            data = obj.data.decode("utf-8")
            decoded_info.append(data)
        
        # Get the bounding box coordinates
            points = obj.polygon
            if len(points) == 4:
                x1, y1 = points[0].x, points[0].y
                x2, y2 = points[2].x, points[2].y
            else:
                x1, y1 = points[0].x, points[0].y
                x2, y2 = points[1].x, points[1].y
        
        # Draw rectangle around QR code
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 5)
            cv2.putText(frame, data, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

        return decoded_info, frame

# Function to format the data
    def format_data(data):
        raw_data_list = data.split('$')
        formatted_data = {}
        for item in raw_data_list:
            key, value = item.split(':', 1)
            formatted_data[key] = value
        return formatted_data
    
    def insert_qr_data_into_db(data, conn):
        try:
            cursor = conn.cursor()
            sql_query = """
                INSERT INTO items_details (item_id, item_name, description, quantity, price, date_added, storage_location)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
        # Convert appropriate fields to integer and float
            item_id = int(data.get('Item ID', 0))
            quantity = int(data.get('Quantity', 0))
            price = float(data.get('Price', 0.0))
        
            cursor.execute(sql_query, (
                item_id,
                data.get('Item Name', ''),
                data.get('Description', ''),
                quantity,
                price,
                data.get('Date Added', ''),
                data.get('Storage Location', '')
            ))
            conn.commit()
            st.success("QR Data inserted into database successfully")
        except Exception as e:
            st.error(f"Error inserting QR Data into database: {e}")

# Ensure items_details table exists
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS items_details (
        item_id INTEGER PRIMARY KEY,
        item_name TEXT,
        description TEXT,
        quantity INTEGER,
        price REAL,
        date_added TEXT,
        storage_location TEXT
    )
    ''')

# Optional: Insert sample data if the table is empty (remove this in production)
    cursor.execute("SELECT COUNT(*) FROM items_details")
    if cursor.fetchone()[0] == 0:
        sample_data = [
            (1, "Laptop", "15\" MacBook Pro", 10, 2000.00, "2024-06-25 00:00:00", "Warehouse A"),
            (2, "Printer", "Wireless Laser Printer", 5, 500.00, "2024-06-25 00:00:00", "Office B"),
            (3, "Desk Chair", "Ergonomic Office Chair", 20, 250.00, "2024-06-24 00:00:00", "Office A"),
            (4, "Monitor", "27\" Dell Monitor", 15, 300.00, "2024-06-23 00:00:00", "Warehouse B"),
            (5, "Keyboard", "Mechanical Keyboard", 50, 80.00, "2024-06-22 00:00:00", "Warehouse C"),
            (6, "Mouse", "Wireless Mouse", 45, 25.00, "2024-06-21 00:00:00", "Warehouse C"),
            (7, "Tablet", "10\" Android Tablet", 25, 150.00, "2024-06-20 00:00:00", "Warehouse D"),
            (8, "Smartphone", "Latest Model Smartphone", 30, 1000.00, "2024-06-19 00:00:00", "Warehouse E"),
            (9, "External Hard Drive", "2TB External Hard Drive", 60, 100.00, "2024-06-18 00:00:00", "Warehouse F"),
            (10, "USB Flash Drive", "64GB USB Flash Drive", 200, 15.00, "2024-06-17 00:00:00", "Warehouse G")
        ]
        cursor.executemany('''
        INSERT INTO items_details (item_id, item_name, description, quantity, price, date_added, storage_location)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', sample_data)
        conn.commit()
    

    def create_qr_code(data):
    # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

    # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)

    # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")
        return img

# Sidebar for different operations
    col1, col2, col3 = st.columns(3)
    with col2:
        operations = ["View Data", "Get QR", "Update Data", "Delete Data"]
        operation = st.selectbox("Select Operation", operations, key="database_operations")

    if operation == "View Data":
        st.header("View Data")
        try:
                df = pd.read_sql_query("SELECT * FROM items_details", conn)
                st.dataframe(df)
        except Exception as e:
                st.error(f"Error: {e}")
        st.header("QR Code Scanning and Database Insertion")
        st.info("Please scan a QR code to insert its data into the database.")

        button1 = st.button("Scan QR", key='QR-scanning')
        if button1:
            cap = cv2.VideoCapture(0)

            if not cap.isOpened():
                st.error("Error: Could not open webcam.")
            else:
                st.success("Webcam opened successfully. Press 'q' to quit scanning.")

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    st.error("Failed to grab frame")
                    break

        # Read QR codes from the frame
                decoded_infos, annotated_frame = read_multiple_qr_codes_from_frame(frame)
    
                for data in decoded_infos:
                    if data:
                        formatted_data = format_data(data)
                        st.info(f"Decoded data: {formatted_data}")
                        insert_qr_data_into_db(formatted_data, conn)

        # Display the frame with QR code annotations
                cv2.imshow('Webcam QR Code Scanner', annotated_frame)
        
        # Bring the window to the front
                cv2.setWindowProperty('Webcam QR Code Scanner', cv2.WND_PROP_TOPMOST, 1)

        # Check for user input to quit scanning
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    # Release the webcam and close windows
            cap.release()
            cv2.destroyAllWindows()

        

    elif operation == "Get QR":
        st.title("QR Code Generator for Inventory Item")

    # Input fields
        item_id = st.text_input("Item ID")
        item_name = st.text_input("Item Name")
        description = st.text_input("Description")
        quantity = st.number_input("Quantity", min_value=0, step=1)
        price = st.number_input("Price", min_value=0.0, step=0.01)
        date_added = st.date_input("Date Added")
        storage_location = st.text_input("Storage Location")

        if st.button("Generate QR Code"):
            if item_id and item_name and description and quantity and price and     date_added and storage_location:
                data = f"Item ID:{item_id}$Item Name:{item_name}$Description:{description}$Quantity:{quantity}$Price:{price}$Date Added:{date_added}$Storage Location:{storage_location}"
                qr_img = create_qr_code(data)

            # Convert PIL image to BytesIO
                img_buffer = BytesIO()
                qr_img.save(img_buffer, format="PNG")
                img_buffer.seek(0)
                col1,col2,col3 = st.columns(3)
                with col2:

            # Display the QR code image in Streamlit
                    st.image(img_buffer, caption="QR Code", use_column_width=True)
            else:
                st.error("Please fill out all fields")

    elif operation == "Update Data":
        st.header("Update Data")
        item_id = st.number_input("Enter Item ID to Update", min_value=1, step=1)
        item_name = st.text_input("Item Name")
        description = st.text_input("Description")
        quantity = st.number_input("Quantity", min_value=0, step=1)
        price = st.number_input("Price", min_value=0.0, step=0.01)
        date_added = st.date_input("Date Added")
        storage_location = st.text_input("Storage Location")

        if st.button("Update"):
            try:
                cursor.execute("""
                    UPDATE items_details
                    SET item_name=?, description=?, quantity=?, price=?, date_added=?, storage_location=?
                    WHERE item_id=?
                """, (item_name, description, quantity, price, date_added, storage_location, item_id))
                conn.commit()
                st.success("Data updated successfully")
            except Exception as e:
                st.error(f"Error: {e}")


    elif operation == "Delete Data":
        st.header("Delete Data")
        item_id = st.number_input("Enter Item ID to Delete", min_value=1, step=1)
        if st.button("Delete"):
            try:
                cursor.execute("DELETE FROM items_details WHERE item_id=?", (item_id,))
                conn.commit()
                st.success("Data deleted successfully")
            except Exception as e:
                st.error(f"Error: {e}")


# Close the database connection
    conn.close()

# Main function to control navigation
def main():
        if 'page' not in st.session_state:
            st.session_state.page = 'home'

        st.sidebar.title("Navigation")
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",
                options=["Home", "Smart CCTV Surveillance", "QR-Code Scanning", "Shelf Monitoring", "Facial Recognition", "Query Database"],
                icons=["house", "camera-video", "image", "eye", "person", "database"],
                menu_icon="cast",
                default_index=0,
            )

        if selected == "Home":
            st.session_state.page = 'home'
        elif selected == "Smart CCTV Surveillance":
            st.session_state.page = 'cctv'
        elif selected == "QR-Code Scanning":
            st.session_state.page = 'QR-Code Scanning'
        elif selected == "Shelf Monitoring":
            st.session_state.page = 'self_monitoring'
        elif selected == "Facial Recognition":
            st.session_state.page = 'facial_recognition'
        elif selected == "Query Database":
            st.session_state.page = 'query_database'

        if st.session_state.page == 'home':
            home_page()
        elif st.session_state.page == 'cctv':
            smart_cctv_surveillance_page()
        elif st.session_state.page == 'QR-Code Scanning':
            qr_scanning()
        elif st.session_state.page == 'facial_recognition':
            facial_recognition_page()
        elif st.session_state.page == 'query_database':
            query_database_page()
        elif st.session_state.page == 'self_monitoring':
            self_monitoring_page()

# Run the app
if __name__ == "__main__":
    main()
