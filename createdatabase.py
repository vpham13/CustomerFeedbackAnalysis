import sqlite3

def create_database():
    connection = sqlite3.connect('skincare.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SkincareProducts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT,
            condition TEXT,
            rating REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SkincareRoutines (
            id INTEGER PRIMARY KEY,
            routine_name TEXT NOT NULL,
            steps TEXT,
            condition TEXT
        )
    ''')

    cursor.executemany('''
        INSERT INTO SkincareProducts (name, category, condition, rating)
        VALUES (?, ?, ?, ?)
    ''', [
        ('Salicylic Acid Cleanser', 'Cleanser', 'acne', 4.5),
        ('Benzoyl Peroxide Gel', 'Treatment', 'acne', 4.2),
        ('Hyaluronic Acid Serum', 'Serum', 'dryness', 4.8),
        ('Ceramide Moisturizer', 'Moisturizer', 'dryness', 4.7),
        ('Sunscreen SPF 50', 'Sunscreen', 'sensitivity', 4.6),
        ('Gentle Foaming Cleanser', 'Cleanser', 'sensitivity', 4.5)
    ])

    cursor.executemany('''
        INSERT INTO SkincareRoutines (routine_name, steps, condition)
        VALUES (?, ?, ?)
    ''', [
        ('Morning Routine for Acne', 
         '1. Cleanse with Salicylic Acid Cleanser\n'
         '2. Apply Benzoyl Peroxide Gel\n'
         '3. Use Sunscreen SPF 50', 
         'acne'),
        ('Evening Routine for Acne', 
         '1. Cleanse with Salicylic Acid Cleanser\n'
         '2. Apply Benzoyl Peroxide Gel\n'
         '3. Moisturize with a light, non-comedogenic moisturizer', 
         'acne'),
        ('Morning Routine for Dryness', 
         '1. Cleanse with Gentle Foaming Cleanser\n'
         '2. Apply Hyaluronic Acid Serum\n'
         '3. Use Ceramide Moisturizer', 
         'dryness'),
        ('Evening Routine for Dryness', 
         '1. Cleanse with Gentle Foaming Cleanser\n'
         '2. Apply Hyaluronic Acid Serum\n'
         '3. Moisturize with Ceramide Moisturizer', 
         'dryness'),
        ('Morning Routine for Sensitivity', 
         '1. Cleanse with Gentle Foaming Cleanser\n'
         '2. Apply Aloe Vera Gel\n'
         '3. Use Fragrance-Free Hydrating Cream', 
         'sensitivity'),
        ('Evening Routine for Sensitivity', 
         '1. Cleanse with Gentle Foaming Cleanser\n'
         '2. Apply Aloe Vera Gel\n'
         '3. Moisturize with Fragrance-Free Hydrating Cream', 
         'sensitivity')
    ])

    connection.commit()
    connection.close()

def get_recommendations(skin_condition):
    connection = sqlite3.connect('skincare.db')
    cursor = connection.cursor()

    # Query to get recommended products 
    query = "SELECT name, category FROM SkincareProducts WHERE condition = ?"
    cursor.execute(query, (skin_condition,))
    products = cursor.fetchall()

    # Query to get recommended routines
    query_routine = "SELECT routine_name, steps FROM SkincareRoutines WHERE condition = ?"
    cursor.execute(query_routine, (skin_condition,))
    routines = cursor.fetchall()

    connection.close()
    return products, routines

def main():
    create_database()  

    print("Welcome to the Skincare Advisor!")
    condition = input("What skin issue are you facing? (e.g., acne, dryness, sensitivity): ").lower()

    products, routines = get_recommendations(condition)

    # Display products
    if products:
        print("\nRecommended Products:")
        for name, category in products:
            print(f"- {name} ({category})")
    else:
        print("\nNo product recommendations found for your condition.")

    # Display routine
    if routines:
        print("\nRecommended Routine:")
        for routine_name, steps in routines:
            print(f"\n{routine_name}\nSteps:\n{steps}")
    else:
        print("\nNo routine recommendations found for your condition.")

if __name__ == '__main__':
    main()
