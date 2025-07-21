# ensures an input user is part of input group. if no, warn and exit 1. if yes, exit 0

#!/usr/bin/env python3

import pwd
import grd

def group_membership_enforcer(user, group):
    user_uid = pwd.getpwnam(user).pw_uid
    user_
    ideal_gid = grd.getgrnam(group).gr_uid