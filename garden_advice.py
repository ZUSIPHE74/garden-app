import datetime

# Implementation log:
# 2026-02-25: Removed duplicate get_gardening_advice definition.
# 2026-02-25: Fixed __main__ block indentation so the script entrypoint is valid.
# 2026-02-25: Replaced emoji output labels for Windows console compatibility.
# 2026-02-25: Added southern hemisphere monthly tips.

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
    12: "December: Plan next year's garden. Feed birds and enjoy the winter landscape.",
}

climate_zone_tips = {
    "tropical": {
        "general": "Tropical: Year-round growing season. Focus on pest management and rain protection.",
        "wet_season": "Wet season: Plant root vegetables. Ensure good drainage.",
        "dry_season": "Dry season: Focus on drought-tolerant plants. Mulch heavily.",
    },
    "temperate": {
        "general": "Temperate: Four distinct seasons. Follow seasonal planting guides.",
        "spring": "Spring: Start seeds indoors. Plant cool-season crops.",
        "summer": "Summer: Regular watering. Plant warm-season vegetables.",
        "fall": "Fall: Harvest and preserve. Plant garlic and cover crops.",
        "winter": "Winter: Plan garden. Maintain tools. Protect perennials.",
    },
    "mediterranean": {
        "general": "Mediterranean: Mild, wet winters and warm, dry summers. Focus on drought tolerance.",
        "spring": "Spring: Plant warm-season crops. Conserve water.",
        "summer": "Summer: Drought-tolerant plants. Deep watering. Shade protection.",
        "fall": "Fall: Plant cool-season crops. Prepare for rains.",
        "winter": "Winter: Plant natives. Improve soil with organic matter.",
    },
    "arid": {
        "general": "Arid: Low rainfall, extreme temperatures. Focus on water conservation.",
        "spring": "Spring: Plant heat-tolerant varieties. Use shade cloth.",
        "summer": "Summer: Water deeply but infrequently. Mulch heavily.",
        "fall": "Fall: Second planting season. Prepare for cooler weather.",
        "winter": "Winter: Plant cool-season crops. Protect from frost.",
    },
    "cold": {
        "general": "Cold: Short growing season. Focus on cold-hardy varieties.",
        "spring": "Spring: Start seeds indoors. Wait until last frost to plant.",
        "summer": "Summer: Quick-maturing varieties. Extend season with row covers.",
        "fall": "Fall: Harvest before frost. Plant cold frames.",
        "winter": "Winter: Plan next season. Start seeds indoors under lights.",
    },
}

southern_hemisphere_tips = {
    1: "January: Peak summer care. Water deeply and harvest heat-loving crops.",
    2: "February: Continue summer maintenance. Watch for sun stress and pests.",
    3: "March: Begin autumn planting for cool-season vegetables.",
    4: "April: Improve soil and plant autumn crops like brassicas.",
    5: "May: Prepare for winter. Protect sensitive plants from cold snaps.",
    6: "June: Midwinter care. Prune dormant plants and plan spring beds.",
    7: "July: Continue winter maintenance. Start seeds indoors for spring.",
    8: "August: Late winter prep. Feed soil and begin spring seedlings.",
    9: "September: Early spring planting. Transplant seedlings outdoors.",
    10: "October: Mid-spring growth. Mulch and monitor rapid growth.",
    11: "November: Late spring planting. Stake and support tall crops.",
    12: "December: Early summer harvests begin. Increase watering frequency.",
}

seasonal_tips = {
    "spring": "Spring: Time for planting! Prepare soil, start seeds, and enjoy the new growth.",
    "summer": "Summer: Focus on watering, mulching, and pest control. Harvest regularly.",
    "fall": "Fall: Plant bulbs, clean up garden debris, and prepare for winter.",
    "winter": "Winter: Plan your garden, maintain tools, and protect plants from cold.",
}


def get_current_month():
    return datetime.datetime.now().month


def get_month_name(month):
    month_names = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    return month_names[month - 1]


def get_season(month, hemisphere="northern"):
    if hemisphere.lower() == "northern":
        if month in [12, 1, 2]:
            return "winter"
        if month in [3, 4, 5]:
            return "spring"
        if month in [6, 7, 8]:
            return "summer"
        if month in [9, 10, 11]:
            return "fall"
    else:
        if month in [12, 1, 2]:
            return "summer"
        if month in [3, 4, 5]:
            return "fall"
        if month in [6, 7, 8]:
            return "winter"
        if month in [9, 10, 11]:
            return "spring"
    return "unknown"


def get_gardening_advice(month=None, hemisphere="northern", climate_zone="temperate"):
    if month is None:
        month = get_current_month()

    if month < 1 or month > 12:
        return {"error": "Invalid month. Please provide a month between 1 and 12."}

    if climate_zone not in climate_zone_tips:
        zones = ", ".join(climate_zone_tips.keys())
        return {"error": f"Invalid climate zone. Choose from: {zones}"}

    season = get_season(month, hemisphere)
    month_name = get_month_name(month)

    if hemisphere.lower() == "southern":
        monthly_tip = southern_hemisphere_tips.get(month, f"{month_name}: No specific tip available.")
    else:
        monthly_tip = gardening_tips.get(month, f"{month_name}: No specific tip available.")

    seasonal_tip = seasonal_tips.get(
        season, f"Seasonal advice for {season} is not available."
    )
    climate_tip = climate_zone_tips[climate_zone].get(
        season, climate_zone_tips[climate_zone].get("general", "No climate tip available.")
    )

    return {
        "month": month_name,
        "season": season,
        "hemisphere": hemisphere,
        "climate_zone": climate_zone,
        "monthly_tip": monthly_tip,
        "seasonal_tip": seasonal_tip,
        "climate_tip": climate_tip,
    }


def print_gardening_advice(month=None, hemisphere="northern", climate_zone="temperate"):
    advice = get_gardening_advice(month, hemisphere, climate_zone)

    if "error" in advice:
        print(f"Error: {advice['error']}")
        return

    print("\n" + "=" * 50)
    print(f"GARDENING ADVICE - {advice['month']}")
    print("=" * 50)
    print(f"Hemisphere: {advice['hemisphere'].title()}")
    print(f"Climate Zone: {advice['climate_zone'].title()}")
    print(f"Season: {advice['season'].title()}")
    print("\nMonthly Tip:")
    print(f"   {advice['monthly_tip']}")
    print("\nSeasonal Tip:")
    print(f"   {advice['seasonal_tip']}")
    print("\nClimate Zone Tip:")
    print(f"   {advice['climate_tip']}")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    print("Welcome to the Garden Advice App!")
    print("Get personalized gardening tips based on your location and time of year.")

    print("\n" + "=" * 50)
    print("EXAMPLE 1: Northern Hemisphere, Temperate (default)")
    print_gardening_advice()

    print("\n" + "=" * 50)
    print("EXAMPLE 2: Southern Hemisphere, Mediterranean")
    print_gardening_advice(hemisphere="southern", climate_zone="mediterranean")

    print("\n" + "=" * 50)
    print("EXAMPLE 3: Northern Hemisphere, Arid, July")
    print_gardening_advice(month=7, hemisphere="northern", climate_zone="arid")

    print("\n" + "=" * 50)
    print("EXAMPLE 4: Northern Hemisphere, Cold, January")
    print_gardening_advice(month=1, hemisphere="northern", climate_zone="cold")
