import json

# Your Universal CrakRevenue Smartlink (The Mystery Box)
UNIVERSAL_SMARTLINK = "https://t.mbjms.com/412526/9403/0?target=listing&aff_sub5=SF_006OG000004lmDN"

# Placeholders for when you get specific links
DATING_LINK = UNIVERSAL_SMARTLINK  
CAM_LINK = UNIVERSAL_SMARTLINK
AI_LINK = UNIVERSAL_SMARTLINK

rankings = [
    {
        "id": "hero", 
        "name": "🚨 #1 EXCLUSIVE OFFER IN YOUR AREA 🚨",
        "category": "Auto-Match",
        "description": "Our algorithm has detected a high-priority, private invitation available in your current location. Click to reveal and claim your access before the window expires.",
        "url": UNIVERSAL_SMARTLINK,
        "hot_score": "MAX",
        "trending": True
    },
    {
        "id": "cam",
        "name": "Live Cam Network - VIP Access",
        "category": "Cam Sites",
        "description": "Instant access to the most active live cam network on the web. Thousands of active, unfiltered rooms available 24/7.",
        "url": CAM_LINK,
        "hot_score": 9850,
        "trending": True
    },
    {
        "id": "date",
        "name": "Local Hookup Matches",
        "category": "Dating",
        "description": "The fastest growing adult dating and casual hookup network. Extremely high match rates and instant messaging.",
        "url": DATING_LINK,
        "hot_score": 9420,
        "trending": False
    },
    {
        "id": "ai",
        "name": "Premium AI Companion Engine",
        "category": "AI Companions",
        "description": "The undisputed king of visual generation and hardcore roleplay. Step into the most realistic visual engine.",
        "url": AI_LINK,
        "hot_score": 9100,
        "trending": False
    }
]

def generate_rankings():
    with open('live_rankings.json', 'w') as f:
        json.dump(rankings, f, indent=4)
    print("Successfully generated Hero-Banner CrakRevenue payload.")

if __name__ == "__main__":
    generate_rankings()
