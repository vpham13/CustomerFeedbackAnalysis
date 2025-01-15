import sqlite3

def get_recommendations(skin_condition):
    connection = sqlite3.connect('skincare.db')
    cursor = connection.cursor()

    query = "SELECT name, category FROM SkincareProducts WHERE condition = ?"
    cursor.execute(query, (skin_condition,))
    products = cursor.fetchall()

    query_routine = "SELECT routine_name, steps FROM SkincareRoutines WHERE condition = ?"
    cursor.execute(query_routine, (skin_condition,))
    routines = cursor.fetchall()

    connection.close()
    return products, routines

def main():
    print("Welcome to the Skincare Advisor!")
    condition = input("What skin issue are you facing? (e.g., acne, dryness, sensitivity): ").lower()

    products, routines = get_recommendations(condition)

    if products:
        print("\nRecommended Products:")
        for name, category in products:
            print(f"- {name} ({category})")
    else:
        print("\nNo product recommendations found for your condition. Please check in later for more updates!")

    if routines:
        print("\nRecommended Routine:")
        for routine_name, steps in routines:
            print(f"\n{routine_name}\nSteps:\n{steps}")
    else:
        print("\nNo routine recommendations found for your condition. Please check in later for more updates!")

if __name__ == '__main__':
    main()
