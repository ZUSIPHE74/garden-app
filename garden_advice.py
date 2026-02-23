import datetime

gardening_tips = {
    1: "January: Start planning your vegetable garden. Order seeds and prepare your soil.",
    2: "February: Prune fruit trees and winter-flowering shrubs. Start seeds indoors.",
    3: "March: Plant cool-season crops like peas and lettuce. Clean up garden beds.",
    4: "April: Plant summer bulbs. Start tomatoes and peppers indoors.",
    5: "May: Plant warm-season crops. Watch for late frosts in colder regions.",
    6: "June: Regular watering and mulching. Harvest early vegetables.",
    7: "July: Water deeply during hot weather. Deadhead flowers to encourage blooming.",
    8: "August: Plant fall vegetables. Continue harvesting and preserving.",
    9: "September: Plant spring-flowering bulbs. Clean up fallen leaves.",
    10: "October: Plant trees and shrubs. Put garden to bed for winter.",
    11: "November: Protect plants from frost. Clean and store garden tools.",
    12: "December: Plan next year's garden. Feed birds and enjoy the winter landscape."
}

seasonal_tips = {
    "spring": "Spring: Time for planting! Prepare soil, start seeds, and enjoy the new growth.",
    "summer": "Summer: Focus on watering, mulching, and pest control. Harvest regularly.",
    "fall": "Fall: Plant bulbs, clean up garden debris, and prepare for winter.",
    "winter": "Winter: Plan your garden, maintain tools, and protect plants from cold."
}

def get_current_month():
    return datetime.datetime.now().month

def get_month_name(month):
    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    return month_names[month - 1]

def get_season(month, hemisphere="northern"):
    if hemisphere.lower() == "northern":
        if month in [12, 1, 2]:
            return "winter"
        elif month in [3, 4, 5]:
            return "spring"
        elif month in [6, 7, 8]:
            return "summer"
        elif month in [9, 10, 11]:
            return "fall"
    else:
        if month in [12, 1, 2]:
            return "summer"
        elif month in [3, 4, 5]:
            return "fall"
        elif month in [6, 7, 8]:
            return "winter"
        elif month in [9, 10, 11]:
            return "spring"
    return "unknown"

def get_gardening_advice(month=None, hemisphere="northern"):
    if month is None:
        month = get_current_month()
    
    if month < 1 or month > 12:
        return {"error": "Invalid month. Please provide a month between 1 and 12."}
    
    season = get_season(month, hemisphere)
    month_name = get_month_name(month)
    
    monthly_tip = gardening_tips.get(month, f"{month_name}: No specific tip available.")
    seasonal_tip = seasonal_tips.get(season, f"Seasonal advice for {season} is not available.")
    
    return {
        "month": month_name,
        "season": season,
        "hemisphere": hemisphere,
        "monthly_tip": monthly_tip,
        "seasonal_tip": seasonal_tip
    }

def print_gardening_advice(month=None, hemisphere="northern"):
    advice = get_gardening_advice(month, hemisphere)
    
    if "error" in advice:
        print(f"Error: {advice['error']}")
        return
    
    print("\n" + "="*50)
    print(f"GARDENING ADVICE - {advice['month']}")
    print("="*50)
    print(f"Hemisphere: {advice['hemisphere'].title()}")
    print(f"Season: {advice['season'].title()}")
    print("\n Monthly Tip:")
    print(f"   {advice['monthly_tip']}")
    print("\nSeasonal Tip:")
    print(f"   {advice['seasonal_tip']}")
    print("="*50 + "\n")

if __name__ == "__main__":
    print("Welcome to the Garden Advice App!")
    print("Get personalized gardening tips based on your location and time of year.")
    print_gardening_advice()
    print_gardening_advice(hemisphere="southern")
    print_gardening_advice(month=7, hemisphere="northern")
