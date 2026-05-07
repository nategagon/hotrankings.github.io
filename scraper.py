import json

# Your Ultimate CrakRevenue Smartlink
SMARTLINK = "https://t.mbjms.com/412526/9403/0?target=listing&aff_sub5=SF_006OG000004lmDN"

# The Hardcoded VIP Hit List
# This acts as our static database. We are using generic, high-converting titles
# because the Smartlink will dynamically change the destination based on the user.
rankings = [
    {
        "id": 1,
        "name": "Premium AI Companion Match",
        "category": "AI Companions",
        "description": "The highest-rated, uncensored AI companion platform available right now. 100% private, highly responsive, and fully customizable.",
        "url": SMARTLINK,
        "hot_score": 9985,
        "trending": True
    },
    {
        "id": 2,
        "name": "Live Cam Network - VIP Access",
        "category": "Cam Sites",
        "description": "Instant access to the most active live cam network on the web. Thousands of active, unfiltered rooms available 24/7.",
        "url": SMARTLINK,
        "hot_score": 9850,
        "trending": True
    },
    {
        "id": 3,
        "name": "Local Hookup Matches",
        "category": "Dating",
        "description": "The fastest growing adult dating and casual hookup network. Extremely high match rates and instant messaging.",
        "url": SMARTLINK,
        "hot_score": 9420,
        "trending": True
    },
    {
        "id": 4,
        "name": "Candy AI - Visual Engine",
        "category": "AI Companions",
        "description": "The undisputed king of visual generation and hardcore roleplay. Step into the most realistic visual engine.",
        "url": SMARTLINK,
        "hot_score": 9100,
        "trending": False
    },
    {
        "id": 5,
        "name": "OurDream RP",
        "category": "AI Companions",
        "description": "Unfiltered storytelling and deep memory architecture for serious, long-term roleplayers.",
        "url": SMARTLINK,
        "hot_score": 8950,
        "trending": False
    },
    {
        "id": 6,
        "name": "SpicyChat Uncensored",
        "category": "AI Companions",
        "description": "A heavyweight in the unfiltered roleplay niche. Push the limits with zero restrictions.",
        "url": SMARTLINK,
        "hot_score": 8400,
        "trending": False
    }
]

def generate_rankings():
    # This writes our static list directly to the JSON file your website reads
    with open('live_rankings.json', 'w') as f:
        json.dump(rankings, f, indent=4)
    print("Successfully generated static CrakRevenue payload: live_rankings.json")

if __name__ == "__main__":
    generate_rankings()
