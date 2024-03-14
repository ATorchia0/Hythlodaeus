import feedparser
import asyncio
import async_timeout


#schema, ctx -> url dict.
curSubs = {}
update_time = {}

#method to add subscription
##requires ctx, url
def monitorSubscirption(ctx, url):
    curSubs.update({ctx: url})


#remove subcription
def endSubscription(ctx, url):
    subscirptionID = getSubscription(ctx, url)
    curSubs.pop(subscirptionID)


#get Subscription
def getSubscription(ctx, url):
    feed = 0
    for thread in curSubs.keys():
        if(thread.guild == ctx.guild):
            feed = thread

    return feed


async def check_rss_feeds(feed_dict, last_check_dict):
    """
    Checks each RSS feed in the given dictionary and calls the 'send' method if an update has occurred.  AI generated.
    
    Args:
        feed_dict (dict): A dictionary where keys are CONTEXT objects with a 'send' method, and values are RSS feed URLs.
        last_check_dict (dict): A dictionary to store the last check timestamp for each feed.
    """
    while True:
        for context, feed_url in feed_dict.items():
            try:
                feed = feedparser.parse(feed_url)
                latest_entry = feed.entries[0] if feed.entries else None
                last_check_time = last_check_dict.get(feed_url, None)

                if latest_entry and (not last_check_time or latest_entry.published_parsed > last_check_time):
                    # Update the last check time
                    last_check_dict[feed_url] = latest_entry.published_parsed
                    await context.send("New update in RSS feed: {latest_entry.url}")
            except Exception as e:
                print(f"Error checking feed {feed_url}: {e}")

        # Sleep for a specified interval (e.g., 1 hour)
        await asyncio.sleep(3600)
