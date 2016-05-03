from rest_framework import permissions, exceptions


class HasGeneralReadScopeOrIsApiRoot(permissions.BasePermission):
    '''
    Allows access only to clients with general scope.
    '''

    def has_permission(self, request, view):
        if view.get_view_name() == 'Api Root':
            return True

        return (
            request.auth and
            'cvut:utvs:general:read' in request.auth['scope']
        )


class HasEnrollmentsAcces(permissions.BasePermission):
    '''
    Allows access only to clients which should be able to see enrollments.
    '''

    def has_permission(self, request, view):
        if not request.auth:
            return False

        if 'cvut:utvs:enrollments:all' in request.auth['scope']:
            return True

        if ('cvut:utvs:enrollments:by-role' in request.auth['scope'] and
                'B-00000-ZAMESTNANEC' in request.auth['roles']):
            return True

        if ('cvut:utvs:enrollments:personal' in request.auth['scope'] and
                'personal_number' in request.auth):
            # we should check for this in has_object_permission()
            # but it doesn't apply for list queries
            # so filter the queryset instead
            view.queryset = view.queryset.filter(
                personal_number=request.auth['personal_number'])
            return True

        return False
