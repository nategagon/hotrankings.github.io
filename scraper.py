import json
import requests
from datetime import datetime

# The Expanded 2026 Hit List
ai_companions = [
    {"name": "Candy AI", "subreddit": "CandyAI", "base_score": 600, "url": "https://candy.ai/?ref=YOUR_AFFILIATE_ID", "description": "The undisputed king of unfiltered visual generation."},
    {"name": "JuicyChat.AI", "subreddit": "JuicyChat", "base_score": 550, "url": "https://juicychat.ai/?ref=YOUR_AFFILIATE_ID", "description": "Leading the market in persistent memory and NSFW roleplay."},
    {"name": "Janitor AI", "subreddit": "JanitorAI_Official", "base_score": 520, "url": "https://janitorai.com/?ref=YOUR_AFFILIATE_ID", "description": "Massive community-driven bot library with zero filter options."},
    {"name": "Character.ai", "subreddit": "CharacterAI", "base_score": 500, "url": "https://character.ai/?ref=YOUR_AFFILIATE_ID", "description": "The mainstream giant. Massive traffic, brilliant logic, heavy filters."},
    {"name": "SpicyChat AI", "subreddit": "SpicyChatAI", "base_score": 480, "url": "https://spicychat.ai/?ref=YOUR_AFFILIATE_ID", "description": "Aggressive growth, zero filters, and highly responsive chat."},
    {"name": "Kupid AI", "subreddit": "KupidAI", "base_score": 450, "url": "https://kupid.ai/?ref=YOUR_AFFILIATE_ID", "description": "High conversational quality with immersive voice and video integration."},
    {"name": "Crushon AI", "subreddit": "CrushonAI", "base_score": 430, "url": "https://crushon.ai/?ref=YOUR_AFFILIATE_ID", "description": "Top-tier Character.ai alternative with unrestricted, raw interactions."},
    {"name": "DreamGF", "subreddit": "DreamGF", "base_score": 400, "url": "https://dreamgf.ai/?ref=YOUR_AFFILIATE_ID", "description": "Heavy focus on customized, hyper-realistic visual companion creation."},
    {"name": "Yodayo", "subreddit": "YodayoAI", "base_score": 350, "url": "https://yodayo.com/?ref=YOUR_AFFILIATE_ID", "description": "Anime and VTuber focused roleplay with built-in image generation."},
    {"name": "Replika", "subreddit": "replika", "base_score": 300, "url": "https://replika.com/?ref=YOUR_AFFILIATE_ID", "description": "The original mainstream AI companion. Heavy emotional and therapeutic focus."},
    {"name": "Kindroid", "subreddit": "KindroidAI", "base_score": 150, "url": "https://kindroid.ai/?ref=YOUR_AFFILIATE_ID", "description": "Unfiltered, highly intelligent text generation with custom selfie capabilities."},
    {"name": "Nomi AI", "subreddit": "NomiAI", "base_score": 100, "url": "https://nomi.ai/?ref=YOUR_AFFILIATE_ID", "description": "Incredibly natural personality traits, voice calls, and long-term retention."}
]

def fetch_reddit_mentions(subreddit):
    """
    Bypassing the commercial API limits by reading public JSON endpoints.
    """
    url = f"https://www.reddit.com/r/{subreddit}/new.json?limit=50"
    headers = {'User-Agent': 'HotRankings-Bot/1.0'}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            mentions = len(data['data']['children'])
            upvotes = sum(post['data']['ups'] for post in data['data']['children'])
            # Weight upvotes slightly less than raw post volume
            return mentions + (upvotes * 0.5) 
        return 0
    except Exception as e:
        print(f"Failed to scrape {subreddit}: {e}")
        return 0

def calculate_hot_rankings():
    print(f"[{datetime.now()}] Initiating HotRankings scrape...")
    
    for ai in ai_companions:
        # Fetch live social heat
        social_heat = fetch_reddit_mentions(ai['subreddit'])
        # Calculate final 'Hot Score'
        ai['hot_score'] = int(ai['base_score'] + social_heat)
        print(f"Analyzed {ai['name']} -> Hot Score: {ai['hot_score']}")

    # Sort the list ruthlessly from highest to lowest score
    ranked_list = sorted(ai_companions, key=lambda x: x['hot_score'], reverse=True)
    
    # Output the new rankings to a JSON file
    with open('live_rankings.json', 'w') as outfile:
        json.dump(ranked_list, outfile, indent=4)
        
    print("Rankings successfully generated and saved.")

if __name__ == "__main__":
    calculate_hot_rankings()
