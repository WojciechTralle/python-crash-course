# exercise 8-12
def sandwich_items(*items):
    """Print a summary of the sandwich order."""
    print("\nMaking a sandwich with:")
    for item in items:
        print(f"- {item}")

sandwich_items('tomatoes', 'onions', 'chili peppers')
sandwich_items('mushrooms', 'cheese')
sandwich_items('butter')
