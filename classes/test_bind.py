from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import search_projects
from freelancersdk.resources.projects.exceptions import \
    ProjectsNotFoundException
from freelancersdk.resources.projects.helpers import (
    create_search_projects_filter,
    create_get_projects_user_details_object,
    create_get_projects_project_details_object,
)
from freelancersdk.resources.projects import place_project_bid
from freelancersdk.session import Session
from freelancersdk.resources.users \
    import get_self_user_id
from freelancersdk.exceptions import BidNotPlacedException
import os

#FLN_URL="https://www.freelancer-sandbox.com"
FLN_URL="https://www.freelancer.com"
FLN_OAUTH_TOKEN = "WY5xzKBbqRAuxTMwBYMkTGkcSAMIQa"

def sample_place_project_bid(project_id, min_amount, max_amount, period):

    url = FLN_URL
    oauth_token = FLN_OAUTH_TOKEN

    session = Session(oauth_token=oauth_token, url=url)
    my_user_id = get_self_user_id(session)
    bid_data = {
        'project_id': int(project_id),
        'bidder_id': my_user_id,
        'amount': min_amount + (max_amount / 4),
        'period': period,
        'milestone_percentage': 100,
        'description': 'I can work with you, i have experience in software engineering and project management. Based on your requirements i can also implement functionalities that can improve our work and ensure hight quality work. Thank you.',
    }
    try:
        return place_project_bid(session, **bid_data)
    except BidNotPlacedException as e:
        print(e)
        return None

def sample_search_projects():
    url = FLN_URL
    oauth_token = FLN_OAUTH_TOKEN
    session = Session(oauth_token=oauth_token, url=url)

    query = 'javascript web application html css food delivery landing page company'
    search_filter = create_search_projects_filter(
        sort_field= 'time_updated',          
        min_avg_price=100,
        project_types='fixed',
        or_search_query= True,
    )

    try:
        p = search_projects(
            session,
            query=query,
            search_filter=search_filter
        )

    except ProjectsNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return p


p = sample_search_projects()
if p:
    for project in p["projects"]:
        print("="*100)
        print("Title: "+ project["title"])
        print("Link: https://www.freelancer.com/projects/"+ project["seo_url"])
        print("Title: "+ project["title"])
        print("Currency: "+ project["currency"]["name"])
        print("Budget: "+ str(project["budget"]["minimum"]) + " MIN - "+ str(project["budget"]["maximum"]) + " MAX")
        print("Bids: "+ str(project["bid_stats"]["bid_count"]))
        if(project["bid_stats"]["bid_count"] <= 30 and project["status"] == "active"):
            print("Sending proposeal...")
            sended = sample_place_project_bid(project["id"], project["budget"]["minimum"], project["budget"]["maximum"], 7)
            print("Done")
        else:
            print("Not worth for assign, skipping")