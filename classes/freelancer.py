# freelancer api
from freelancersdk.session import Session
from app_env import FLN_OAUTH_TOKEN, FLN_URL

from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import search_projects
from freelancersdk.resources.projects.exceptions import \
    ProjectsNotFoundException
from freelancersdk.resources.projects.helpers import (
    create_search_projects_filter,
    create_get_projects_user_details_object,
    create_get_projects_project_details_object,
)
from freelancersdk.resources.users \
    import get_self_user_id
from freelancersdk.exceptions import BidNotPlacedException
from freelancersdk.resources.projects import place_project_bid
from freelancersdk.resources.projects.projects import (
    get_projects, get_project_by_id
)
# 
import json
from functions.find_replace import find_replace

class FreelancerClient:
    def __init__(self,configPath):
        with open(configPath,"r",encoding="UTF-8") as jsondata:
            userdata = json.load(jsondata)
            formatted_text = find_replace(userdata)
            self.FORMATTED_TEXT = formatted_text
            self.FLN_OAUTH_TOKEN = userdata["FLN_OAUTH_TOKEN"]

    def getProjects(self,):
        url = FLN_URL
        oauth_token = self.FLN_OAUTH_TOKEN
        session = Session(oauth_token=oauth_token, url=url)

        query = 'Web'
        search_filter = create_search_projects_filter(
            sort_field= 'time_updated',
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
            self.projects = p["projects"]
            return p["total_count"]
        
    def sample_place_project_bid(self,PROJECT_ID):
        url = FLN_URL
        oauth_token = self.FLN_OAUTH_TOKEN
        project_id = PROJECT_ID

        session = Session(oauth_token=oauth_token, url=url)
        my_user_id = get_self_user_id(session)
        bid_data = {
            'project_id': int(project_id),
            'bidder_id': my_user_id,
            'amount': 10,
            'period': 2,
            'milestone_percentage': 100,
            'description': 'This is my bid',
        }
        try:
            return place_project_bid(session, **bid_data)
        except BidNotPlacedException as e:
            print(('Error message: %s' % e.message))
            print(('Error code: %s' % e.error_code))
            return None
        
    def sample_get_project_by_id(self, project_id):
        url = FLN_URL
        oauth_token = self.FLN_OAUTH_TOKEN
        session = Session(oauth_token=oauth_token, url=url)

        project_id = project_id
        project_details = create_get_projects_project_details_object(
            full_description=True
        )
        user_details = create_get_projects_user_details_object(
            basic=True
        )

        try:
            p = get_project_by_id(session, project_id, project_details, user_details)
        except ProjectsNotFoundException as e:
            print('Error message: {}'.format(e.message))
            print('Server response: {}'.format(e.error_code))
            return None
        else:
            return p

    def bindAll(self,):
        print(self.projects)
        for project in self.projects:
            #if(project["sub_status"] != "closed_expired"):
            #    print("="*100)
            #    print(self.sample_get_project_by_id(project["id"]))
                #self.sample_place_project_bid(project["id"])
                print("="*100)