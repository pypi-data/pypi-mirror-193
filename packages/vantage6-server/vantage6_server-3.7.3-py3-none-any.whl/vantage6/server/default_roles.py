from enum import Enum

from vantage6.server.model.rule import Operation, Scope


# Name of the default roles
class DefaultRole(str, Enum):
    ROOT = "Root"
    CONTAINER = "container"
    NODE = "node"
    VIEWER = "Viewer"
    RESEARCHER = "Researcher"
    ORG_ADMIN = "Organization Admin"
    COL_ADMIN = "Collaboration Admin"


# TODO BvB 22-06-07: we now have to pass this 'db' module as argument to a
# function because that module has a connection to the database. This should
# not be necessary. Fix that after fixing the circular imports described in
# https://github.com/vantage6/vantage6/issues/53
# Then simply do: import vantage6.server.db
def get_default_roles(db):
    # Define default roles
    # 1. Root user
    SUPER_ROLE = {
        'name': DefaultRole.ROOT,
        'description': "Super role",
        'rules': db.Rule.get()
    }
    # 2. Role for viewing organization resources
    VIEWER_RULES = [
        db.Rule.get_by_('user', Scope.OWN, Operation.EDIT),
        db.Rule.get_by_('user', Scope.OWN, Operation.DELETE),
        db.Rule.get_by_('user', Scope.ORGANIZATION, Operation.VIEW),
        db.Rule.get_by_('organization', Scope.ORGANIZATION, Operation.VIEW),
        db.Rule.get_by_('organization', Scope.COLLABORATION, Operation.VIEW),
        db.Rule.get_by_('collaboration', Scope.ORGANIZATION, Operation.VIEW),
        db.Rule.get_by_('role', Scope.ORGANIZATION, Operation.VIEW),
        db.Rule.get_by_('node', Scope.ORGANIZATION, Operation.VIEW),
        db.Rule.get_by_('task', Scope.ORGANIZATION, Operation.VIEW),
        db.Rule.get_by_('result', Scope.ORGANIZATION, Operation.VIEW),
        db.Rule.get_by_('port', Scope.ORGANIZATION, Operation.VIEW),
        db.Rule.get_by_('event', Scope.ORGANIZATION, Operation.VIEW),
    ]
    VIEWER_ROLE = {
        'name': DefaultRole.VIEWER,
        'description': "Can manage their own account and view resources "
                       "related to their organization",
        'rules': VIEWER_RULES
    }
    # 3. Researcher role
    RESEARCHER_RULES = VIEWER_RULES + [
        db.Rule.get_by_('task', Scope.ORGANIZATION, Operation.CREATE),
        db.Rule.get_by_('task', Scope.ORGANIZATION, Operation.DELETE),
    ]
    RESEARCHER_ROLE = {
        'name': DefaultRole.RESEARCHER,
        'description': "Can perform tasks, manage their own account, and "
                       "view resources related to their organization",
        'rules': RESEARCHER_RULES
    }
    # 4. Organization administrator role
    ORG_ADMIN_RULES = RESEARCHER_RULES + [
        db.Rule.get_by_('user', Scope.ORGANIZATION, Operation.CREATE),
        db.Rule.get_by_('user', Scope.ORGANIZATION, Operation.EDIT),
        db.Rule.get_by_('user', Scope.ORGANIZATION, Operation.DELETE),
        db.Rule.get_by_('organization', Scope.ORGANIZATION, Operation.EDIT),
        db.Rule.get_by_('role', Scope.ORGANIZATION, Operation.CREATE),
        db.Rule.get_by_('role', Scope.ORGANIZATION, Operation.EDIT),
        db.Rule.get_by_('role', Scope.ORGANIZATION, Operation.DELETE),
        db.Rule.get_by_('node', Scope.ORGANIZATION, Operation.CREATE),
        db.Rule.get_by_('node', Scope.ORGANIZATION, Operation.EDIT),
        db.Rule.get_by_('event', Scope.ORGANIZATION, Operation.CREATE),
    ]
    ORG_ADMIN_ROLE = {
        'name': DefaultRole.ORG_ADMIN,
        'description':
            "Can manage an organization including its users, roles, and nodes."
            " Also has all permissions of a researcher.",
        'rules': ORG_ADMIN_RULES
    }
    # 4. Collaboration administrator role
    COLLAB_ADMIN_RULES = ORG_ADMIN_RULES + [
        db.Rule.get_by_('user', Scope.GLOBAL, Operation.VIEW),
        db.Rule.get_by_('user', Scope.GLOBAL, Operation.CREATE),
        db.Rule.get_by_('user', Scope.GLOBAL, Operation.EDIT),
        db.Rule.get_by_('organization', Scope.GLOBAL, Operation.VIEW),
        db.Rule.get_by_('organization', Scope.GLOBAL, Operation.EDIT),
        db.Rule.get_by_('collaboration', Scope.GLOBAL, Operation.VIEW),
        db.Rule.get_by_('collaboration', Scope.GLOBAL, Operation.EDIT),
        db.Rule.get_by_('role', Scope.GLOBAL, Operation.VIEW),
        db.Rule.get_by_('node', Scope.GLOBAL, Operation.CREATE),
        db.Rule.get_by_('node', Scope.GLOBAL, Operation.VIEW),
        db.Rule.get_by_('node', Scope.GLOBAL, Operation.DELETE),
        db.Rule.get_by_('event', Scope.COLLABORATION, Operation.VIEW),
        db.Rule.get_by_('event', Scope.COLLABORATION, Operation.CREATE),
    ]
    COLLAB_ADMIN_ROLE = {
        'name': DefaultRole.COL_ADMIN,
        'description':
            "Can manage an collaboration including its organization and users."
            " Also has permissions of an organization admin.",
        'rules': COLLAB_ADMIN_RULES
    }
    # Combine all in array
    return [
        SUPER_ROLE, VIEWER_ROLE, RESEARCHER_ROLE, ORG_ADMIN_ROLE,
        COLLAB_ADMIN_ROLE
    ]
