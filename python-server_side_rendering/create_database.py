import sqlite3

def create_database():
    """
    Create and populate the SQLite database with sample data
    """
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Create Products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Insert sample data
    cursor.execute('''
        INSERT OR REPLACE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Python Book', 'Books', 29.99)
    ''')
    
    conn.commit()
    conn.close()
    print("Database created and populated successfully!")

if __name__ == '__main__':
    create_database()
