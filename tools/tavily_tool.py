from tavily import TavilyClient 
import os
from dotenv import load_dotenv

load_dotenv()
#creation of client
client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

#using client it will search for the results from the internet
def tavily_search(query):
    response=client.search(
        query=query,
        max_results=5
    )
    # this is to fileter the response from the meta data
    results = []

    for i,r in enumerate(response["results"],1):
        title = r.get("title","unknown")
        url   = r.get("url","")
        snippet = r.get("content","").strip()
        #keep only the 300 chars of data to avoid wall of text
        if len(snippet)>300:
            snippet=snippet[:300].rsplit(" ",1)[0] + "..." 
        results.append(f"{i}. **{title}**\n   {url}\n  {snippet}")
    return "\n\n".join(results)


