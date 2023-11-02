from django.shortcuts import render

from .models import Feedentry
import feedparser
from django.http import JsonResponse


def index(request):
    if request.method == 'POST':
        rss_url = request.POST['rss_url']
        feed = feedparser.parse(rss_url)
        
        for entry in feed.entries:
            Feedentry.objects.create(
                title = entry.title,
                description = entry .summary,
                link = entry.link
            )
            
        entries = Feedentry.objects.all()
        return render(request , 'rss/feed.html',{'entries':entries})
    return render(request, 'rss/index.html')

def fetch_rss_feed_data(rss_url):
    feed = feedparser.parse(rss_url)
    entries = feed.entries
    return entries
def display_feed(request):
    rss_url = 'your_rss_feed_url'
    entries = fetch_rss_feed_data(rss_url)
    
    return render(request , 'rss/feed.html',{'entries':entries})




def fetch_rss_feed(request):
    rss_url = request.GET.get("rss_url", "")

    try:
        # Fetch and parse the RSS feed
        feed = feedparser.parse(rss_url)

        # Initialize an empty list to store feed entries
        feed_data = []

        # Iterate through the feed entries and extract relevant information
        for entry in feed.entries:
            feed_entry = {
                "title": entry.title,
                "summary": entry.summary,
                "link": entry.link,
            }
            feed_data.append(feed_entry)

        return JsonResponse(feed_data, safe=False)

    except Exception as e:
        # Handle errors, e.g., if the RSS feed cannot be fetched or parsed
        error_message = f"Error fetching or parsing RSS feed: {str(e)}"
        return JsonResponse({"error": error_message}, status=500)
