import feedparser
import asyncio
import async_timeout


#schema, ctx -> url dict.
curSubs = {}

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


#post subscriptions to subscription db which is gonna be a file generated and not a real database because ain't no way i'm properly doing this LMAO

