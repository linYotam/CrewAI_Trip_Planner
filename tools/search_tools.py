import json
import os
from exa_py import Exa
from langchain.agents import tool
import requests
from langchain.tools import tool
from typing import List


class SearchTools():

    @tool
    def search(query: str):
        """Search for a webpage based on the query."""
        return SearchTools._exa().search(f"{query}", use_autoprompt=True, num_results=3)
    
    
    @tool
    def find_similar(url: str):
        """Search for webpages similar to a given URL.
        The url passed in should be a URL returned from `search`.
        """
        return SearchTools._exa().find_similar(url, num_results=3)

    # @tool
    # def get_contents(ids: str):
    #     """Get the contents of a webpage.
    #     The ids must be passed in as a list, a list of ids returned from `search`.
    #     """
    #     ids = eval(ids)

    #     contents = str(SearchTools._exa().get_contents(ids))
    #     contents = contents.split("URL:")
    #     contents = [content[:1000] for content in contents]
    #     return "\n\n".join(contents)
    
    @tool
    def get_contents(ids: List[str]):
        """Get the contents of a webpage.
        The ids must be passed in as a list, a list of ids returned from `search`.
        """
        if not isinstance(ids, list) or not all(isinstance(i, str) for i in ids):
            raise ValueError("ids must be a list of strings")

        # Assuming SearchTools._exa().get_contents(ids) returns contents related to the IDs.
        contents = SearchTools._exa().get_contents(ids)
        
        # Convert contents to string if necessary and handle processing.
        contents = str(contents)
        contents = contents.split("URL:")
        contents = [content[:1000] for content in contents]
        return "\n\n".join(contents)
        
    def tools():
        return [
        SearchTools.search,
        SearchTools.find_similar,
        SearchTools.get_contents
        ]
    def _exa():
        return Exa(api_key=os.environ.get('EXA_API_KEY'))


    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet
        about a a given topic and return relevant results"""
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        # check if there is an organic key
        if 'organic' not in response.json():
            return "Sorry, I couldn't find anything about that, there could be an error with you serper api key."
        else:
            results = response.json()['organic']
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}", f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}", "\n-----------------"
                    ]))
                except KeyError:
                    next

            return '\n'.join(string)