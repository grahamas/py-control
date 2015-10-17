import utils

import mailing

all_creds = utils.load_json('../credentials.json')
control_creds = all_credentials['control']

all_users = utils.load_json('../users.json')
admin_user_list = all_users['admin']
admin_user = admin_user_list[0]