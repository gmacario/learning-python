# Find interesting people on medium.com
# See https://github.com/Radu-Raicea/Interesting-People-On-Medium
# See https://medium.freecodecamp.org/how-i-used-python-to-find-interesting-people-on-medium-be9261b924b0

import click
import requests
import sys
import json

MEDIUM = 'https://medium.com'


def clean_json_response(response):
    """Removes the extra characters that get returned
    with every JSON request on Medium endpoints"""
    #print("DEBUG: {0}: response={1}".format("clean_json_response", response))
    #print("DEBUG: {0}: response.text={1}".format("clean_json_response", response.text))
    jstxt = response.text.split('])}while(1);</x>')[1]
    #print("DEBUG: {0}: jstxt={1}".format("clean_json_response", jstxt))
    return json.loads(jstxt)


def get_user_id(username):
    print('Retrieving user ID...')

    url = MEDIUM + '/@' + username + '?format=json'
    print("DEBUG: {0}: url={1}".format("get_user_id", url))
    response = requests.get(url)
    response_dict = clean_json_response(response)
    return response_dict['payload']['user']['userId']


def get_list_of_followings(user_id):
    print('Retrieving users from Followings...')

    next_id = False
    followings = []
    while True:
        if next_id:
            # If this is not the first page of the followings list
            url = MEDIUM + '/_/api/users/' + user_id + '/following?limit=8&to=' + next_id
        else:
            # If this is the first page of the followings list
            url = MEDIUM + '/_/api/users/' + user_id + '/following'
        response = requests.get(url)
        response_dict = clean_json_response(response)
        payload = response_dict['payload']
        for user in payload['value']:
            followings.append(user['username'])
        try:
            # If the "to" key is missing, we've reached the end
            # of the list and an exception is thrown
            next_id = payload['paging']['next']['to']
        except:
            break
    return followings


def get_list_of_latest_posts_ids(usernames):
    print('Retrieving the latest posts...')

    post_ids = []
    for username in usernames:
        url = MEDIUM + '/@' + username + '/latest?format=json'
        response = requests.get(url)
        response_dict = clean_json_response(response)
        try:
            posts = response_dict['payload']['references']['Post']
        except:
            posts = []
        if posts:
            for key in posts.keys():
                post_ids.append(posts[key]['id'])
    return post_ids


def get_post_responses(posts):
    print('Retrieving the post responses...')

    print("DEBUG: {0}: posts={1}".format("get_post_responses", posts))
    responses = []
    for post in posts:
        url = MEDIUM + '/_/api/posts/' + post + '/responses'
        response = requests.get(url)
        print("DEBUG: {0}: post=${1} ==> response={2}".format("get_post_responses", post, response))
        response_dict = clean_json_response(response)
        #
        #responses += response_dict['payload']['value']
        #
        item = response_dict['payload']['value']
        #
        # UnicodeEncodeError: 'UCS-2' codec can't encode characters in position 56492-56492: Non-BMP character not supported in Tk
        #print("DEBUG: {0}: item={1}".format("get_post_responses", item))
        responses += item
        #
    print("DEBUG: {0}: returning {1} elements in responses[]".format("get_post_responses", len(responses)))
    return responses


def get_user_ids_from_responses(responses, recommend_min):
    print("DEBUG: {0}(responses={1}, recommend_min={2})".format("get_user_ids_from_responses", '?', recommend_min))

    user_ids = []

    for response in responses:
        recent = check_if_recent(response)
        high_recommends = check_if_high_recommends(response, recommend_min)
        if recent and high_recommends:
            user_ids.append(response['creatorId'])

    return user_ids


def get_usernames(users):
    print("DEBUG: {0}(users={1})".format("get_usernames", users))
    print('Retrieving usernames of interesting users...')

    usernames = []

    for user_id in user_ids:
        url = MEDIUM + '/_/api/users/' + user_id
        response = requests.get(url)
        response_dict = clean_json_response(response)
        usernames.append(response_dict['payload']['value']['username'])

    return usernames


# Adds list of interesting users to the interesting_users.csv and adds a timestamp
def list_to_csv(interesting_users_list):
    # TODO
    pass


def get_interesting_users(username, recommend_min):
    print("DEBUG: {0}: username={1}".format("get_interesting_users", username))
    print('Looking for interesting users for %s...' % username)
    
    user_id = get_user_id(username)
    print("DEBUG: {0}: user_id={1}".format("get_interesting_users", user_id))
    usernames = get_list_of_followings(user_id)
    print("DEBUG: {0}: usernames={1}".format("get_interesting_users", usernames))
    posts = get_list_of_latest_posts_ids(usernames)
    print("DEBUG: {0}: posts={1}".format("get_interesting_users", posts))
    responses = get_post_responses(posts)
    #
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    #
    # **FIXME**: TRY WORKAROUND FOR
    #
    # Traceback (most recent call last):
    #  File "D:\data\github\gmacario\learning-python\findpeople\medium_find_people.py", line 102, in <module>
    #    interesting_users = get_interesting_users('gmacario', 5)
    #  File "D:\data\github\gmacario\learning-python\findpeople\medium_find_people.py", line 95, in get_interesting_users
    #    print("DEBUG: {0}: responses={1}".format("get_interesting_users", responses))
    # UnicodeEncodeError: 'UCS-2' codec can't encode characters in position 387823-387823: Non-BMP character not supported in Tk
    #
    # See https://stackoverflow.com/questions/32442608/ucs-2-codec-cant-encode-characters-in-position-1050-1050
    #
    # print("DEBUG: {0}: responses={1}".format("get_interesting_users", str(responses).translate(non_bmp_map)))
    #
    users = get_user_ids_from_responses(responses, recommend_min)
    print("DEBUG: {0}: users={1}".format("get_interesting_users", users))
    return get_usernames(users)

print('DEBUG: findpeople.finder: Hello, world!')

@click.command()
@click.option('-n', '--name', default='gmacario', help='Medium username')
@click.option('-r', '--min-recommendations', default=2, help='Minimum number of recommendations per response')
def main(name, min_recommendations):

    print("DEBUG: findpeople.finder.main() BEGIN")

    # interesting_users = get_interesting_users('gmacario', 5)
    # interesting_users = get_interesting_users('Radu_Raicea', 10)
    interesting_users = get_interesting_users(name, min_recommendations)
    print(interesting_users)
    # list_to_csv(interesting_users)

# ------------------
# import pdb; pdb.set_trace()
get_interesting_users('gmacario', 2)

if __name__ == '__main__':
    main()

# EOF
