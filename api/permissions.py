from rest_framework import permissions, exceptions


class HasGeneralReadScope(permissions.BasePermission):
    """
    Allows access only to clients with general scope.
    """

    def has_permission(self, request, view):
        return (
            request.auth and
            'cvut:utvs:general:read' in request.auth['scope']
        )
